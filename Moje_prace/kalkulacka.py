print("-- VÍTEJ V KALKULAČCE ---")

cislo1 = float(input("Zadej první číslo: ")) # Použiju float(), aby kalkulačka zvládla i desetinná čísla (např. 5.5)
cislo2 = float(input("Zadej druhé číslo: "))

print("\nVyber:") # mat. operace
print(" + pro sčítání")
print(" - pro odčítání")
print(" * pro násobení")
print(" / pro dělení")

operace = input("Zadej znak - (+, -, *, /): ")

print("-" * 30)  # Oddělovací čára pro přehlednost

# 3. Rozhodování podle operace (používá if, elif, else)
if operace == "+":
    vysledek = cislo1 + cislo2
    print(f"Výsledek: {cislo1} + {cislo2} = {vysledek}")

elif operace == "-":
    vysledek = cislo1 - cislo2
    print(f"Výsledek: {cislo1} - {cislo2} = {vysledek}")

elif operace == "*":
    vysledek = cislo1 * cislo2
    print(f"Výsledek: {cislo1} * {cislo2} = {vysledek}")

elif operace == "/":
    # Napíše když budu chtít dělit nulou
    if cislo2 == 0:
        print("Chyba: Nulou nelze dělit!")
    else:
        vysledek = cislo1 / cislo2
        # :.2f zaokrouhlí výsledek na 2 desetinná místa
        print(f"Výsledek: {cislo1} / {cislo2} = {vysledek:.2f}")

else:
    # Jestli zadám něco jiného než +, -, *, /
    print("Neplatná operace! Spusť program znovu a vyber +, -, * nebo /.")