import random
import string

# Opakujeme dotaz, dokud uživatel nezadá kladné číslo.
while True:
    delka = int(input("Jak dlouhé heslo chceš vygenerovat? "))

    if delka > 0:
        break  # Platná délka ukončí tuto smyčku.

    print("Délka hesla musí být alespoň 1.")

znaky = string.ascii_letters + string.digits # Spojím malé a velké písmenka, čísla a znaky
heslo = ""

for i in range(delka): # Cyklus se zopakuje podle toho jakou délku hesla zadám
    heslo += random.choice(znaky)

print(f"Tvoje nové bezpečné heslo je: {heslo}")