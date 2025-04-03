#Question1
"""import subprocess


def lister_interfaces():
    # Commande pour Windows
    commande = "netsh interface show interface"

    # Exécuter la commande avec l'encodage CP850 et gestion des erreurs
    result = subprocess.run(commande, shell=True, capture_output=True, text=True, encoding="cp850", errors="ignore")

    # Vérifier si la commande a bien fonctionné
    if result.returncode != 0:
        print("Erreur lors de l'exécution de la commande.")
        return []

    # Extraire les noms des interfaces
    lignes = result.stdout.splitlines()
    interfaces = []

    for ligne in lignes:
        if "Connecté" in ligne or "Déconnecté" in ligne:  # Identifier les interfaces
            nom_interface = " ".join(ligne.split()[3:])  # Récupérer le nom de l'interface
            interfaces.append(nom_interface)

    return interfaces


# Exécuter la fonction et afficher les résultats
interfaces = lister_interfaces()
print("Interfaces réseau :", interfaces)"""
#************************************************************************************************#
#Question2
from fabric import Connection

# Informations de connexion à la machine distante
hote = "192.168.1.100"  # Remplace par l'IP de la machine distante
utilisateur = "user"    # Nom d'utilisateur sur la machine distante
mot_de_passe = "password"  # Mot de passe SSH

def lister_interfaces():
    # Connexion SSH à la machine distante
    with Connection(host=hote, user=utilisateur, connect_kwargs={"password": mot_de_passe}) as conn:
        # Exécuter la commande pour afficher les interfaces réseau (Linux)
        result = conn.run("ip link show", hide=True)

        # Extraire les noms des interfaces
        lignes = result.stdout.splitlines()
        interfaces = [ligne.split(":")[1].strip() for ligne in lignes if ":" in ligne]

        return interfaces

# Exécuter la fonction et afficher les résultats
interfaces = lister_interfaces()
print("Interfaces réseau (machine distante) :", interfaces)

