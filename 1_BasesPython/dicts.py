campain: dict = {}
campain["name"] = "John Doe"
print(campain)

campain["created_at"] = "17/08/1986"
campain["end_date"] = "15/08/1997"
print(campain)
print(campain.get("name"))
campain.pop("end_date")
print(campain)

if "name" in campain:
    print("La valeur name existe")
else:
    print("La valeur name n'existe pas")

# Exercice OpenClassRoom

fruits: dict = {}
fruits["pomme"] = "Rouge"
fruits["banane"] = "Jaune"
fruits["orange"] = "Orange"
fruits["kiwi"] = "Vert"
couleur_banane = fruits.get("banane")
fruits["pomme"] = "Vert"
fruits.pop("orange")
print(f"Voici les valeurs restante pour fruits.json: \n {fruits.keys()}")