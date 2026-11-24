# Modul random obsahuje funkce pro práci s náhodnými čísly.
import random

# 1. Načtení a kontrola počtu hodů
# while True opakuje tento blok, dokud ho neukončí příkaz break.
# Díky tomu se po chybném vstupu můžeme uživatele zeptat znovu.
while True:
    # V bloku try zkusíme provést kód, při kterém může nastat chyba.
    try:
        # input() vrací text, i když uživatel napíše číslici.
        # int() převede například text "3" na celé číslo 3.
        pocet_hodu = int(input("Kolikrát chceš hodit kostkou? (1 až 100): "))
    except ValueError:
        # Sem program přejde, když int() nedokáže vstup převést.
        # Například "ahoj" nebo "2.5" nejsou zápisem celého čísla.
        print("Zadej počet hodů jako celé číslo.")
        # continue přeskočí zbytek tohoto opakování a vrátí se na začátek while.
        # Rozsah tedy nekontrolujeme, dokud nemáme správně načtené číslo.
        continue

    # Tato podmínka znamená: počet hodů je alespoň 1 a zároveň nejvýše 100.
    # Horní limit brání příliš dlouhému výpisu v terminálu.
    if 1 <= pocet_hodu <= 100:
        # Číslo je platné, takže ukončíme while a přejdeme k házení kostkou.
        break

    # Sem se dostaneme, pokud se číslo převedlo, ale je mimo povolený rozsah.
    # Po výpisu smyčka while znovu začne dotazem na počet hodů.
    print("Počet hodů musí být od 1 do 100.")

# 2. Házení kostkou a sčítání výsledků
# Před prvním hodem je součet nulový. Každý hod k němu potom přičteme.
celkem = 0

# for zopakuje odsazený blok tolikrát, kolik hodů uživatel zadal.
# Například range(3) postupně dává hodnoty 0, 1, 2, které se ukládají do i.
for i in range(pocet_hodu):
    # randint(1, 6) vybere náhodné celé číslo od 1 do 6 včetně obou krajů.
    hod = random.randint(1, 6)
    # Zkrácený zápis pro celkem = celkem + hod. Starší hody tak neztratíme.
    celkem += hod
    # i začíná od nuly, proto pro pořadí hodu vypisujeme i + 1.
    # Písmeno f před textem umožňuje vložit hodnoty do složených závorek {}.
    print(f"{i + 1}. Hodil jsi číslo: {hod}")

# Tento řádek není odsazený pod for, proto se provede až po všech hodech.
print(f"Celkový součet hodů: {celkem}")
