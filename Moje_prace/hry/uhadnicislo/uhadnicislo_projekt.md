# Uhodni číslo

# Popis a cíl projektu

Vytvořit hru na hádání čísla a procvičit náhodná čísla, podmínky a cyklus.

# O co jde?

Program vybere číslo od 1 do 20. Uživatel zadává tipy a dostává nápovědu,
jestli má zkusit větší nebo menší číslo. Po uhodnutí se vypíše počet pokusů
a hra skončí. Počítají se všechny číselné tipy, i ty mimo rozsah.
Text místo čísla zatím způsobí pád programu.

# Technická část

Soubor `uhadnicislo.py` používá random.randint, input a int.
Cyklus while opakuje zadávání tipů. Podmínky if/elif/else porovnávají tip
s tajným číslem. Break ukončí cyklus při uhodnutí.

# Kontrola funkčnosti

Zadávat čísla od 1 do 20 a sledovat nápovědu. Při uhodnutí se má hra
ukončit a vypsat správný počet pokusů.

# Evidence dokumentace

Dokumentace doplněna 24. 11. 2026 k již existujícímu programu.
