#1. creați un fișier "times.txt" cu următorul conținut:
s = """It was the best of times,
it was the worst of times,
it was the age of wisdom,
it was the age of foolishness,
it was the epoch of belief,
it was the epoch of incredulity,
it was the season of light,
it was the season of darkness,
it was the spring of hope,
it was the winter of despair."""

with open("times.txt", "w", encoding="utf-8") as f:
    f.write(s)


#2. modificați funcția grep de ieri
#   pentru a returna o listă de linii
#   (în loc de a face print)

def grep(filename, txt, encoding="utf-8"):
    with open(filename, encoding=encoding) as f:
        matches = []
        for line in f:
            if txt in line:
                matches.append(line.removesuffix("\n"))
        return matches

# Concept: list comprehension
source = range(10)
# obținem o listă cu pattern de acumulare
# într-un one-liner
[
    item * item        # obiectul calculat
    for item in source # for iterație
    if item % 2        # if filtrare
]

#2.5. funcția grep rescrisă cu list comprehension

def grep(filename, txt, encoding="utf-8"):
    with open(filename, encoding=encoding) as f:
        return [
            line.removesuffix("\n")
            for line in f
            if txt in line
        ]

def grep(filename, txt, insensitive=False, encoding="utf-8"):
    if insensitive:
        txt = txt.casefold()

    with open(filename, encoding=encoding) as f:
        return [
            line.removesuffix("\n")
            for line in f
            if (
                (insensitive and txt in line.casefold())
                or (txt in line)
            )
        ]



#3. citiți fișierul "data/temperatures.csv"
#   și separați cele 2 coloane în variabilele
#   `time` și `value`, apoi printați media valorilor

path = "data/temperatures.csv"

values = []
with open(path, encoding='utf-8') as f:
    content = f.readlines()
    for line in content:
        time, value = line.removesuffix("\n").split(",")
        values.append(float(value))

print(sum(values) / len(values))


#3.1. creați o listă de tuple de forma
#     (hour, average)
#     cu mediile orare pentru fiecare oră
#     existentă în sursă.

# sosul secret:
#  1) să menținem o listă de valori
#  2) să detectăm când se schimbă ora
#  3) dacă s-a schimbat, calculăm media orară
#     și reinițializăm lista de valori

path = r"data/temperatures.csv"
# times = []
values = []
result = []
previous_hour = None
with open(path, encoding='utf-8') as f:
    for line in f:
        time, value = line.removesuffix("\n").split(",")
        current_hour = time[:2]

        # dacă s-a schimbat ora
        # (și nu suntem la prima iterație)
        if previous_hour is not None and current_hour != previous_hour:
            # vrem să calculăm media veche
            medie = sum(values) / len(values)

            # și să scriem valoarea pentru ora care a trecut
            tupla = (previous_hour, medie)
            result.append(tupla)
            # și să reinițializăm lista
            values = []

        # we always append the value
        values.append(float(value))
        previous_hour = current_hour

    # la final, trebuie să calculăm și ora curentă
    # după ce s-a terminat iterația
    medie = sum(values) / len(values)
    tupla = (previous_hour, medie)
    result.append(tupla)

print(result)


# listă de date
# ordonată după un criteriu ==> putem detecta schimbarea în timpul iterației
# vrem să facem agregare (o medie în acest caz)
# după fix acest criteriu

# sosul secret: detecția schimbării
#  ---> păstrăm valoarea veche, pentru a putea compara cu cea nouă

from decimal import Decimal # aceasta este o clasă

def compute_temp_averages_from_file(filename):
    with open(filename, encoding='utf-8') as f:

        prev_hour = None

        averages = []
        values = []

        # izolez logica de creat average-ul curent
        # într-o funcție
        def compute_current_average():
            average = sum(values) / len(values)
            average = round(average, 4)

            # stochez ora veche cu media ei
            averages.append((prev_hour, average))

        for line in f:
            time, value = line.removesuffix("\n").split(",")
            # îmi normalizez și procesez datele de input
            # imediat după ce le-am obținut
            #value = float(value)

            # folosim Decimal dacă lucrăm
            # cu scientific data sau financial data
            value = Decimal(value)

            hour, minute, second = time.split(":")
            hour = int(hour)

            # nu facem încă append la valoare,
            # pentru că putem avea cazul special
            # în care s-a schimbat ora,
            # ceea ce înseamnă că trebuie să ne ocupăm
            # de dataset-ul pe care l-am strâns în memorie

            # dacă s-a schimbat ora,
            # dar(!) nu suntem la prima linie:
            # (tratăm cazul special la începutul codului)
            if hour != prev_hour and prev_hour is not None:
                # vreau să calculez media orei care tocmai a trecut
                compute_current_average()

                # reinițializăm lista de valori
                values = []
            
            # vrem să facem asta în toate cazurile
            # (motiv pentru care îl lăsăm la sfârșitul codului)
            values.append(value)

            # la fiecare row țin minte valoarea veche
            prev_hour = hour # ultima linie din for

        # nu uităm să calculăm valorile pentru ultima oră,
        # în afara for-ului!
        compute_current_average()

        return averages
    
