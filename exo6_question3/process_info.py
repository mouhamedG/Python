import psutil
import json

class ProcessInfo:
    def __init__(self):
        self.processes = []

    def obtenir_informations_processus(self):
        """Récupère les informations de tous les processus en cours"""
        # Itere sur tous les processus
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'status']):
            try:
                # On récupère les informations du processus
                process_info = {
                    'pid': proc.info['pid'],
                    'name': proc.info['name'],
                    'cpu_percent': proc.info['cpu_percent'],
                    'memory_percent': proc.info['memory_percent'],
                    'status': proc.info['status'],
                }
                # Filtrer les processus consommant plus de 2% de la RAM
                if proc.info['memory_percent'] > 2:
                    self.processes.append(process_info)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                # Ignore les erreurs si un processus est terminé ou inaccessible
                pass

    def afficher_processus(self):
        """Affiche les processus consommant plus de 2% de RAM"""
        print(f"Processus consommant plus de 2% de la RAM :")
        for proc in self.processes:
            print(f"PID: {proc['pid']}, Nom: {proc['name']}, RAM utilisée: {proc['memory_percent']}%")

    def exporter_donnees(self, nom_fichier):
        """Exporter les informations des processus dans un fichier JSON"""
        with open(nom_fichier, 'w') as fichier_json:
            json.dump(self.processes, fichier_json, indent=4)
        print(f"Informations des processus sauvegardées dans {nom_fichier}")
