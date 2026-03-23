conditie = True

if conditie:
    # logică ce se rulează
    print("facem ceva")


if conditie:
    # logică ce se rulează
    print("facem ceva")
else:
    # altă logică
    print("facem altceva")

alta_conditie1 = False
alta_conditie2 = True

if conditie:
    pass  # no-op
elif alta_conditie1:
    pass
elif alta_conditie2:
    pass
# ...
else:
    pass


# Write a function called validate_password that validates a password
# based on certain criteria:
# - the password has at least 8 characters
# - the password contains at least one uppercase letter
# - the password contains at least one lowercase letter
# - the password contains at least one digit.
#
# If all criteria are met, return True; otherwise, return False.

def validate_password(pwd):
    if len(pwd) < 8:
        return False # early exit

    # restul logicii
    has_upper = False
    has_lower = False
    has_digit = False

    # iterăm pe fiecare caracter
    for c in pwd:
        if c.isupper():
            has_upper = True
        if c.islower():
            has_lower = True
        if c.isdigit():
            has_digit = True

        # optimisation
        if has_upper and has_lower and has_digit:
            return True

    return False


# Exercițiu:
# scrieți o funcție
def age_diff(v1, v2):
    pass
# ce returnează diferența dintre cele două numere,
# drept număr pozitiv (valoarea absolută)
def age_diff(v1, v2):
    diff = v1 - v2
    if diff < 0:
        diff = -diff
    return diff

# Exercițiu
# scrieți o funcție
def valid_age(v):
    pass
# ce returnează True dacă `v` este cuprins între 18 și 60
# (inclusiv) și False în celelalte cazuri.
print(valid_age(12)) # False
print(valid_age(18)) # True
print(valid_age(55)) # True
print(valid_age(61)) # False

def valid_age(v):
    if v >= 18 and v <= 60:
        return True
    else:
        return False

# v2, chaining operators
def valid_age(v):
    if 18 <= v <= 60:
        return True
    else:
        return False

# v3, simplified
def valid_age(v):
    return 18 <= v <= 60

# Exercițiu
# scrieți o funcție
def get_greeting(hour):
    pass
# ce returnează unul din stringurile următoare:
# între 5 inclusiv și 10 exclusiv: "Bună dimineața"
# între 10 și 18: "Bună ziua"
# între 18 și 22: "Bună seara"
# între 22 și 5: "Noapte bună"
def get_greeting(hour):
    if 5 <= hour < 10:
        return "Bună dimineața"
    elif 10 <= hour < 18:
        return "Bună ziua"
    elif 18 <= hour < 22:
        return "Bună seara"
    else:
        return "Noapte bună"

# Exercițiu:
# scrieți o funcție ce returnează salutul potrivit
# pentru ora curentă
from datetime import datetime

def get_current_greeting():
    now = datetime.now()
    hour = now.hour

    if 5 <= hour < 10:
        return "Bună dimineața"
    elif 10 <= hour < 18:
        return "Bună ziua"
    elif 18 <= hour < 22:
        return "Bună seara"
    else:
        return "Noapte bună"

# Exercițiu
# luați input de la utilizator numele său
# și salutați-l cu un salut de forma:
# "<salutarea potrivită> <nume>"

name = input("numele tău? ")
greeting = get_current_greeting()
print(greeting + " " + name)

# Exercițiu
# Având variabilele
# person1_name, person1_age, person2_name, person2_age
# scrieți un condițional ce printează:
# "<p1_name> este mai în vârstă decât <p2_name> cu <diff> ani"
# sau "<p1_name> și <p2_name> au aceeași vârstă"

person1_name = "John"
person1_age = 24
person2_name = "Bob"
person2_age = 45

# folosim string formatting:
template1 = "{older} este mai în vârstă decât {younger} cu {diff} ani"
template2 = "{person1} și {person2} au aceeași vârstă"

diff = age_diff(person1_age, person2_age)
#template.format(person1=person1_name, person2=person2_name, diff=diff)

if person1_age == person2_age:
    print(template2.format(person1=person1_name, person2=person2_name))
else:
    if person1_age > person2_age:
        older = person1_name
        younger = person2_name
    else:
        older = person2_name
        younger = person1_name

    print(template1.format(older=older, younger=younger, diff=diff))
