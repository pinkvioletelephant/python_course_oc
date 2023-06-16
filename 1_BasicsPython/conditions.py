sunny: bool = True

if(sunny):
    print("Super, allons à la plage.")

sunny: bool = False

if(sunny):
    print("Super, allons à la plage.")
else: 
    print("Il ne fait pas beau dehors, restons à la maison.")

sunny: bool = False
hot_weather: bool = True

if(sunny):
    print("Il fait beau aujourd'hui")
elif(hot_weather):
    print("Il va faire chaud aujourd'hui")
else:
    print("Il fait froid aujourd'hui, restons à la maison.")


if(sunny and hot_weather):
    print("Il va faire beau et chaud, faisons attention.")
elif(sunny or hot_weather):
    print("Il ne va pas faire froid aujourd'hui")
else:
    print("La réponse B")


seats_numbers: int = 50
seats_reserved: int = 55

if(seats_numbers < seats_reserved):
    print(f"Nous devons absolument ajouter {seats_reserved - seats_numbers} sièges.")
else: 
    print("Tout va bien aller.")

age_required: int = 18
user_age: int = 17

if(user_age >= age_required):
    print("Vous pouvez prendre place dans le cinéma")
else:
    print("Désolé, vous n'avez pas l'âge requis")


age_user_a = 17
age_user_b = 17


if(age_user_a == age_user_b):
    print(f"Wow, vous avez le même âge, à vous deux vous avez {age_user_a + age_user_b} ans!")
else: 
    print("Vous n'avez pas le même âge.")


fruit: str = "pomme"

match fruit:
    case "banane":
        print("Banane n'est pas mon fruit préféré")
    case "pomme":
        print("Bravo, la pomme est mon fruit préféré")
    case "orange":
        print("J'aime les orange mais ce n'est pas mon fruit préféré")

# Exercice OpenClassRoom
left_number: int  = 15
right_number: int = 0
symbol: str = "/"
result: int = 0

if isinstance(left_number, (int)) or isinstance(right_number, (int)):
    print("C'est bien, les deux nombres doivent être entiers")
else:
    print("Erreur: Les deux nombres doivent être des entiers.")

match symbol:
    case "+":
        print("OK")
        result = left_number + right_number
        print(f"Le résultat de l'opération est: {result}")
    case "/":
        print("OK")
        if left_number == 0 or right_number == 0:
            print("Désolé, l'opérateur arythmétique est correct, cependant il est impossible de diviser le nombre par 0.")
        elif left_number != 0 or right_number != 0:
            result = left_number / right_number
            print(f"Le résultat de l'opération est: {result}")
    case "-":
        print("OK")
        result = left_number - right_number
        print(f"Le résultat de l'opération est: {result}")
    case "*":
        print("OK")
        result = left_number * right_number
        print(f"Le résultat de l'opération est: {result}")

