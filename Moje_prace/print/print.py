print("Ahoj!")
print()  # Udělá prázdný řádek

# proměnné slouží k uložení dat (text, číslo, atd.)
jmeno = "Franta"
rok = 2007

# Nejlepší způsob vypisování textu (f string)
print(f"Jmenuju se {jmeno}, narodil jsem se v roce {rok}.") # Před uvozovky napíšu f a do závorek {} dám proměnné

# V printu jdou počítat příklady
cislo_a = 15
cislo_b = 5

print()
print("---MATEMATIKA---")
print(f"Součet čísel {cislo_a} + {cislo_b} je:", cislo_a + cislo_b)
print(f"Násobení čísel {cislo_a} * {cislo_b} je:", cislo_a * cislo_b)
print()

# Funkce input() počká až uživatel něco napíše na klávesnici a odešle to.
uzivatelske_jmeno = input("Jak se jmenuješ? ")

# Odpověď použiju v dalším printu
print(f"Ahoj, {uzivatelske_jmeno}!")

# \n vytvoří nový řádek, násobení textu * ho zopakuje
print("\n" + "=" * 5)
print("Konec")
print("=" * 5)