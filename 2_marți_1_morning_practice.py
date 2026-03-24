#1. Repetați (concatenați) string-ul "tralala" de 7 ori.
"tralala" * 7

#2. Obțineți partea întragă a împărțirii lui 17 la 4.
17 // 4

#3. Obțineți restul împărțirii lui 17 la 4.
17 % 4

#4. 8 la puterea a 3a?
8 ** 3

#5. Dat fiind variabilele `is_student` (boolean) și `name` (str),
#   scrieți un condițional care să facă print textului
#   "<name> is a student" / "<name> is not a student" după caz.

# Testați cu variabilele
name = Jane
is_student = True

if is_student:
    print (name +" is a student")
else:
    print (name +" is not a student")

# și apoi cu
name = Andrew
is_student = False

if is_student:
    print (name +" is a student")
else:
    print (name +" is not a student")

#6. Scrieți o funcție `cube(x)` ce calculează `x` la puterea a 3a.
def cube(x):
     return (x ** 3)

#7. Dat fiind string-ul
s = "Bună dimineața"

# - verificați dacă începe cu "Bu"
s.startswith ("Bu")
# - verificați dacă se termină cu "aa"
s.endswith("aa")
# - numărați apariția caracterului "a"
s.count("a")
# - obțineți prima poziție pe care apare caracterul "n"
s.find("n")
# - obțineți a doua poziție pe care apare caracterul "n"
# - [avansat, opțional] obțineți a doua poziție pe care apare caracterul "n"
#   scriind cod generic, ce se potrivește oricărui string. testați.
s.find("n", s.find("n") + 1)

#8. Dat fiind string-ul template
t = "Dear {name}, you just received €{amount} in your account {account}."
#   folosiți metoda .format() pentru a popula string-ul.
t.format(name="John",amount=10000000,account="RO12XXXX")

#9. Dat fiind string-ul
h = "===Column header==="
#   extrageți numele coloanei fără caracterele "=".
h.replace("=", "")

#10. Dat fiind string-ul
h = "Column header"
#   generați un string nou cu lungime de 25 de caractere
#   pad-uit la stânga și la dreapta cu caracterul "#".
h.center(25, "#")

#11. Dat fiind variabila globală
M_TO_FT = 3.28084
#    scrieți două funcții de conversie,
#    `feet_to_meters(ft)` și `meters_to_feet(m)`.

def meters_to_feet(m):
    return (m * M_TO_FT)

def feet_to_meters(ft):
    return (ft / M_TO_FT)

#12. [opțional] Scrieți o funcție
def format_minutes(total_minutes):
    pass
#    ce, primind un număr întreg,
#    returnează un string formatat "ore:minute".
#    Exemplu: 72 --> "1:12"; "62" --> "1:02".

def format_minutes(total_minutes):
    hours = total_minutes // 60
    minutes = total_minutes % 60
    
    return "{}:{}".format(hours, str(minutes).rjust(2, "0"))

# alternativ, folosind f-strings
def format_minutes(total_minutes):
    hours = total_minutes // 60
    minutes = total_minutes % 60
    
    return f"{hours}:{minutes:02d}"


#13. [extra-opțional] Scrieți o funcție
def get_seconds_from_now(timespec):
    pass
#    ce returnează numărul de secunde din
#    momentul curent până la următoarea apariție
#    a lui `timespec` (ce poate fi azi sau mâine).
#
#    considerați `timespec` în format "HH:MM".
#
#    care este utilitatea unei astfel de funcții?
#
#    îmbunătățire posibilă: procesați `timespec`
#    în oricare din formatele: "SS" / "MM:SS" / "HH:MM:SS"


#"12:22" --> 3872
#"11:00" --> 86328