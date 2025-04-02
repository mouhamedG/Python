import platform
import psutil
import json

class SystemInfo:
    def __init__(self):
        # On initialise les informations système
        self.os = platform.system()  # Nom du système d'exploitation (ex: Windows, Linux)
        self.version = platform.version()  # Version du système d'exploitation
        self.ram_utilisee = self.obtenir_ram_utilisee()  # RAM utilisée en pourcentage

    def obtenir_ram_utilisee(self):
        """Retourne le pourcentage de RAM utilisée"""
        ram = psutil.virtual_memory()
        return ram.percent  # Retourne le pourcentage de RAM utilisée

    def exporter_donnees(self, nom_fichier):
        """Exporter les informations système dans un fichier JSON"""
        infos = {
            "OS": self.os,
            "Version": self.version,
            "RAM_utilisee": self.ram_utilisee
        }

        # Sauvegarder dans un fichier JSON
        with open(nom_fichier, 'w') as fichier_json:
            json.dump(infos, fichier_json, indent=4)

        print(f"Informations système sauvegardées dans {nom_fichier}")
