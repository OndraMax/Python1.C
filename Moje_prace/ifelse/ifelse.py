# Jde jen o ukázkové heslo pro procvičení podmínek.
heslo = input("Zadej heslo: ")

if heslo != "tajne123":
    print("Špatné heslo!")
else:
    # Na věk se ptáme pouze po zadání správného hesla.
    while True:
        try:
            vek = int(input("Kolik ti je let? "))
        except ValueError:
            print("Zadej věk jako celé číslo.")
            continue

        if vek < 0:
            print("Věk nemůže být záporný.")
        else:
            break

    if vek >= 18:
        print(f"Je ti alespoň 18 let, přístup povolen!")
    else:
        zbyva = 18 - vek
        # Podle počtu zbývajících let vybereme správný tvar slova.
        if zbyva == 1:
            print("Do přístupu ti zbývá 1 rok.")
        elif zbyva <= 4:
            print(f"Do přístupu ti zbývají {zbyva} roky.")
        else:
            print(f"Do přístupu ti zbývá {zbyva} let.")
