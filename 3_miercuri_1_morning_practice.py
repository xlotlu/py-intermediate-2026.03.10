#1. Scrieți o funcție
def find_appearances(lst, s):
    pass
# care primind o listă, detectează numărul de apariții
# al substringului `s` în elementele lui `lst`.
# Exemplu:
find_appearances(["ala", "bala", "porto", "cala tralalala"], "ala") == 5

def find_appearances(lst, s):
    count = 0
    for i in lst:
        count += i.count(s)
    return count

#2. Dată fiind lista
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
# creați o listă nouă cu orașele care încep cu litera "B" sau "C".
lst = []
for city in cities:
    if city.startswith("B") or city.startswith("C"):
        lst.append(city)
print(lst)

#3. Dată fiind lista
l = [1, 2, 3, 4, 5]
# aflați suma pătratelor elementelor din l.

suma = 0
for elem in l:
    suma = suma + elem ** 2
print(suma)

#4. Dată fiind lista de tuple de forma (nume, vârstă)
candidates = [
    ('Mara', 28),
    ('George', 16),
    ('Dragoș', 42),
    ('Ana', 74),
    ('Mircea', 31),
    ('Carmen', 17),
    ('Andreea', 38),
    ('Vasi', 61),
]
# creați două liste noi, `accepted` și `rejected`
# astfel încât persoanele cu vârsta între 18 și 60 de ani
# sunt acceptate, iar restul respinse.
#
# faceți asta consumând lista inițială în timp ce iterați.

# v1, fără a consuma lista
accepted = []
rejected = []
for elem in candidates:
    if 18 <= elem[1] <= 60:
        accepted.append(elem)
    else:
        rejected.append(elem)
print(accepted)
print(rejected)


# v2, consumând lista

accepted = []
rejected = []

while candidates:
    nume, varsta = candidates.pop()
    if  18 <= varsta <= 60:
        accepted.append(nume)
    else:
        rejected.append(nume)

# Întrebare: dacă voiam să păstrăm ordinea inițială?
# Răspuns 1: facem .reverse() înainte la listă
# Răspuns 2: facem .pop(0)
#
# Detaliu de implementare: .pop() este mult mai rapid decât .pop(0)
#                          mai precis, costul unui .pop(0) este același cu al lui .reverse()

#5. Dată fiind structura de date conținând o listă de
#   [name, age, hobbies]
friends = [
    ["Jane", 20, ["reading", "hiking", "biking"]],
    ["Mike", 17, ["hiking", "fishing"]],
    ["Anna", 25, []],
    ["Sam", 40, ["playing guitar"]],
    ["Dan", 34, ["painting", "reading"]],
]
# a) Îmbătrâniți-o pe Jane cu 1 an.
friends[0][1] += 1

# b) Adăugați hobby-urilor Annei "reading" și "cooking"
friends[2][2].extend(["reading", "cooking"])

# c) Ștergeți-i lui Mike hobby-ul de la indexul 1
mike = friends[1]
mikes_hobbies = mike[2]
del mikes_hobbies[1]

# d) Adăugați un prieten nou
["Georgie", 22, ["reading", "cooking", "hiking"]]
friends.append(["Georgie", 22, ["reading", "cooking", "hiking"]])


#6. Dată fiind structura de date friends de mai sus,
#   scrieți o funcție
def find_by_name(lst, name):
    for elem in lst:
        if elem[0] == name:
            return elem
#   și returnează elementul din `lst` care are la indexul 0
#   numele repectiv.
find_by_name(friends, "Sam")

#7. Similar, scrieți o funcție
def find_by_hobby(lst, hobby):
    result = []
    for elem in lst:
        hobbies = elem[2]
        if hobby in hobbies:
            result.append(elem)
    return result

# ce returnează lista persoanelor (întregul element) care au acel hobby.
find_by_hobby(friends, "hiking")

#8. La fel,
def find_by_age(lst, min_age, max_age=None):
    pass
# returnează lista persoanelor cu vârsta mai mare decât `min_age` și,
# dacă este specificat, mai mică decât `max_age`.
def find_by_age(lst, min_age, max_age=None):
    result = []
    for elem in lst:
        age = elem[1]
        # atenție, `max_age` poate să fie `None`
        if age >= min_age and (max_age is None or age <= max_age):
            result.append(elem)
    return result

#9. Folosiți `find_by_hobby` și `find_by_age` pe `friends`
#   pentru a obține lista prietenilor între 20 și 60 de ani
#   pasionați de "hiking".
find_by_age(
    find_by_hobby(friends, "hiking"),
    20, 60
)

#10. Adăugați tuturor prietenilor cu vârsta peste 30 de ani
#    hobby-ul "knitting".
for f in find_by_age(friends, 30):
    f[2].append("knitting")
