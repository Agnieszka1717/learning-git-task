zakupy = {
    "piekarnia" : ["chleb", "bulki", "paczek"],
    "warzywniak" : ["marchew", "seler", "rukola"]
}
print("Lista zakupów " )
for key, value in zakupy.items() :
    print(f"Idę do {key.capitalize()} i kupuję tam : {", ".join(value)} ")