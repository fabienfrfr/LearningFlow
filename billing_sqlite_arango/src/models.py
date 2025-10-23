
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

class UniteDOeuvre:
    def __init__(self, id, id_projet, description, quantite, prix_unitaire):
        self.id = id
        self.id_projet = id_projet
        self.description = description
        self.quantite = quantite
        self.prix_unitaire = prix_unitaire

class Facture:
    def __init__(self, id, id_projet, date, montant_total, statut):
        self.id = id
        self.id_projet = id_projet
        self.date = date
        self.montant_total = montant_total
        self.statut = statut
