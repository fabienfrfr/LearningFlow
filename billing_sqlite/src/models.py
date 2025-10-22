
# Modèles pour les tables de la base de données
# Exemple : classe Client, Projet, etc.
class Client:
    def __init__(self, id, nom, adresse, contact):
        self.id = id
        self.nom = nom
        self.adresse = adresse
        self.contact = contact

class Projet:
    def __init__(self, id, nom, id_client, budget, date_debut, date_fin):
        self.id = id
        self.nom = nom
        self.id_client = id_client
        self.budget = budget
        self.date_debut = date_debut
        self.date_fin = date_fin
