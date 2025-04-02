# Question1
"""adresse_ipv4 = input("Entrez une adresse IPv4 : ")
print("Vous avez entré :", adresse_ipv4)"""
#*******************************************************************************#

# Question2
"""def est_ipv4_valide(ip):
    try:
        # Séparer l'adresse en 4 parties et convertir en nombres
        parties = ip.split(".")
        if len(parties) != 4:
            return False
        for part in parties:
            if not (0 <= int(part) <= 255):
                return False
        return True
    except:
        return False

# Demander une adresse IPv4
adresse = input("Entrez une adresse IPv4 : ")

# Vérifier et afficher le résultat
if est_ipv4_valide(adresse):
    print("Adresse IPv4 valide.")
else:
    print("Adresse IPv4 invalide.")"""
#*******************************************************************************#

# Question3
"""def ipv6_valide(ip):
    try:
        # Séparer l'adresse en 8 parties
        parties = ip.split(":")
        if len(parties) != 8:
            return False
        for part in parties:
            # Chaque partie doit avoir entre 1 et 4 caractères
            if len(part) == 0 or len(part) > 4:
                return False
            # Essayer de convertir la partie en nombre hexadécimal (base 16)
            if not (0 <= int(part, 16) <= 0xFFFF):
                return False
        return True
    except:
        return False

# Demander une adresse IPv6
adresse = input("Entrez une adresse IPv6 : ")

# Vérifier et afficher le résultat
if ipv6_valide(adresse):
    print("Adresse IPv6 valide.")
else:
    print("Adresse IPv6 invalide.")"""
#*******************************************************************************#
# Question4

"""import ipaddress

def detecter_ip(adresse):
    try:
        ip = ipaddress.ip_address(adresse)
        print(f"Adresse IP valide de version {ip.version}.")
    except ValueError:
        print("Adresse IP invalide.")

# Demander une adresse à l'utilisateur
adresse = input("Entrez une adresse IP : ")
detecter_ip(adresse)"""
#*******************************************************************************#
# Question5
"""import ipaddress

def detecter_ip(adresses):
    for adresse in adresses:
        try:
            ip = ipaddress.ip_address(adresse)
            print(f"{adresse} : Adresse IP valide de version {ip.version}.")
        except ValueError:
            print(f"{adresse} : Adresse IP invalide.")

# Demander une liste d'adresses à l'utilisateur
adresses = input("Entrez une liste d'adresses IP séparées par des espaces : ").split()
detecter_ip(adresses)"""

#*******************************************************************************#
# Question6
"""import ipaddress

def detecter_ip(adresses):
    for host, adresse in adresses.items():
        try:
            ip = ipaddress.ip_address(adresse)
            print(f"{host} ({adresse}) : Adresse IP valide de version {ip.version}.")
        except ValueError:
            print(f"{host} ({adresse}) : Adresse IP invalide.")

# Exemple de dictionnaire d'adresses IP
adresses = {
    "Serveur1": "192.168.1.1",
    "Serveur2": "2001:db8::ff00:42:8329",
    "Machine1": "256.256.256.256"
}

detecter_ip(adresses)"""


