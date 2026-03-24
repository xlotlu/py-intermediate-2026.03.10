while condiție:
    execută

while True:
    do_stuff()
    if some_condition:
        break

    if value_i_dont_need:
        continue
    
    mult_cod()


from time import sleep
# let's do a timer:

def timer(s):
    "counts down from `s` seconds to zero"

    while s > 0:
        print(s)
        sleep(1)
        s -= 1   # echivalent cu s = s - 1

#v2: cu break manual
def timer(s):
    "counts down from `s` seconds to zero"

    while True:
        print(s)
        sleep(1)
        s -= 1
        if s == 0:
            # we're done
            break

# let's do a timer that prints only now and then
def skipping_timer(s, skip=5): # keyword-argument
    initial = s
    while s > 0:
        # we print only the other `skip` seconds
        if (initial - s) % skip == 0:
            print(s)

        sleep(1)
        s -= 1   # echivalent cu s = s - 1

# print only the odd numbers counting from 15 downwards
s = 15

while s > 0:
    if s % 2 == 1:
        print(s)
    s -= 1

# invers, cu continue:
while s > 0:
    s -= 1 # incrementăm la început pt. că continue
    if s % 2 == 0:
        continue
    print(s) # are un bug, îl pierde 15


# print the numbers from 15 to 8
while s > 0: # introdus alt bug, dacă este mai mic decât 8
    print(s)
    if s == 8:
        break
    s -= 1


# scrieți o funcție
def prompt_for_int(prompt="Introdu un număr întreg: "):
    pass
# ce promptează utilizatorul să introducă un nr. întreg
# și continuă să prompteze dacă valoare introdusă nu este int.
# dacă valoarea este validă, returnează numărul.

def prompt_for_int(prompt="Introdu un număr întreg: "):
    while True:
        num = input(prompt)
        if num.isdecimal():
            return int(num)
        else:
            print(f"Error: '{num}' is not a number")

def prompt_for_int(prompt="Introdu un număr întreg: "):
    while True:
        num = input(prompt)
        if not num.isdecimal():
            print(f"Error: '{num}' is not a number")
            continue
        # if we got here, the value is ok
        return int(num)

# refacem exercițiul cu diferența de vârstă:


varsta_mea = prompt_for_int("vârsta ta? ")
varsta_pr = prompt_for_int("vârsta celuilalt? ")

print(f"Diferența de vârstă este {abs(varsta_mea - varsta_pr)}")


# Concept:
# acces după index ("item access")
# obj[1]

for element in collection: # un iterabil
    do_stuff_with(element)

# range(start, stop, step)

# creați o listă cu numerele de la 20 la 1 (inclusiv),
# descrescător
list(range(20, 0, -1))

# slice
# lst[start:stop:step]

