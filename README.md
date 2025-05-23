# crime_analiza_WSB
Skład: Mateusz Marciniuk, Krzysztof Sadło, Wojciech Szostak
Opis: Analiza zabójstw w Indiach w latach 2020-2024 
Szczegoły : w trakcie pracy nad projektem
Data set: https://www.kaggle.com/datasets/sudhanvahg/indian-crimes-dataset

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

# Analiza wykresu: Płeć ofiar

## Rozkład procentowy ofiar według płci:
- **Kobiety (F)**: 55.83% – największa grupa ofiar, ponad połowa wszystkich przypadków.
- **Mężczyźni (M)**: 33.38% – druga co do liczebności grupa.
- **Inne/niezidentyfikowane (X)**: 10.79% – osoby z niezydentifkowaną płcią.

## Wnioski:
- Kobiety są najczęściej ofiarami przestępstw w analizowanym zbiorze.
- Wysoki odsetek kategorii "X" może wskazywać na:
  - obecność osób niebinarnych,
  - brak możliwości rozpoznania płci ofiary po zdarzeniu.
  
# Analiza wykresu: Top 10 przestępstw

## Najczęściej występujące typy przestępstw:
Wykres przedstawia 10 najczęściej występujących przestępstw według liczby zgłoszeń:

1. **BURGLARY** (włamanie)
2. **VANDALISM** (wandalizm)
3. **FRAUD** (wyłudzenie)
4. **DOMESTIC VIOLENCE** (przemoc domowa)
5. **FIREARM OFFENSE** (przestępstwo z użyciem broni palnej)
6. **ROBBERY** (rozbój)
7. **KIDNAPPING** (porwanie)
8. **IDENTITY THEFT** (kradzież tożsamości)
9. **SEXUAL ASSAULT** (napastowanie seksualne)
10. **ASSAULT** (pobicie)

## Wnioski:
- Wysoka liczba przestępstw takich jak **burglary**, **vandalism** i **fraud** wskazuje na powszechność przestępstw majątkowych i uszkodzenia mienia.
- Obecność **domestic violence**, **sexual assault** oraz **assault** w pierwszej dziesiątce podkreśla znaczenie przestępstw związanych z przemocą fizyczną i psychiczną.
- Obecność **firearm offense** i **kidnapping** sugeruje także obecność poważnych zagrożeń dla bezpieczeństwa osobistego.
- Dane mogą być użyteczne dla priorytetyzacji działań policyjnych i kampanii społecznych mających na celu zapobieganie konkretnym typom przestępstw.

# Analiza wykresu: Liczba policjantów vs Rodzaj przestępstwa

## Opis wykresu:
Wykres przedstawia mapę cieplną (heatmap), gdzie:
- **Oś Y** pokazuje rodzaj przestępstwa.
- **Oś X** przedstawia liczbę policjantów przydzielonych do danego zgłoszenia.
- **Kolor oraz wartość liczby w kafelku** reprezentuje **liczbę wystąpień** danego rodzaju przestępstwa przy danej liczbie funkcjonariuszy.

## Wnioski:
- **Częstotliwość występowania**:
  - Przestępstwa takie jak **BURGLARY**, **ROBBERY**, **FRAUD** i **SEXUAL ASSAULT** występowały często przy różnych poziomach zaangażowania sił policyjnych.
  - W szczególności **VANDALISM** przy 13 funkcjonariuszach (125 przypadków) i **DOMESTIC VIOLENCE** przy 6 funkcjonariuszach (126 przypadków) wskazują na konkretne wzorce alokacji.

- **Popularne konfiguracje**:
  - Wiele przestępstw najczęściej obsługiwanych było przez około 10–13 funkcjonariuszy.
  - Liczby policjantów rzadziej przekraczają 15, co może oznaczać ograniczenia kadrowe lub że większość przestępstw nie wymaga bardzo dużych sił policyjnych.

- **Zastosowanie praktyczne**:
  - Wzorce te mogą być wykorzystane do efektywniejszego planowania zasobów ludzkich w policji.
  - Analiza może pomóc w identyfikacji sytuacji, gdzie standardowe przydziały funkcjonariuszy są najbardziej skuteczne lub wymagają dostosowania.

# Analiza wykresu: Czas zamknięcia sprawy

## Opis wykresu:
Histogram przedstawia rozkład liczby spraw w zależności od liczby dni potrzebnych do ich zamknięcia.

- **Oś X (Dni)**: Liczba dni potrzebnych do zamknięcia sprawy.
- **Oś Y (Liczba spraw)**: Liczba spraw zamkniętych w danym przedziale czasowym.
- **Niebieska przerywana linia** oznacza **średni czas zamknięcia sprawy**, który wynosi około **89 dni**.

## Wnioski:
- Większość spraw (dominująca część histogramu) została zamknięta w czasie krótszym niż 100 dni.
- Największa liczba spraw została zakończona w przedziale **0–30 dni**, co sugeruje, że wiele zgłoszeń może dotyczyć mniej skomplikowanych przypadków.
- Rozkład jest **silnie prawostronnie skośny** – oznacza to, że większość spraw kończy się stosunkowo szybko, ale istnieje niewielka liczba przypadków, które trwają **nawet ponad 700 dni**.
- Średnia (89 dni) jest przesunięta w prawo względem największych słupków, co jest typowe dla rozkładów z tzw. „długim ogonem”.

## Zastosowanie praktyczne:
- Dane mogą pomóc w identyfikacji przypadków wymagających szczególnej uwagi (np. spraw trwających ponad 200 dni).
- Potencjalna optymalizacja procesu zamykania spraw może koncentrować się na skróceniu czasu najdłuższych postępowań.

# Analiza wykresu: Przestępstwa na 100 000 mieszkańców (2020–2025)

## Opis wykresu:
Wykres przedstawia liczbę przestępstw przypadających na 100 000 mieszkańców w wybranych miastach Indii w latach 2020–2024 (2025 brak danych).

- **Oś X**: miasta (m.in. Ahmedabad, Bangalore, Chennai, Jaipur, Mumbai).
- **Oś Y**: liczba przestępstw na 100 000 mieszkańców.
- Każdy słupek reprezentuje inny rok (kolory).

## Wnioski:

### 1. **Tendencja spadkowa**:
- We wszystkich miastach zauważalny jest **stopniowy spadek przestępczości w przeliczeniu na mieszkańca** od 2020 do 2024 roku.
- Może to sugerować poprawę efektywności działań prewencyjnych, wzrost bezpieczeństwa lub zmianę metodologii raportowania przestępstw.

### 2. **Najwyższe wskaźniki**:
- **Jaipur**, **Pune** i **Bangalore** mają najwyższy poziom przestępczości per capita.
- **Jaipur** w 2020 roku przekroczył 37 przestępstw na 100 000 mieszkańców – najwyższy poziom na wykresie.

### 3. **Najniższe wskaźniki**:
- **Surat** oraz **Kolkata** mają najniższe wartości przestępczości przez wszystkie lata – poniżej 20 przestępstw na 100 000 mieszkańców.

### 4. **Stabilność danych**:
- W większości miast spadek jest stopniowy i systematyczny.
- Brak gwałtownych zmian między latami wskazuje na stabilne trendy przestępczości.

## Zastosowanie praktyczne:
- Analiza może wspierać decydentów w identyfikacji miast wymagających dalszej interwencji (np. Jaipur).
- Miasta o pozytywnych trendach mogą stanowić wzór do naśladowania w zakresie polityk bezpieczeństwa.

# Analiza wykresu: Czas zamknięcia sprawy wg typu przestępstwa

## Opis wykresu:
Wykres pudełkowy (boxplot) przedstawia rozkład czasu (w dniach) potrzebnego na zamknięcie sprawy w zależności od rodzaju przestępstwa.

- **Oś X**: Rodzaje przestępstw.
- **Oś Y**: Liczba dni do zamknięcia sprawy.
- Każde „pudełko” reprezentuje rozkład kwartylowy: 25%, mediana (50%) i 75%.
- „Wąsy” pokazują zakres większości danych, a punkty poza nimi mogą oznaczać wartości odstające (outliers).

## Wnioski:

### 1. **Najdłuższy czas zamykania spraw**:
- **SEXUAL ASSAULT** zdecydowanie wyróżnia się najdłuższym czasem zamykania spraw – mediany sięgają około 450 dni, a maksymalne wartości przekraczają 700 dni.
- Świadczy to o złożoności i/lub wrażliwości tych przypadków.

### 2. **Średni czas zamykania – inne przestępstwa**:
- **BURGLARY**, **ROBBERY** również mają stosunkowo wysokie mediany, w okolicach 100–150 dni.
- Inne przestępstwa takie jak **VANDALISM**, **ASSAULT**, **FRAUD**, **FIREARM OFFENSE**, **DOMESTIC VIOLENCE** są rozwiązywane szybciej – większość spraw zamykana poniżej 100 dni.

### 3. **Równomierność vs zróżnicowanie**:
- Dla **SEXUAL ASSAULT**, **BURGLARY** i **ROBBERY** występuje duże zróżnicowanie w czasie zamykania spraw, co wskazuje na przypadki bardzo skomplikowane.
- W pozostałych kategoriach czas zamykania spraw jest bardziej przewidywalny i skupiony.

## Zastosowanie praktyczne:
- Wyniki te mogą pomóc w analizie efektywności działań organów ścigania w zależności od rodzaju przestępstwa.
- Wskazują również, które typy spraw wymagają największego nakładu pracy i czasu, co może służyć do alokacji zasobów lub reform proceduralnych.

# Analiza wykresu: Płeć ofiar wg rodzaju przestępstwa

## Opis wykresu:
Wykres przedstawia liczbę ofiar różnych typów przestępstw z podziałem na płeć:
- **F** – kobiety (kolor różowy),
- **M** – mężczyźni (kolor pomarańczowy),
- **X** – inne lub nieokreślone (kolor szary).

Oś pozioma pokazuje liczbę ofiar, oś pionowa – typ przestępstwa.

## Wnioski:

### 1. **Przestępstwa zdominowane przez kobiety jako ofiary**:
- W przypadku **SEXUAL ASSAULT** i **DOMESTIC VIOLENCE** ofiarami najczęściej są kobiety – ich udział jest wyraźnie większy niż mężczyzn.
- Wskazuje to na silny związek tych typów przestępstw z przemocą wobec kobiet.

### 2. **Przestępstwa bardziej równomierne**:
- Przestępstwa takie jak **FRAUD**, **BURGLARY**, **VANDALISM**, **IDENTITY THEFT** i **FIREARM OFFENSE** wykazują bardziej równomierny udział kobiet i mężczyzn jako ofiar.

### 3. **Nieokreślona/inna płeć (X)**:
- Dla każdego typu przestępstwa widoczny jest niewielki, ale powtarzalny udział kategorii „X” – wskazuje to na przypadki bez jednoznacznego przypisania płci, które mogą wynikać z błędów w danych lub bardziej złożonej tożsamości ofiar.

## Zastosowanie praktyczne:
- Dane mogą być pomocne przy projektowaniu polityk prewencyjnych i programów wsparcia – szczególnie dla kobiet w kontekście przestępstw seksualnych i przemocy domowej.
- Może to również wspierać kampanie uświadamiające i działania profilaktyczne skierowane do określonych grup społecznych.

# Analiza wykresu: Średni czas zamknięcia sprawy vs. liczba policjantów

## Opis wykresu:
Wykres przedstawia średni czas (w dniach) potrzebny na zamknięcie sprawy w zależności od liczby funkcjonariuszy przydzielonych do sprawy.

- **Oś X**: liczba przydzielonych policjantów.
- **Oś Y**: średni czas zamknięcia sprawy (w dniach).

## Wnioski:

### 1. **Ogólna tendencja**:
- Wbrew intuicji, **większa liczba funkcjonariuszy nie skraca wyraźnie czasu zamknięcia sprawy**.
- Średni czas rośnie stopniowo wraz ze wzrostem liczby przydzielonych policjantów – od około 82 dni (przy 13 funkcjonariuszach) do ponad 94 dni (przy 8 funkcjonariuszach).

### 2. **Możliwe wyjaśnienia**:
- **Więcej funkcjonariuszy może być przydzielanych do bardziej złożonych, poważnych lub czasochłonnych spraw**, co wydłuża czas ich zamykania.
- Mniejsza liczba funkcjonariuszy może być przypisywana do prostszych spraw, które łatwiej i szybciej rozwiązać.

### 3. **Brak silnej zależności liniowej**:
- Choć występuje wzrost średniego czasu, nie jest to zależność ściśle liniowa – sugeruje wpływ innych czynników (typ przestępstwa, skomplikowanie sprawy).

## Zastosowanie praktyczne:
- Dane mogą być wykorzystane do analizy efektywności alokacji sił policyjnych.
- Można przeanalizować, czy liczba funkcjonariuszy faktycznie wpływa na przyspieszenie procedur, czy też ich liczba zależy głównie od trudności sprawy.


# Analiza wykresu: Rodzaje broni używane w przestępstwach w top 10 miastach

## Opis wykresu:
Wykres słupkowy skumulowany przedstawia liczbę przypadków użycia różnych typów broni w przestępstwach w 10 największych miastach.

- **Oś X**: Miasta (Delhi, Mumbai, Bangalore itd.).
- **Oś Y**: Liczba przypadków.
- Kolory reprezentują różne typy broni: `Knife`, `Explosives`, `Blunt Object`, `Poison`, `Other`, `Inne`.

## Wnioski:

### 1. **Delhi i Mumbai – najwyższy poziom przestępstw z użyciem broni**:
- Delhi zdecydowanie dominuje, z łączną liczbą przypadków przekraczającą 4500.
- Mumbai plasuje się na drugim miejscu (~3800), oba miasta znacząco przewyższają pozostałe pod względem liczby przypadków.

### 2. **Najczęściej używane rodzaje broni**:
- We wszystkich miastach **`Knife`** i **`Blunt Object`** należą do najczęściej używanych narzędzi przestępstwa.
- **`Explosives`** mają istotny udział tylko w największych miastach (Delhi, Mumbai, Bangalore).
- **`Poison`** i **`Other`** również są powszechne, ale w mniejszym zakresie.

### 3. **Miasta o mniejszej intensywności przestępczości z użyciem broni**:
- Miasta takie jak **Ahmedabad**, **Jaipur** i **Lucknow** mają znacznie mniejszą łączną liczbę przypadków (około 1200–1500).
- W tych miastach rozkład typów broni jest bardziej zrównoważony i nie występują znaczne wartości skrajne.

## Zastosowanie praktyczne:
- Tego typu analiza może wspierać służby porządkowe w lepszym doborze środków prewencyjnych w zależności od lokalizacji.
- Miasta o dużej liczbie przypadków z użyciem określonego typu broni mogą wymagać ukierunkowanych działań (np. kontrola nielegalnego posiadania noży).

# Analiza wykresu: Przestępstwa na 100k mieszkańców – miasta vs lata

## Opis wykresu:
Wykres przedstawia mapę cieplną (heatmap), która ukazuje przestępczość (liczba przestępstw na 100 000 mieszkańców) w 10 największych miastach Indii w latach 2020–2024.

- **Oś X**: lata (2020–2024)
- **Oś Y**: miasta
- **Wartości w komórkach**: liczba przestępstw na 100 000 mieszkańców
- **Kolorystyka**: im ciemniejszy kolor, tym wyższy wskaźnik przestępczości

## Wnioski:

### 1. **Miasta o najwyższym wskaźniku przestępczości**:
- **Jaipur** przez cały analizowany okres ma najwyższe wartości (od 37.0 w 2020 do 33.5 w 2024).
- **Pune** i **Hyderabad** również utrzymują się w czołówce, choć z tendencją spadkową.

### 2. **Miasta o najniższej przestępczości**:
- **Surat** oraz **Kolkata** mają najniższe wskaźniki – około 13–17 przestępstw na 100 000 mieszkańców.

### 3. **Tendencja ogólna**:
- W prawie wszystkich miastach widoczny jest **stały spadek** wskaźników przestępczości w analizowanym okresie.
- Może to świadczyć o poprawie skuteczności służb porządkowych, polityki bezpieczeństwa lub zmianach w sposobie raportowania przestępstw.

## Zastosowanie praktyczne:
- Wskazanie obszarów o największym ryzyku może pomóc w kierowaniu zasobów oraz wdrażaniu programów prewencyjnych.
- Spadki wskaźników przestępczości mogą być wskaźnikiem skuteczności dotychczasowych działań bezpieczeństwa miejskiego.

# Podsumowanie analizy danych o przestępczości w Indiach (2020–2025)

Analiza objęła różnorodne aspekty przestępczości w Indiach, bazując na danych z lat 2020–2025. Poniżej przedstawiono najważniejsze wnioski:

---

## 🔹 Ogólne trendy
- **Przestępczość ogółem wykazuje tendencję spadkową** w większości analizowanych miast.
- **Najbardziej niebezpieczne miasta** to Jaipur, Pune i Hyderabad (najwyższe wskaźniki na 100 tys. mieszkańców).
- **Najbezpieczniejsze miasta** to Surat i Kolkata.

---

## 🔹 Rodzaje przestępstw
- Najczęstsze przestępstwa to: **BURGLARY**, **VANDALISM**, **FRAUD**, **DOMESTIC VIOLENCE**, **ASSAULT**.
- **SEXUAL ASSAULT** charakteryzuje się najdłuższym czasem zamykania spraw.

---

## 🔹 Ofiary
- Kobiety stanowią **większość ofiar**, szczególnie w przestępstwach takich jak **SEXUAL ASSAULT** i **DOMESTIC VIOLENCE**.
- Dla większości przestępstw ofiary są podzielone dość równomiernie między płcie.

---

## 🔹 Broń i środki przemocy
- Najczęściej używaną bronią w przestępstwach są: **noże (Knife)** i **tępe przedmioty (Blunt Object)**.
- **Delhi** i **Mumbai** dominują pod względem liczby przestępstw z użyciem broni.

---

## 🔹 Siły policyjne i czas zamykania spraw
- **Większa liczba funkcjonariuszy nie zawsze przekłada się na krótszy czas zamykania spraw** – często wynika to ze złożoności sprawy.
- Średni czas zamknięcia sprawy to ok. **89 dni**, przy czym znaczna część spraw zamykana jest w mniej niż 100 dni.

---

## 📌 Wnioski końcowe:
Dane te są kluczowe dla podejmowania decyzji o alokacji zasobów, planowaniu polityk bezpieczeństwa publicznego i prowadzeniu kampanii profilaktycznych. Wskazują też, które obszary wymagają największej uwagi pod względem bezpieczeństwa i ochrony ofiar.
