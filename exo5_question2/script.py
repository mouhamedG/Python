# Script script.py
import os
import sys
from exercice4 import lister_dossier, copier_fichier, compter_fichiers

if __name__ == "__main__":
    if len(sys.argv) > 1:
        dossier_utilise = sys.argv[1]
    else:
        dossier_utilise = os.getcwd()  # Dossier actuel par défaut

    lister_dossier(dossier_utilise)

    fichier_test = os.path.join(dossier_utilise, "test.txt")  # Exemple de fichier à copier
    copier_fichier(fichier_test)

    compter_fichiers(dossier_utilise)
