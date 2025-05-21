# Import
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression

# Dane
df = pd.read_csv('crime_dataset_india.csv', dtype=str)
pop = pd.read_csv('populacja_miast_indie_2020_2024.csv')
pop.rename(columns={'Miasto': 'City'}, inplace=True)

# Typy danych
df['Report Number'] = pd.to_numeric(df['Report Number'], errors='coerce')
for year in ['2020', '2021', '2022', '2023', '2024']:
    pop[year] = pd.to_numeric(pop[year], errors='coerce')

# Płeć ofiar (barplot)
vc = df['Victim Gender'].value_counts(dropna=False).rename_axis('Płeć').reset_index(name='Liczba')
vc['%'] = round((vc['Liczba'] / vc['Liczba'].sum()) * 100, 2)

plt.figure(figsize=(6, 4))
bar = sns.barplot(data=vc, x='Płeć', y='Liczba', palette='Set2')
for i, r in vc.iterrows():
    bar.text(i, r['Liczba'] + 50, f"{r['%']}%", ha='center')
plt.title('Płeć ofiar')
plt.tight_layout()
plt.show()

# Top 10 przestępstw (barplot)
top_crimes = df['Crime Description'].value_counts().head(10).rename_axis('Typ').reset_index(name='Liczba')

plt.figure(figsize=(10, 6))
sns.barplot(data=top_crimes, y='Typ', x='Liczba', palette='Blues_d')
plt.title('Top 10 przestępstw')
plt.tight_layout()
plt.show()

# Heatmapa: rodzaj przestępstwa vs policja
ct = pd.crosstab(df['Crime Description'], df['Police Deployed'])
heat = ct.loc[top_crimes['Typ']]

plt.figure(figsize=(12, 6))
sns.heatmap(heat, annot=True, fmt="d", cmap="YlGnBu")
plt.title('Policja vs rodzaj przestępstwa')
plt.tight_layout()
plt.show()

# Histogram czasu zamknięcia spraw
df['Date of Occurrence'] = pd.to_datetime(df['Date of Occurrence'], errors='coerce')
df['Date Case Closed'] = pd.to_datetime(df['Date Case Closed'], errors='coerce')
df['Czas'] = (df['Date Case Closed'] - df['Date of Occurrence']).dt.days
czas = df['Czas'].dropna()
czas = czas[czas >= 0]
srednia = czas.mean()

plt.figure(figsize=(10, 5))
plt.hist(czas, bins=50, color='coral', edgecolor='black')
plt.axvline(srednia, color='blue', linestyle='--', label=f'Średnia = {srednia:.1f}')
plt.title('Czas zamknięcia sprawy')
plt.xlabel('Dni')
plt.ylabel('Liczba spraw')
plt.legend()
plt.tight_layout()
plt.show()

# Przestępstwa na 100k + predykcja 2025 (barplot grupowy)
pop_long = pop.melt(id_vars='City', var_name='Rok', value_name='Populacja')
crime_counts = df.groupby('City').size().reset_index(name='Liczba')
combined = pd.merge(pop_long, crime_counts, on='City', how='inner')
combined['Rok'] = combined['Rok'].astype(int)
combined['Na100k'] = (combined['Liczba'] / combined['Populacja']) * 100000
combined.dropna(inplace=True)

# Predykcja na 2025 (regresja liniowa)
pred = []
for city in combined['City'].unique():
    data = combined[combined['City'] == city]
    X = data[['Rok']].values
    y = data['Na100k'].values
    if len(X) >= 2:
        model = LinearRegression()
        model.fit(X, y)
        y_2025 = model.predict([[2025]])[0]
        pred.append({'City': city, 'Rok': 2025, 'Na100k': y_2025, 'Populacja': np.nan, 'Liczba': np.nan})

combined = pd.concat([combined, pd.DataFrame(pred)], ignore_index=True)

# Wykres przestępstw 2020–2025
pivot = combined.pivot(index='City', columns='Rok', values='Na100k')
pivot.columns = pivot.columns.astype(int)  # Upewniamy się, że kolumny to int

plt.figure(figsize=(14, 8))
x = np.arange(len(pivot.index))
width = 0.15
lata = [2020, 2021, 2022, 2023, 2024, 2025]  # Liczby, nie stringi

for i, rok in enumerate(lata):
    if rok in pivot.columns:
        plt.bar(x + i * width, pivot[rok], width=width, label=str(rok))

plt.xticks(x + width * len(lata) / 2, pivot.index, rotation=45)
plt.title('Przestępstwa na 100k mieszkańców (2020–2025)')
plt.xlabel('Miasto')
plt.ylabel('Na 100 000 mieszkańców')
plt.legend(title='Rok')
plt.tight_layout()
plt.grid(True, axis='y')
plt.show()

#wykres trendu przestępstw w czasie
df['YearMonth'] = df['Date of Occurrence'].dt.to_period('M')
trend = df['YearMonth'].value_counts().sort_index()

trend.plot(kind='line', figsize=(12, 5), marker='o', title='Liczba przestępstw w czasie')
plt.xlabel('Rok-Miesiąc')
plt.ylabel('Liczba przestępstw')
plt.tight_layout()
plt.show()


#Mapa cieplna – przestępstwa według miast i lat
heatmap = combined.pivot_table(index='City', columns='Rok', values='Na100k')
plt.figure(figsize=(12, 8))
sns.heatmap(heatmap, annot=True, fmt='.1f', cmap='OrRd')
plt.title('Przestępstwa na 100k – miasta vs lata')
plt.tight_layout()
plt.show()

#boxplot czasu zamkniecia spraw wedlug typu przestepstwa
filtered = df[(df['Czas'] >= 0) & (df['Crime Description'].isin(top_crimes['Typ']))]
plt.figure(figsize=(14, 6))
sns.boxplot(data=filtered, x='Crime Description', y='Czas', palette='coolwarm')
plt.xticks(rotation=45)
plt.title('Czas zamknięcia sprawy wg typu przestępstwa')
plt.tight_layout()
plt.show()

# stosunek męzczyzni vs kobiety dla każdego przestępstwa
pivot_gender = pd.crosstab(df['Crime Description'], df['Victim Gender'])
pivot_gender = pivot_gender.loc[top_crimes['Typ']]
pivot_gender.plot(kind='barh', stacked=True, figsize=(10, 6), colormap='Pastel1')
plt.title('Płeć ofiar wg rodzaju przestępstwa')
plt.tight_layout()
plt.show()
 
 #czas zamkniecia sprawy w zaleznosci od obecnosci policji
avg_time = df.groupby('Police Deployed')['Czas'].mean().dropna().sort_values()
avg_time.plot(kind='bar', figsize=(10, 5), color='teal')
plt.title('Średni czas zamknięcia sprawy vs. liczba policjantów')
plt.ylabel('Średnia liczba dni')
plt.tight_layout()
plt.show()

#najczesciej uzywane bronie wg miast
weapon_city = pd.crosstab(df['City'], df['Weapon Used'])

top_weapons = df['Weapon Used'].value_counts().head(5).index
weapon_city_top = weapon_city[top_weapons]
weapon_city_top['Inne'] = weapon_city.drop(columns=top_weapons).sum(axis=1)
weapon_city_top = weapon_city_top.loc[weapon_city_top.sum(axis=1).sort_values(ascending=False).head(10).index]
weapon_city_top.plot(kind='bar', stacked=True, figsize=(14, 7), colormap='tab10')
plt.title('Rodzaje broni używane w przestępstwach – top 10 miast')
plt.xlabel('Miasto')
plt.ylabel('Liczba przypadków')
plt.legend(title='Rodzaj broni')
plt.tight_layout()
plt.show()


