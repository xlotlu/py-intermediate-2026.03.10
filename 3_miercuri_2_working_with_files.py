# acestea sunt căi absolute
#path = r"C:\Users\etc..."
path = "/tmp/myfile.txt"

# ATENȚIE:
# forma default a lui `open()` așteaptă un fișier text!
f = open(path)
print(f.read())

# ATENȚIE 2:
# vrem să specificicăm enconding-ul întotdeauna!
# (când lucrăm cu fișiere text)
f = open(path, encoding="utf-8")
print(f.read())


# avem 2 pattern-uri de lucrat cu fișiere:

# 1) citim tot conținutul în memorie
f = open(path, encoding="utf-8")
content = f.read()

# 2) iterăm prin fișier (linie cu linie)
f = open(path, encoding="utf-8")
for line in f:
    print(line)


# De ținut minte: și `.read()` și iterația
# mută file-pointer-ul intern, și vor "consuma"
# fișierul până ajung la End Of File.


# Exercițiu:
# scrieți o funcție get_contents(filename) ce returnează
# un string cu conținutul fișierului.
def get_contents(filename):
    f = open(filename, encoding="utf-8")
    return f.read()


print(get_contents("test.txt"))


# `with` introduce un "context manager".
# un context manager (poate) face ceva special
# la deschiderea și la închiderea "contextului".

with open("test.txt", encoding="utf-8") as f:
    content = f.read()
    print(content)

# în particular, context-manager-ul creat de `open()`
# va face `.close()` indiferent dacă a fost o excepție
# sau nu în logica internă.

# Exercițiu:
# rescrieți funcția `get_contents()`
# pentru a folosi context manager
def get_contents(filename):
    with open(filename, encoding="utf-8") as f:
        content = f.read()
        return content


# Exercițiu:
# scrieți funcția
def write_contents(filename, txt):
    pass

def write_contents(filename, txt):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(txt)
    

write_contents("open_docs.txt", open.__doc__)


# Exercițiu / întrebare:
# cum lăsăm utilizatorul să specifice encoding-ul
# pentru funcțiile `get_contents()` / `write_contents()`
# păstrând în același timp default-ul "utf-8"?

def get_contents(filename, encoding="utf-8"):
    with open(filename, encoding=encoding) as f:
        content = f.read()
        return content

def write_contents(filename, txt, encoding="utf-8"):
    with open(filename, "w", encoding=encoding) as f:
        f.write(txt)


# Exercițiu: 
# scrieți o funcție
def grep(filename, txt, encoding="utf-8"):
    pass

# ce printează toate liniile din `filename`
# care conțin string-ul `txt`.

def grep(filename, txt, encoding="utf-8"):
    with open(filename, encoding=encoding) as f:
         for line in f:
             if txt in line:
                print(line.removesuffix("\n"))

grep("open_docs.txt", "read")

# îmbunătățiți funcția `grep()`
# pentru a îi adăuga argumentul opțional
# `insensitive` cu valoare default `False`

# case-sensitive     "u" != "U"
# case-insensitive   "u" == "U"

def grep(filename, txt, insensitive=False, encoding="utf-8"):
    # ne normalizăm input data
    if insensitive:
        # folosim .casefold() și nu .lower()
        # pentru că nu toate caracterele sunt normalizate la fel
        # când sunt în context uppercase și lowercase
        # (exemplu: ß)
        txt = txt.casefold()

    with open(filename, encoding=encoding) as f:
        for line in f:
            if (insensitive and txt in line.casefold()) or (txt in line):
                print(line.removesuffix("\n"))


# Scrieți o funcție
def grepinto(source_fname, target_fname, txt, insensitive=False, encoding="utf-8"):
    pass
# ce scrie liniile din fișierul `source_fname` ce conțin string-ul `txt`
# în fișierul `target_fname`

# un fișier deschis pentru citire
# un fișier deschis pentru scriere

def grepinto(source_fname, target_fname, txt,
             insensitive=False, encoding="utf-8"):
    with open(source_fname, encoding=encoding) as source_f:
        with open(target_fname, 'w', encoding=encoding) as target_f:
            pass

# !!! statement-ul `with` suportă contexte multiple într-o singură declarație
#     (separate prin virgulă)
def grepinto(source_fname, target_fname, txt,
             insensitive=False, encoding="utf-8"):
    with open(source_fname, encoding=encoding) as source_f, \
         open(target_fname, 'w', encoding=encoding) as target_f:
        pass

def grepinto(source_fname, target_fname, txt,
             insensitive=False, encoding="utf-8"):
    
    if insensitive:
        txt = txt.casefold()

    with (
        open(source_fname, encoding=encoding) as source_f,
        open(target_fname, 'w', encoding=encoding) as target_f
    ):
        for line in source_f:
            if (insensitive and txt in line.casefold()) or (txt in line):
                target_f.write(line)

grepinto("open_docs.txt", "grepped_docs.txt", "ReaD", insensitive=True)