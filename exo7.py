#Question1
"""import pandas as pd

def charger_fichier(chemin_fichier):

    try:
        if chemin_fichier.endswith(".csv"):
            return pd.read_csv(chemin_fichier)
        elif chemin_fichier.endswith(".json"):
            return pd.read_json(chemin_fichier)
        elif chemin_fichier.endswith(".html"):
            return pd.read_html(chemin_fichier)[0]  # Retourne le premier tableau trouvé
        elif chemin_fichier.endswith(".xlsx"):
            return pd.read_excel(chemin_fichier)
        else:
            raise ValueError("Format de fichier non pris en charge.")
    except Exception as e:
        print(f"Erreur lors du chargement du fichier : {e}")
        return None

# Exemple d'utilisation
if __name__ == "__main__":
    fichier = input("Entrez le chemin du fichier à charger : ")
    df = charger_fichier(fichier)
    if df is not None:
        print("Aperçu des données :")
        print(df.head())"""
#**********************************************************************************#
#Question2
import pandas as pd

# Fonction pour filtrer les lignes où 'boolean' est 'Yes'
def filtrer_par_boolean(df):
    # On filtre les lignes où la colonne 'boolean' est égale à 'Yes'
    return df[df['boolean'] == 'Yes']

# Fonction pour filtrer les lignes où 'url' contient 'reddit'
def filtrer_par_url(df):
    # On filtre les lignes où la colonne 'url' contient 'reddit'
    return df[df['url'].str.contains('reddit', case=False, na=False)]

# Fonction pour calculer le pourcentage de lignes respectant au moins une des conditions
def calculer_pourcentage(df, result_boolean, result_url):
    # On combine les résultats des deux filtres sans doublons
    result_combined = pd.concat([result_boolean, result_url]).drop_duplicates()
    # On calcule le pourcentage de lignes respectant au moins une des conditions
    pourcentage = (len(result_combined) / len(df)) * 100
    return pourcentage

# Fonction principale
def main():
    # Demander à l'utilisateur de donner le chemin du fichier CSV
    chemin_fichier = input("Indiquez le chemin du fichier CSV: ")

    # Lire le fichier CSV avec pandas
    df = pd.read_csv(chemin_fichier)

    # Filtrer les lignes où 'boolean' est 'Yes'
    result_boolean = filtrer_par_boolean(df)
    print("\nLignes où 'boolean' est 'Yes':")
    print(result_boolean)

    # Filtrer les lignes où 'url' contient 'reddit'
    result_url = filtrer_par_url(df)
    print("\nLignes où 'url' contient 'reddit':")
    print(result_url)

    # Calculer et afficher le pourcentage des lignes respectant au moins une condition
    pourcentage = calculer_pourcentage(df, result_boolean, result_url)
    print(f"\nPourcentage de lignes respectant au moins une des deux conditions : {pourcentage:.2f}%")

if __name__ == '__main__':
    main()
#***********************************************************************************************************#
#Question3
"""import pandas as pd

# Fonction pour filtrer les lignes où 'boolean' est 'Yes'
def filtrer_par_boolean(df):
    return df[df['boolean'] == 'Yes']

# Fonction pour filtrer les lignes où 'url' contient 'reddit'
def filtrer_par_url(df):
    return df[df['url'].str.contains('reddit', case=False, na=False)]

# Fonction principale pour créer les deux fichiers CSV filtrés
def main():
    # Demander à l'utilisateur de donner le chemin du fichier CSV
    chemin_fichier = input("Indiquez le chemin du fichier CSV: ")

    # Lire le fichier CSV avec pandas
    df = pd.read_csv(chemin_fichier)

    # Filtrer les lignes où 'boolean' est 'Yes'
    result_boolean = filtrer_par_boolean(df)
    # Enregistrer ces lignes dans un nouveau fichier CSV
    result_boolean.to_csv('lignes_boolean_yes.csv', index=False)

    # Filtrer les lignes où 'url' contient 'reddit'
    result_url = filtrer_par_url(df)
    # Enregistrer ces lignes dans un autre fichier CSV
    result_url.to_csv('lignes_url_reddit.csv', index=False)

    print("Les fichiers filtrés ont été enregistrés : 'lignes_boolean_yes.csv' et 'lignes_url_reddit.csv'")

if __name__ == '__main__':
    main()
"""
