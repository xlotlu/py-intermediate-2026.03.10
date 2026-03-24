Cheatsheet & stuff
==================


În Python:
 - totul este o referință
 - totul este un obiect

Python is self-documenting.


De citit o dată în viață:
-------------------------

(dacă ești programator)

PEP-8: the styleguide:
https://peps.python.org/pep-0008/


Basic data-types:
https://docs.python.org/3/library/stdtypes.html


Formatting strings (se aplică la .format() și la f-strings):
https://docs.python.org/3/library/string.html#format-examples


Concepte:
---------

reprezentarea unui obiect
OOP = object-oriented programming
mutabilitate (int, float, str sunt immutable)


Operatori:
----------

= assignment de variabilă

aritmetici:
// câtul împărțirii
% restul împărțirii
** ridicare la putere

boolean:
== verifică egalitate
!= not equal

and
or
not

in
not in

is

Essential debugging tools:
--------------------------

print()
help()
repr()


Excepții importante:
--------------------

NameError:  variabila (funcția etc.) nu a fost definită
IndexError
ValueError: poate apărea în mai multe contexte,
            când valoarea nu este "corectă"

Metode importante ale str-ului:
-------------------------------

.find() / .index()
.count()

.replace()
.split() / .join() [!!!]
.strip() / .lstrip() / .rstrip()

.upper() / .lower()

.startswith() / .endswith()

.format()

mai puțini importante:

.center() / .ljust() / .rjust()

.translate() [TODO?]


Sequences:
----------

str, list, tuple

sunt data-type-uri:
 - iterabile
 - cu acces după index
 - și acces după slice
 - au lungime (suportă funcția `len`)
 - suportă operatorul `in` și `not in`
 - au metodele `.count()` și `.index()`
 - suportă operatorii `+` și `*`

Lucrul cu VSCode:
-----------------

Ctrl+F5     rulează tot fișierul într-un shell de sistem
Shift+Enter pe selecție rulează selecția într-un shell de Python
Ctrl+/      comment selection

Essential wisdom:
-----------------

OCD = obsessive-compulsive disorder

There are 2 hard problems in computing:
- naming things
- cache invalidation
- off-by-one errors