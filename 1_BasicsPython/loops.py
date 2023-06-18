colors_list: list = ["Orange", "Bleu", "Rouge", "Vert", "Jaune"]


for color in colors_list:
    print(color)


for i in range(11):
    print(f"Départ dans: {i}")


counter = 10
can_count = 0

while can_count < counter:
    can_count+= 1 
    print("OK")


for i in range(5):
    if i == 3:
        break
    print(i)


for color in colors_list:
    if color == "Rouge":
        continue
    print(color)


# Exercice OpenClassRoom

list_user: list = input("Saisissez une liste de nombres séparés par des virgules: ")

result = 0
for number in list_user:
    if number == ",":
        continue
    result += int(number)
print(f"Le calcul de notes est {result}")

list_user: list = input("Saisissez une liste de nombres séparés par des virgules: ")
list_user = list_user.split(",")
average_grade: int = result / len(list_user)
print(f"La moyenne des notes est de {average_grade}")

higher_than_average: int = 0
for number in list_user:
    if int(number) > higher_than_average:
        higher_than_average += 1
print(f"Il y'a {higher_than_average} notes au-dessus de la moyenne")


even_number: int = 0
counter: int = 0

while counter < len(list_user):
    if int(list_user[counter]) % 2 == 0:
        even_number += 1
    counter += 1
print(f"Il y'a {even_number} nombre paires")
