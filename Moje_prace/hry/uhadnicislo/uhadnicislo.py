import random # Pomocí import random si do skriptu nahraju příkaz pro náhodné čísla

print("--- HRA UHODNI TAJNÉ ČÍSLO ---")
print("Myslím na číslo od 1 do 20. Zkus ho uhodnout")

tajne_cislo = random.randint(1, 20) # vybere náhodné celé číslo od 1 do 20
pocet_pokusu = 0 # Počítadlo pokusů, které je nastavené na 0

while True: # vytvoří nekonečnou smyčku. Kód se bude v loopu dokud ho nezastavím pomocí break
    tip = int(input("\nZadej svoje číslo: ")) # Načtu odpověď od uživatele a převedu ho na číslo
    pocet_pokusu += 1 # Zvýším  pokusy o 1

    if tip < tajne_cislo:
        print("Moc nízko, zkus větší číslo.")
        
    elif tip > tajne_cislo:
        print("Moc vysoko, zkus menší číslo.")
        
    else:
        print(f"\nSUPER! Uhodl jsi číslo {tajne_cislo}!") # Pokud tip není menší ani větší, znamená to, že se rovná správnému číslu
        print(f"Vypotřeboval jsi na to celkem {pocet_pokusu} pokusů.")

        break # Použiju break ukončím while True a hra skončí

print("Dohrál si hru.")