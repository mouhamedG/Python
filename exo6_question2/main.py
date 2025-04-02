from process_info import ProcessInfo

if __name__ == "__main__":
    # Créer une instance de la classe ProcessInfo
    info_processus = ProcessInfo()

    # Obtenir les informations de tous les processus
    info_processus.obtenir_informations_processus()

    # Exporter les données dans un fichier JSON
    info_processus.exporter_donnees('processus_info.json')
