# if-else (Heslo, Věk)
heslo = input("Zadej heslo: ")

if heslo == "tajne123":
    print("Přístup povolen!") # Jestli zadám dobré heslo, zobrazí se tohle.
else:
    print("Špatné heslo!") # Jestli zadám špatné heslo, zobrazí se tohle.

vek = int(input("Kolik ti je let? ")) # Funkce int() převede text na celé číslo, abych s ním mohl počítat.

if vek >= 18: # Pomocí f-stringu vložím hodnotu proměnné 'vek' přímo do textu
    print(f"Je ti {vek} let, přístup povolen!")
elif vek >= 14:
    print(f"Je ti {vek} let, do přístupu ti zbývájí {18 - vek} roky.")
else: # Složené závorky {18 - vek} vypočítají zbývající roky
    print(f"Je ti {vek} let, do přístupu ti zbývá {18 - vek} let.") 