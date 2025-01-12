zakupy = {
    "Sklep z pieczywem" : ["chleb", "bulki", "paczek"],
    "Sklep z warzywami" : ["marchew", "seler", "rukola"]
} # do tych sklepów chodzę zawsze
print("Lista zakupów " )
licznik = 0
for key, value in zakupy.items() :
    for i in range (0, len(value)):
        value[i] = value[i].capitalize()
        licznik = licznik + 1
    print(f"Idę do {key.capitalize()} i kupuję tam : {", ".join(value)} ")
    print (f"W sumie kupuję: {licznik} produktów.")
    # Specjalne pozdrowienia