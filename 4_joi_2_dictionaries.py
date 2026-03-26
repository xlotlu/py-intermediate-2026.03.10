# Exercițiu:
# Creați un dicționar numit `person` ce conține
# următoarele perechi cheie-valoare:
#  name:    Jane
#  age:     20
#  hobbies: ["hiking", "biking"]

# - faceți print dicționarului
# - printați valoarea pentru cheia "name"
# - îmbătrâniți-o pe Jane cu un an
# - adăugați o cheie nouă numită "friends"
#   cu valoare lista ["Andrew", "Mike", "Anna"]
# - adăugați "knitting" la hobbies


# Exercițiu:
# dat fiind dataset-ul `friends`
friends = [
    ["Jane", 20, ["reading", "hiking", "biking"]],
    ["Mike", 17, ["hiking", "fishing"]],
    ["Anna", 25, []],
    ["Sam", 40, ["playing guitar"]],
    ["Dan", 34, ["painting", "reading"]],
]
# creați o listă de dicționare cu cheile
# "name", "age", "hobbies".

friends_d =[]
for friend in friends:
    name, age, hobbies = friend # unpacking
    person = {
        "name": name,
        "age": age,
        "hobbies": hobbies,
    }
    friends_d.append(person)
print(friends_d)

# dat fiind dicționarul de ocupații
occupations = {
    "Jane": "nurse",
    "Dan": "firefighter",
    "Mike": "dancer",
    "Sam": "boat captain",
    "Anna": "gardner",
}
# în care cheia este numele persoanei din dataset-ul
# `friends`, iterați prin lista obținută mai devreme
# `friends_d` și adăugați cheia "occupation" cu valoarea
# corespunzătoare din `occupations`.

# Rezultatul friends_d va fi o listă conținând
[
    {
        'id': 27,
        'name': 'Dan',
        'age': 34,
        'hobbies': ['painting', 'reading'],
        'occupation': "firefighter",
    },
    #{...},
    #...
]

# Strategie:
# 1. iterăm în datasource
#    --> fiecare element (persoana) este dicționarul asupra căruia operăm
# 2. obținem numele persoanei din acest element
# 3. folosim acest nume drept cheie de lookup în `occupations`
# 4. obținem ocupația
# 5. în persoana curentă adăugam cheia "occupation" cu această valoare

for person in friends_d:
        name = person["name"] # "Jane"
        v = occupations[name] # "nurse"
        person["occupation"] = v

print (friends_d)


# Ne-am făcut un prieten nou:
friends_d.append({
      "name": "Jay",
      "age": 50,
      "hobbies": ["hiking", "knitting"]
})

# Între timp a mai apărut cineva în dataset-ul cu ocupații:
occupations = {
    "Jane": "nurse",
    "Dan": "firefighter",
    "Mike": "dancer",
    "Sam": "boat captain",
    "Anna": "gardner",
    "Mary": "policewoman",
}
# așa că rulăm din nou scriptul:

for person in friends_d:
        name = person["name"]
        v = occupations[name]
        person["occupation"] = v
print(friends_d)


for person in friends_d:
        name = person["name"]
        # știu că există șansă să nu existe
        try:
            v = occupations[name]
        except KeyError:
            # .. special handling?
            # i will explicitely silence the exception
            pass
        else: # se rulează dacă try a fost ok!
            person["occupation"] = v
            
print(friends_d)

# alternativ, folosind if
for person in friends_d:
        name = person["name"]
        if name in occupations:
            v = occupations[name] 
            person["occupation"] = v

# alternativ la alternativ
for person in friends_d:
        name = person["name"]

        if name not in occupations:
            continue # early exit

        v = occupations[name] 
        person["occupation"] = v
