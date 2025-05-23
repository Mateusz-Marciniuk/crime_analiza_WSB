# crime_analiza_WSB
Skład: Mateusz Marciniuk, Krzysztof Sadło, Wojciech Szostak
Opis: Analiza zabójstw w Indiach w latach 2020-2024 
Szczegoły : w trakcie pracy nad projektem
Data set: https://www.kaggle.com/datasets/sudhanvahg/indian-crimes-dataset


Zawsze pokazuj szczegóły

Kopiuj
# Prepare the analysis content
markdown_content = """
# Krótka analiza danych przestępczości w Indiach

## Opis kolumn:
1. **Report Number** – unikalny numer zgłoszenia przestępstwa.
2. **Date Reported** – data zgłoszenia przestępstwa.
3. **Date of Occurrence** – data wystąpienia przestępstwa.
4. **Time of Occurrence** – godzina wystąpienia przestępstwa.
5. **City** – miasto, w którym miało miejsce zdarzenie.
6. **Crime Code** – kod przypisany do rodzaju przestępstwa.
7. **Crime Description** – opis rodzaju przestępstwa (np. kradzież tożsamości, zabójstwo).
8. **Victim Age** – wiek ofiary.
9. **Victim Gender** – płeć ofiary (M - mężczyzna, F - kobieta).
10. **Weapon Used** – rodzaj użytej broni (np. broń palna, tępy przedmiot).
11. **Crime Domain** – kategoria przestępstwa (np. przestępstwo z użyciem przemocy).
12. **Police Deployed** – liczba policjantów zaangażowanych w sprawę.
13. **Case Closed** – czy sprawa została zamknięta (Yes/No).
14. **Date Case Closed** – data zamknięcia sprawy (jeśli została zamknięta).

## Krótka analiza:
- Dane zawierają **ponad 40 tysięcy zgłoszeń** przestępstw z różnych miast Indii.
- Występuje **pełne pokrycie danych** we wszystkich kolumnach z wyjątkiem `Date Case Closed`, która zawiera wartości tylko dla przypadków zamkniętych.
- Główne kategorie przestępstw to m.in. **Identity Theft**, **Homicide**, **Kidnapping**, **Burglary** i **Vandalism**.
- Wiek ofiar jest różnorodny – dane obejmują młodzież i dorosłych.
- Występuje zróżnicowanie w liczbie zaangażowanych funkcjonariuszy – od pojedynczych osób do kilkunastu.
"""