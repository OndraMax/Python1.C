import math
# proměnné a řetězce
jmeno = "Petr"
vek = 27
print(f"Jmenuji se {jmeno} a je mi {vek} let.")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers.append(11)
numbers.sort
print(f"Seřazený seznam: {numbers}")
print(f"První prvek seznamu: {numbers[0]}")
print(f"Poslední prvek seznamu: {numbers[-1]}")
# Slovníky a množiny:

student = {
    "jmeno": "Lojza",
    "vek": 20,
    "predmety": ["Matematika", "Fyztika"]
}

student ["vek"] = 27
student ["jmeno"] = "Petr"
student ["predmety"] = ["Matematika", "Fyzika", "Informatika"]
print ("Student: ", student)

data = [3, 3, 3, 4, 5, 6, 7, 8, 9, 9, 9, 10]
unique_data = set(data)
print(f"Unikátní hodnoty: {unique_data}")

for i in range(1, 11):
    if i % 3 == 0:       # cislo delitelne 3
        print("Fizz")
    elif i % 5 == 0:     # cislo delitelne 5
        print("Buzz")
    else:
        print(i)

def vypocet_obvodu_obdelniku(delka, sirka):
    return 2 * (delka + sirka)

delka = 5
sirka = 3
print(f"Obvod obdelniku s delkou {delka} a sirkou {sirka} je: {vypocet_obvodu_obdelniku(delka, sirka)}")

def vypocet_obvodu_telesa(delka, sirka=None):
    if sirka is None:
        sirka = delka
    return 2 * (delka + sirka)

delka = 5
sirka = 3
print(f"Obvod obdelniku s delkou {delka} a sirkou {sirka} je: {vypocet_obvodu_telesa(delka)}")