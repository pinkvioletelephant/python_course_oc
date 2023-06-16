socials_media: list = ["Facebook", "Slack", "YouTube"]
print(socials_media)
socials_media.append("TikTok")
print(f"Impossible de parler de réseaux sociaux sans ajouter également {socials_media}")
socials_media.remove("Facebook")
print(f"Facebook, viens de changer son nom en Meta, il n'est donc plus dans cette liste pour le moment: {socials_media}")
print(f"Il y'a pour le moment {len(socials_media)} réseaux sociaux important dans la liste.")


numbers: list = [1, 2, 3, 4, 5]

if 5 in numbers:
    print(f"5 à été trouvé dans la liste: {numbers}")
else: 
    print(f"Impossible de trouver 5 dans la liste: {numbers}")


# Exercice OpenClassRoom 
fruits_list: list = ["Pomme", "Banane", "Orange"]
fruits_list.append("Kiwi")
fruits_list.remove("Orange")
fruits_list[1] = "Ananas"
print(len(fruits_list))
fruits_list.sort()
print(f"Dans l'ordre, la liste de fruit ressemble à: {fruits_list}")