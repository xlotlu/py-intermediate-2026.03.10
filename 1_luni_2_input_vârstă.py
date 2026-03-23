# cereți utilizatorului vârsta sa
# și a prietenului său
# (faceți 2 input()-uri).
#
# după aceasta, faceți print string-ului:
# "diferența voastră de vârstă este de <x> ani"

varsta_mea = input("vârsta ta? ") # argumentul opțional este prompt-ul input()-ului
varsta_pr = input("vârsta celuilalt? ")
diferenta_varste = int(varsta_mea) - int(varsta_pr)
print(" Diferenta voastra de varsta este de " + str(diferenta_varste) + " ani")
