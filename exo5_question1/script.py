# script.py
from exo5_question1 import exercice1

# Demander une adresse IP
adresse = input("Entrez une adresse IP (IPv4 ou IPv6) : ")

# Vérification du type d'IP
if exercice1.est_ipv4_valide(adresse):
    print("Adresse IPv4 valide.")
elif exercice1.ipv6_valide(adresse):
    print("Adresse IPv6 valide.")
else:
    print("Adresse IP invalide.")

# Demander une liste d'adresses IP
adresses = input("Entrez une liste d'adresses IP séparées par des espaces : ").split()

# Vérifier et afficher les résultats pour la liste d'adresses
print("\nVérification de la liste d'adresses IP :")
for adresse in adresses:
    exercice1.detecter_ip(adresse)

# Exemple avec un dictionnaire d'adresses IP
adresses_dict = {
    "Serveur1": "192.168.1.1",
    "Serveur2": "2001:db8::ff00:42:8329",
    "Machine1": "256.256.256.256"
}

print("\nVérification des adresses IP dans un dictionnaire :")
for host, adresse in adresses_dict.items():
    print(f"{host} ({adresse}) : ", end="")
    exercice1.detecter_ip(adresse)
