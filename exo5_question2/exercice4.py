# Module exercice4.py
import os
import shutil
import datetime

def lister_dossier(dossier):
    """Liste les fichiers d'un dossier."""
    if os.path.exists(dossier):
        fichiers = [f for f in os.listdir(dossier) if os.path.isfile(os.path.join(dossier, f))]
        print(f"\n📂 Contenu du dossier '{dossier}':")
        for fichier in fichiers:
            print(f" - {fichier}")
    else:
        print("❌ Le dossier n'existe pas.")

def copier_fichier(fichier_source):
    """Copie un fichier en ajoutant un horodatage au nom."""
    if os.path.exists(fichier_source):
        dossier = os.path.dirname(fichier_source)
        nom_fichier, extension = os.path.splitext(os.path.basename(fichier_source))
        date_heure = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nouveau_nom = f"{nom_fichier}_copie_{date_heure}{extension}"
        fichier_destination = os.path.join(dossier, nouveau_nom)
        shutil.copy(fichier_source, fichier_destination)
        print(f" Copie créée : {fichier_destination}")
    else:
        print(" Le fichier source n'existe pas.")

def compter_fichiers(dossier):
    """Compte le nombre de fichiers dans un dossier avec gestion des permissions."""
    if os.path.exists(dossier) and os.path.isdir(dossier):
        try:
            fichiers = [f for f in os.listdir(dossier) if os.path.isfile(os.path.join(dossier, f))]
            print(f"\n Nombre de fichiers dans '{dossier}': {len(fichiers)}")
        except PermissionError:
            print(" Erreur : Vous n'avez pas la permission d'accéder à ce dossier.")
    else:
        print(" Erreur : Le dossier spécifié n'existe pas ou n'est pas un dossier valide.")
