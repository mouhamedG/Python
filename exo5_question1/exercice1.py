# exercice.py
import ipaddress

# Fonction de validation de l'adresse IPv4
def est_ipv4_valide(ip):
    try:
        parties = ip.split(".")
        if len(parties) != 4:
            return False
        for part in parties:
            if not (0 <= int(part) <= 255):
                return False
        return True
    except:
        return False

# Fonction de validation de l'adresse IPv6
def ipv6_valide(ip):
    try:
        parties = ip.split(":")
        if len(parties) != 8:
            return False
        for part in parties:
            if len(part) == 0 or len(part) > 4:
                return False
            if not (0 <= int(part, 16) <= 0xFFFF):
                return False
        return True
    except:
        return False

# Fonction de détection automatique de l'adresse IP
def detecter_ip(adresse):
    try:
        ip = ipaddress.ip_address(adresse)
        print(f"{adresse} : Adresse IP valide de version {ip.version}.")
    except ValueError:
        print(f"{adresse} : Adresse IP invalide.")
