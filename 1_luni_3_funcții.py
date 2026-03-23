# știind că funcția de rădăcină pătrată se numește `sqrt`
# și se găsește în modulul math,
# știind că operatorul de ridicare la putere este **,
# scrieți o funcție hyp(c1, c2)
# ce returnează ipotenuza unui triunghi dreptunghic
# cu catetele `c1` și `c2`

from math import sqrt

def hyp(c1, c2):
    return sqrt(c1 ** 2 + c2 ** 2)


# Write a function `get_words` which receives a string
# as a parameter and does the following:
# - removes punctuation marks (, . ! and ?)
# - transforms everything to lowercase
# - splits the string by space
# - returns the list of words

# Call the function on a sentence like:
s = "One warm, sunny day Jessica and Lilly went to the Zoo. \
    When they arrived, they visited the monkeys?"

def get_words(txt):
    txt = (
        txt.replace(",", " ")
           .replace(".", " ")
           .replace("!", " ")
           .replace("?", " ")
    )
    return txt.lower().split()

print(get_words(s))

