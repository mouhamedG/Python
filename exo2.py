#Question1
"""import ipaddress

def detecter_ip(adresses):
    try:
        for host, adresse in adresses.items():
            try:
                ip = ipaddress.ip_address(adresse)
                print(f"{host} ({adresse}) : Adresse IP valide de version {ip.version}.")
            except ValueError:
                print(f"{host} ({adresse}) : Adresse IP invalide.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

# Exemple de dictionnaire d'adresses IP avec une erreur simulée
adresses = {
    "Serveur1": "192.168.1.1",
    "Serveur2": "2001:db8::ff00:42:8329",
    "Machine1": "256.256.256.256",
    "Erreur": None  # Erreur simulée
}

detecter_ip(adresses)"""

#*******************************************************************************#
# Question2
"""import fileinput
import os


def remplacer_lettres(chemin_fichier, lettres_a_remplacer):
    try:
        if not os.path.isfile(chemin_fichier):
            raise FileNotFoundError(f"Le fichier '{chemin_fichier}' n'existe pas.")

        with fileinput.input(chemin_fichier, inplace=True, backup='.bak') as fichier:
            for ligne in fichier:
                for lettre in lettres_a_remplacer:
                    ligne = ligne.replace(lettre, 'x')
                print(ligne, end='')

        print("Remplacement terminé avec succès !")
    except FileNotFoundError as e:
        print(f"Erreur : {e}")
    except OSError as e:
        print(f"Erreur système : {e}")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")


# Exemple d'utilisation
if __name__ == "__main__":
    chemin = input("Entrez le chemin du fichier : ")
    lettres = input("Entrez les lettres à remplacer (sans espaces, ex: adhojt) : ")
    remplacer_lettres(chemin, set(lettres))"""
#*******************************************************************************#
# Question3

"""def lire_fichier_en_dictionnaire(chemin_fichier):
    try:
        with open(chemin_fichier, "r", encoding="utf-8") as f:
            return {i + 1: ligne.strip() for i, ligne in enumerate(f)}
    except Exception as e:
        print(f"Erreur : {e}")
        return {}

# Exemple d'utilisation
chemin_fichier = input("Entrez le chemin du fichier : ")
contenu_dict = lire_fichier_en_dictionnaire(chemin_fichier)
print(contenu_dict)"""
#*******************************************************************************#
# Question4

"""def lire_fichier_en_dictionnaire(chemin_fichier):
    try:
        with open(chemin_fichier, "r", encoding="utf-8") as f:
            return {i + 1: ligne.strip() for i, ligne in enumerate(f)}
    except Exception as e:
        print(f"Erreur : {e}")
        return {}

def afficher_contenu_dictionnaire(contenu_dict):
    for num, ligne in contenu_dict.items():
        print(f"Ligne numéro {num} : {len(ligne)} caractères → \"{ligne}\"")

# Exemple d'utilisation
chemin_fichier = input("Entrez le chemin du fichier : ")
contenu_dict = lire_fichier_en_dictionnaire(chemin_fichier)
afficher_contenu_dictionnaire(contenu_dict)"""





