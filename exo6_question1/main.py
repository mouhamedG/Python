from system_info import SystemInfo

if __name__ == "__main__":
    # Créer une instance de la classe SystemInfo
    info_systeme = SystemInfo()

    # Exporter les données dans un fichier JSON
    info_systeme.exporter_donnees('informations_systeme.json')
