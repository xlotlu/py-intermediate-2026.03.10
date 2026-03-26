"""
# forma cea mai simplă:
try:
    ...
except NumeExceptie:
    ...

# forma extinsă
try:
    ...
except NumeExceptie:
    ...
else:
    ...
    # această parte se rulează
    # _doar_ dacă ce s-a rulat în try
    # a fost ok
"""

# rescrieți funcția prompt_for_int
# pentru a folosi try / except în loc de if
def prompt_for_int(prompt="Introdu un număr întreg: "):
    while True:
        num = input(prompt)
        if not num.isdecimal():
            print(f"Error: '{num}' is not a number")
            continue
        # if we got here, the value is ok
        return int(num)

def prompt_for_int(prompt="Introdu un număr întreg: "):
    while True:
        # folosim try / except ca mecanism de flow control
        try:
            return int(input(prompt))
        except ValueError:
            print("Introdu un număr valid")

"""
# formă parțială, cu cleanup:
try:
    ...
finally:
    ...
    # această parte se rulează
    # __întotdeauna__!!!
    # la sfârșitul execuției


# forma și mai extinsă:
try:
    ...
except NumeExceptie:
    ...
else:
    ...
    # această parte se rulează
    # _doar_ dacă 
finally:
    ...
    # cleanup
"""


"""
# forma totală
try:
    ...
except NumeExceptie1:
    ...
except NumeExceptie2:
    ...
except:
    # catch-all
    ...
else:
    ...
    # această parte se rulează
    # _doar_ dacă 
finally:
    ...
    # cleanup
"""


# Exemplu de cleanup
# când lucram (acum mulți ani) cu fișiere

def process(txt):
    return txt[10000]

f = open("test.txt")

try:
    print("procesez")
    content = f.read()
    process(content)
finally:
    print("fac curat")
    f.close()



# Exemplu de aplicație tip long-running process
# Avem o funcție ce poate crăpa în anumite situații,
# și vrem ca procesul să nu își oprească execuția:

from time import sleep
from random import randint


def crapă():
    x = randint(0, 3)
    print("» random:", x)

    if x == 3:
        # putem genera o excepție programatic.
        # este util drept canal de comunicare lateral
        # cu alte zone ale aplicației care ne folosesc interfața.
        raise ValueError("nu-mi place valoarea " + str(x))

# main loop, aplicația rulează la nesfărșit
while True:
    try:
        crapă()
    except Exception as e: # capturăm excepția
        # vrem să aflăm de ce a crăpat
        # și să logăm
        print("[!!!] excepție:", type(e), e)

    sleep(1)
