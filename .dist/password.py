
mot_de_passe = input("Veuillez entrer un mot de passe : ")

majuscule = False
minuscule = False
chiffre = False
special = False

caractere_speciaux = "/?!+=;:.,#"

for letter in mot_de_passe:

    if letter.isupper():
        majuscule = True

    if letter.islower():
        minuscule = True

    if letter.isdigit():
        chiffre = True

    if letter in caractere_speciaux:
        special = True

if majuscule and minuscule and chiffre and special:
    print("Mot de passe valide")
else:
    print("Mot de passe invalide")

