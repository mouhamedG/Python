#Question1
"""import requests


def requete_api(url, methode='GET', donnees=None):

    try:
        if methode.upper() == 'GET':
            response = requests.get(url)
        elif methode.upper() == 'POST':
            response = requests.post(url, json=donnees)
        else:
            raise ValueError("Méthode non supportée. Utilisez 'GET' ou 'POST'.")

        if 400 <= response.status_code < 500:
            raise Exception(f"Erreur {response.status_code} : Requête incorrecte.")

        return response.json()

    except requests.RequestException as e:
        print(f"Erreur de connexion : {e}")
        return {}


# Exemple d'utilisation avec l'API Dictionary
if __name__ == "__main__":
    mot = input("Entrez un mot : ")
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{mot}"
    resultat = requete_api(url)
    print(resultat)"""
#************************************************************************************************#
#Question2
"""import os
from pathlib import Path
import pandas as pd  # 📌 Nécessaire pour travailler avec Excel

# Définition des chemins des fichiers
dossier_csv = Path(r"C:\Users\mouha\csv_files")
fichier_source = dossier_csv / "csv.xlsx"
fichier_destination = dossier_csv / "csv-Copie.xlsx"

def modifier_excel(fichier_source, fichier_destination):
    try:
        # Vérifier si le fichier source existe
        if not fichier_source.exists():
            print(f"❌ Le fichier {fichier_source} n'existe pas.")
            return

        # Lire le fichier Excel
        df = pd.read_excel(fichier_source)

        # Ajouter une colonne "Modifié" avec la valeur "Oui"
        df["Modifié"] = "Oui"

        # Enregistrer les modifications dans un nouveau fichier
        df.to_excel(fichier_destination, index=False)

        print(f"✅ Fichier modifié enregistré sous : {fichier_destination}")

    except Exception as e:
        print(f"❌ Une erreur est survenue : {e}")

# Exécuter la fonction
modifier_excel(fichier_source, fichier_destination)"""

#***********************************************************************************************#
#Questiin3
"""import pandas as pd
import os
from pathlib import Path


def modifier_excel(fichier_source, fichier_destination):
    try:
        # Vérifier si le fichier source existe
        fichier_source = Path(fichier_source)
        fichier_destination = Path(fichier_destination)

        if not fichier_source.exists():
            print(f"❌ Le fichier {fichier_source} n'existe pas.")
            return

        # Lire le fichier Excel
        df = pd.read_excel(fichier_source)

        # Modifier les données (ajouter une colonne "Modifié")
        df["Modifié"] = "Oui"

        # Sauvegarder dans un nouveau fichier Excel
        df.to_excel(fichier_destination, index=False)

        print(f"✅ Fichier modifié enregistré sous : {fichier_destination}")
    except Exception as e:
        print(f"❌ Une erreur est survenue : {e}")


# Exécuter la fonction
if __name__ == "__main__":
    fichier_source = r"C:\Users\mouha\csv_files\csv.xlsx"
    fichier_destination = r"C:\Users\mouha\csv_files\csv_modifie.xlsx"
    modifier_excel(fichier_source, fichier_destination)"""

#**********************************************************************************************#
#Question4

"""import pandas as pd
import os


def modifier_excel(fichier_source, fichier_destination):
    try:
        # Vérifier si le fichier source existe
        if not os.path.isfile(fichier_source):
            raise FileNotFoundError(f"❌ Le fichier {fichier_source} n'existe pas.")

        # Lire le fichier Excel
        df = pd.read_excel(fichier_source, engine='openpyxl')

        # Vérifier s'il y a des données
        if df.empty:
            raise ValueError("❌ Le fichier est vide.")

        # Ajouter une colonne "Somme" (si applicable)
        df["Somme"] = df.apply(lambda row: sum(pd.to_numeric(row, errors='coerce').fillna(0)), axis=1)

        # Enregistrer le fichier modifié
        df.to_excel(fichier_destination, index=False, engine='openpyxl')

        print(f"✅ Fichier modifié enregistré sous : {fichier_destination}")

    except FileNotFoundError as e:
        print(f"❌ Erreur : {e}")
    except Exception as e:
        print(f"❌ Une erreur est survenue : {e}")


# 📌 Exemple d'utilisation
if __name__ == "__main__":
    fichier_source = r"C:\Users\mouha\csv_files\csv.xlsx"
    fichier_destination = r"C:\Users\mouha\csv_files\csv_modifie.xlsx"

    modifier_excel(fichier_source, fichier_destination)"""

