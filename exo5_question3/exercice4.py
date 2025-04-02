import os
import shutil
import datetime

class GestionDossier:
    def __init__(self, chemin_dossier):
        self.chemin_dossier = chemin_dossier

    def lister_dossier(self):
        """Lister les fichiers présents dans le dossier"""
        if os.path.exists(self.chemin_dossier):
            fichiers = [f for f in os.listdir(self.chemin_dossier) if os.path.isfile(os.path.join(self.chemin_dossier, f))]
            print(f"📂 Contenu du dossier '{self.chemin_dossier}':")
            for fichier in fichiers:
                print(f" - {fichier}")
        else:
            print("❌ Le dossier n'existe pas.")

    def copier_fichier(self, fichier_source):
        """Créer une copie d'un fichier avec la date et l'heure dans le nom"""
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
            print(f" Copie créée : {fichier_destination}")
        else:
            print(" Le fichier source n'existe pas.")

    def compter_fichiers(self):
        """Compter le nombre de fichiers dans le dossier"""
        if os.path.exists(self.chemin_dossier):
            fichiers = [f for f in os.listdir(self.chemin_dossier) if os.path.isfile(os.path.join(self.chemin_dossier, f))]
            print(f" Nombre de fichiers dans '{self.chemin_dossier}': {len(fichiers)}")
        else:
            print(" Le dossier spécifié n'existe pas.")

# Exemple d'utilisation
if __name__ == "__main__":
    dossier_travail = os.path.expanduser("~")  # Chemin générique vers le dossier utilisateur
    gestionnaire = GestionDossier(dossier_travail)

    # Lister les fichiers du dossier
    gestionnaire.lister_dossier()

    # Copier un fichier avec la date et l'heure dans le nom
    chemin_fichier = os.path.join(dossier_travail, "toto.txt")  # Exemple de fichier
    gestionnaire.copier_fichier(chemin_fichier)

    # Compter le nombre de fichiers dans le dossier
    gestionnaire.compter_fichiers()
