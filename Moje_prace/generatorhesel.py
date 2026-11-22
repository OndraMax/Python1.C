import random
import string

delka = int(input("Jak dlouhé heslo chceš vygenerovat? "))

znaky = string.ascii_letters + string.digits + "!@#$%" # Spojím malé a velké písmenka, čísla a znaky
heslo = ""

for i in range(delka): # Cyklus se zopakuje podle toho jakou délku hesla zadám
    heslo += random.choice(znaky)

print(f"Tvoje nové bezpečné heslo je: {heslo}")