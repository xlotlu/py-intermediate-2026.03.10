# Exercițiu:
# dată fiind lista de orașe:
cities = [
    'București',
    'Brașov',
    'Cluj-Napoca',
    'Arad',
    'Timișoara',
    'Iași',
    'Constanța',
    'Pitești',
    'Satu Mare',
]

#1. creați o listă cu primele 3 orașe
print(cities[:3])

#2. creați o listă cu ultimele 3 orașe
print(cities[-3:])

#3. creați o listă cu elementele de la
#   indicele 2 la 5 (inclusiv)
print(cities[2:6])

#4. creați o listă cu ultimele 3 orașe
#   în ordine inversă
print(cities[:-4:-1])

#5. creați o listă nouă cu toate elementele
#   în ordine inversă
print(cities[::-1])

#6. repetați exerciții similiare pe stringul
#   (făcând slice-uri pe litere)
s = "Salutare, ce după-amiază însorită!"

# dat fiind lista de numere
range(1, 5)
# creați o listă nouă ce conține pătratele
# acestor numere

# [!!!] Pattern de acumulare
#
#0. avem acces la obiectul sursă
source = range(1, 5)
#1. definim un obiect
results = []
#2. iterăm prin sursă
for x in source:
    #3. calculăm valoarea nouă pe baza
    #   elementului sursă
    v = x * x
    #4. acumulăm
    results.append(v)
#5. suntem gata
print(results)

# extra-complexitate: filtrăm
# dat fiind lista de numere
range(1, 12)
# creați o listă nouă ce conține pătratele
# numerelor impare

#0. avem acces la obiectul sursă
source = range(1, 5)
#1. definim un obiect
results = []
#2. iterăm prin sursă
for x in source:
    #3. filtrăm
    if x % 2 == 1:
        #4. calculăm valoarea nouă pe baza
        #   elementului sursă
        v = x * x
        #5. acumulăm
        results.append(v)
#6. suntem gata
print(results)

# varianta "pe dos" [*]
#0. avem acces la obiectul sursă
source = range(1, 5)
#1. definim un obiect
results = []
#2. iterăm prin sursă
for x in source:
    #3. filtrăm
    if x % 2 != 0: # [*] tot un fel de early exit
        continue
    #4. calculăm valoarea nouă pe baza
    #   elementului sursă
    v = x * x
    #5. acumulăm
    results.append(v)
#6. suntem gata
print(results)


# Exercițiu:
# dată fiind lista `cities` de mai sus,
# creați o listă nouă cu orașele care încep
# cu litera 'C'
lst = []
for city in cities:
    if city.startswith("C"):
        lst.append(city)
print(lst)

# creati o lista noua cu orase care contine "-"
my_list = []
for c in cities:
    if "-" in c:
        my_list.append(c)


# Exercițiu:
# dată fiind lista de tuple de forma (city, distance)
cd = [
    ('Cluj-Napoca', 450),
    ('Timișoara', 550),
    ('Iași', 390),
    ('Constanța', 225),
    ('Brașov', 180),
    ('Craiova', 230),
    ('Galați', 250),
    ('Ploiești', 60),
    ('Oradea', 610),
    ('Sibiu', 275),
    ('Arad', 560),
    ('Bacău', 300),
    ('Brăila', 200),
    ('Buzău', 110),
    ('Suceava', 450),
    ('Pitești', 120),
    ('Târgu Mureș', 330),
    ('Baia Mare', 600),
]

# creați o listă nouă cu numele orașelor
# cu distanță <= 300 km

close_cities = []
for elem in cd:
    city = elem[0]
    distance = elem[1]

    if distance <= 300:
        close_cities.append(city)


# creați o listă cu primele 3 orașe găsite
# cu distanță <= 400 km
first_close_cities = []
for elem in cd:
    city = elem[0]
    distance = elem[1]

    if distance <= 400:
        first_close_cities.append(city)
        if len(first_close_cities) == 3:
            break

print(first_close_cities)

# dată fiind lista
cd = [
    ('Cluj-Napoca', 450),
    ('Timișoara', 550),
    ('Iași', 390),
    ('Constanța', 225),
    ('Brașov', 180),
    ('Craiova', 230),
    ('Galați', 250),
    ('Ploiești', 60),
    ('Oradea', 610),
    ('Sibiu', 275),
    ('Arad', 560),
    ('Bacău', 300),
    ('Brăila', 200),
    ('Buzău', 110),
    ('Suceava', 450),
    ('Pitești', 120),
    ('Târgu Mureș', 330),
    ('Baia Mare', 600),
]
# obțineți o listă nouă cu numele orașelor 
# cu distanță <= 300 km, în timp ce eliberați memoria
# (adică la finalul iterației `cd` va fi o listă goală)

# mai bine cu while. acest pattern se potrivește
# la câteva data-type-uri, care
# 1) sunt concrete în memorie
# 2) au o metodă de a fi "consumate"
# 3) doar în situațiile în care nu mai avem nevoie
#    de acces la dataset-ul inițial.
close_cities = []
while cd:
    elem = cd.pop()

    city = elem[0]
    distance = elem[1]

    if distance <= 300:
        close_cities.append(city)

print(close_cities)

# mai frumos, cu inline unpacking
close_cities = []
while cd:
    city, distance = cd.pop()

    if distance <= 300:
        close_cities.append(city)

print(close_cities)

