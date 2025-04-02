#Question 1 et 2
"""import os
import shutil
import datetime

def lister_dossier(dossier):
    if os.path.exists(dossier):
        fichiers = [f for f in os.listdir(dossier) if os.path.isfile(os.path.join(dossier, f))]
        print(f"📂 Contenu du dossier '{dossier}':")
        for fichier in fichiers:
            print(f" - {fichier}")
    else:
        print("❌ Le dossier n'existe pas.")

def copier_fichier(fichier_source):
    if os.path.exists(fichier_source):
        # Récupérer le dossier et le nom du fichier
        dossier = os.path.dirname(fichier_source)
        nom_fichier, extension = os.path.splitext(os.path.basename(fichier_source))

        # Obtenir la date et l'heure actuelles
        date_heure = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # Construire le nouveau nom de fichier
        nouveau_nom = f"{nom_fichier}_copie_{date_heure}{extension}"
        fichier_destination = os.path.join(dossier, nouveau_nom)

        # Copier le fichier
        shutil.copy(fichier_source, fichier_destination)
        print(f"✅ Copie créée : {fichier_destination}")
    else:
        print("❌ Le fichier source n'existe pas.")

def compter_fichiers(dossier):
    if os.path.exists(dossier):
        fichiers = [f for f in os.listdir(dossier) if os.path.isfile(os.path.join(dossier, f))]
        print(f"📂 Nombre de fichiers dans '{dossier}': {len(fichiers)}")
    else:
        print("❌ Le dossier spécifié n'existe pas.")

# Exemple d'utilisation
if __name__ == "__main__":
    dossier_travail = os.path.expanduser("~")  # Chemin générique vers le dossier utilisateur
    chemin_fichier = os.path.join(dossier_travail, "toto.txt")  # Fichier dans le dossier utilisateur

    # Lister les fichiers du dossier
    lister_dossier(dossier_travail)

    # Copier le fichier avec la date et l'heure dans le nom
    copier_fichier(chemin_fichier)

    # Compter le nombre de fichiers dans le dossier
    compter_fichiers(dossier_travail)"""
#*************************************************************************************************************#
#Question3
"""import os
import shutil
import datetime
import sys

def lister_dossier(dossier):
    if os.path.exists(dossier):
        fichiers = [f for f in os.listdir(dossier) if os.path.isfile(os.path.join(dossier, f))]
        print(f"📂 Contenu du dossier '{dossier}':")
        for fichier in fichiers:
            print(f" - {fichier}")
    else:
        print("❌ Le dossier n'existe pas.")

def copier_fichier(fichier_source):
    if os.path.exists(fichier_source):
        dossier = os.path.dirname(fichier_source)
        nom_fichier, extension = os.path.splitext(os.path.basename(fichier_source))

        date_heure = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nouveau_nom = f"{nom_fichier}_copie_{date_heure}{extension}"
        fichier_destination = os.path.join(dossier, nouveau_nom)

        shutil.copy(fichier_source, fichier_destination)
        print(f"✅ Copie créée : {fichier_destination}")
    else:
        print("❌ Le fichier source n'existe pas.")

def compter_fichiers(dossier):
    if os.path.exists(dossier) and os.path.isdir(dossier):
        try:
            fichiers = [f for f in os.listdir(dossier) if os.path.isfile(os.path.join(dossier, f))]
            print(f"📂 Nombre de fichiers dans '{dossier}': {len(fichiers)}")
        except PermissionError:
            print("❌ Erreur : Vous n'avez pas la permission d'accéder à ce dossier.")
    else:
        print("❌ Erreur : Le dossier spécifié n'existe pas ou n'est pas un dossier valide.")

# Exemple d'utilisation avec argument
if __name__ == "__main__":
    if len(sys.argv) > 1:
        dossier_a_compter = sys.argv[1]
    else:
        dossier_a_compter = os.getcwd()  # Dossier actuel par défaut

    compter_fichiers(dossier_a_compter)"""

