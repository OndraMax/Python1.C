print("Ahoj!")
print()

# Ukázkové hodnoty nejsou osobní údaje.
prezdivka = "Člověk"
cislo_a = 15
cislo_b = 5

# f-string vloží hodnotu proměnné přímo do textu.
print(f"Moje přezdívka je {prezdivka}.")
print("\n--- MATEMATIKA ---")
print(f"Součet čísel {cislo_a} + {cislo_b} je: {cislo_a + cislo_b}")
print(f"Násobení čísel {cislo_a} * {cislo_b} je: {cislo_a * cislo_b}")

uzivatelska_prezdivka = input("Zadej přezdívku (ne skutečné jméno): ")
print(f"Ahoj, {uzivatelska_prezdivka}!")

# Násobením textu vytvoříme jednoduchý oddělovač.
print("\n" + "=" * 5)
print("Konec")
print("=" * 5)
