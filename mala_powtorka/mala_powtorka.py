zakupy = {
    "piekarnia" : ["chleb", "bulki", "paczek"],
    "warzywniak" : ["marchew", "seler", "rukola"]
}
print("Lista zakupów " )
for key, value in zakupy.items() :
    for i in range (0, len(value)):
        value[i] = value[i].capitalize()
    print(f"Idę do {key.capitalize()} i kupuję tam : {", ".join(value)} ")