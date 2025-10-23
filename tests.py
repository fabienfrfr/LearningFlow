import os
from pathlib import Path


def create_project_structure():
    # Créer les dossiers
    Path("facturation_hybride/src").mkdir(parents=True, exist_ok=True)
    Path("facturation_hybride/tests").mkdir(parents=True, exist_ok=True)
    Path("facturation_hybride/docs").mkdir(parents=True, exist_ok=True)
    Path("facturation_hybride/data").mkdir(parents=True, exist_ok=True)

    # Fichiers src/
    with open("facturation_hybride/src/__init__.py", "w") as f:
        f.write("# Package src\n")

    with open("facturation_hybride/src/models.py", "w") as f:
        f.write(
            """
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
"""
        )

    with open("facturation_hybride/src/sqlite_manager.py", "w") as f:
        f.write(
            '''
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "facturation.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            adresse TEXT,
            contact TEXT
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Projets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            id_client INTEGER,
            budget REAL,
            date_debut TEXT,
            date_fin TEXT,
            FOREIGN KEY (id_client) REFERENCES Clients(id)
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS UnitesDOeuvre (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_projet INTEGER,
            description TEXT,
            quantite REAL,
            prix_unitaire REAL,
            FOREIGN KEY (id_projet) REFERENCES Projets(id)
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Factures (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_projet INTEGER,
            date TEXT,
            montant_total REAL,
            statut TEXT,
            FOREIGN KEY (id_projet) REFERENCES Projets(id)
        )
        """)
        conn.commit()

def get_db_connection():
    return sqlite3.connect(DB_PATH)
'''
        )

    with open("facturation_hybride/src/arango_manager.py", "w") as f:
        f.write(
            """
from arango import ArangoClient
from arango.graph import Graph, EdgeDefinition

ARANGO_URL = "http://localhost:8529"
ARANGO_USER = "root"
ARANGO_PASSWORD = ""
ARANGO_DB = "facturation_graphe"

client = ArangoClient(hosts=ARANGO_URL)
db = client.db(ARANGO_DB, username=ARANGO_USER, password=ARANGO_PASSWORD)

def init_arango_graph():
    if not db.has_collection("Clients"):
        db.create_collection("Clients")
    if not db.has_collection("Projets"):
        db.create_collection("Projets")
    if not db.has_collection("UnitesDOeuvre"):
        db.create_collection("UnitesDOeuvre")
    if not db.has_collection("Factures"):
        db.create_collection("Factures")
    if not db.has_collection("BonsDeLivraison"):
        db.create_collection("BonsDeLivraison")

    if not db.has_graph("FacturationGraph"):
        graph = db.create_graph("FacturationGraph")
        graph.add_edge_definition(
            EdgeDefinition(
                "A_PAYE",
                from_collections=["Clients"],
                to_collections=["Projets"]
            )
        )
        graph.add_edge_definition(
            EdgeDefinition(
                "CONTIENT",
                from_collections=["Projets"],
                to_collections=["UnitesDOeuvre"]
            )
        )
        graph.add_edge_definition(
            EdgeDefinition(
                "FACTURE",
                from_collections=["Projets"],
                to_collections=["Factures"]
            )
        )
"""
        )

    with open("facturation_hybride/src/sync.py", "w") as f:
        f.write(
            """
from sqlite_manager import get_db_connection
from arango_manager import db

def sync_clients():
    with get_db_connection() as sqlite_conn:
        cursor = sqlite_conn.cursor()
        cursor.execute("SELECT * FROM Clients")
        clients = cursor.fetchall()
        for client in clients:
            doc = {
                "_key": str(client[0]),
                "nom": client[1],
                "adresse": client[2],
                "contact": client[3]
            }
            if not db.collection("Clients").has(doc["_key"]):
                db.collection("Clients").insert(doc)

def sync_projets():
    with get_db_connection() as sqlite_conn:
        cursor = sqlite_conn.cursor()
        cursor.execute("SELECT * FROM Projets")
        projets = cursor.fetchall()
        for projet in projets:
            doc = {
                "_key": str(projet[0]),
                "nom": projet[1],
                "id_client": projet[2],
                "budget": projet[3],
                "date_debut": projet[4],
                "date_fin": projet[5]
            }
            if not db.collection("Projets").has(doc["_key"]):
                db.collection("Projets").insert(doc)
                db.graph("FacturationGraph").insert_edge(
                    "A_PAYE",
                    {"_from": f"Clients/{projet[2]}", "_to": f"Projets/{projet[0]}"}
                )
"""
        )

    with open("facturation_hybride/src/cli.py", "w") as f:
        f.write(
            """
import argparse
from sqlite_manager import init_db
from arango_manager import init_arango_graph
from sync import sync_clients, sync_projets

def main():
    parser = argparse.ArgumentParser(description="Gestion de facturation hybride")
    parser.add_argument("--init-sqlite", action="store_true", help="Initialiser SQLite")
    parser.add_argument("--init-arango", action="store_true", help="Initialiser ArangoDB")
    parser.add_argument("--sync", action="store_true", help="Synchroniser SQLite → ArangoDB")
    args = parser.parse_args()

    if args.init_sqlite:
        init_db()
        print("SQLite initialisé.")
    elif args.init_arango:
        init_arango_graph()
        print("ArangoDB initialisé.")
    elif args.sync:
        sync_clients()
        sync_projets()
        print("Synchronisation terminée.")
    else:
        print("Utilisation : python main.py --init-sqlite/--init-arango/--sync")

if __name__ == "__main__":
    main()
"""
        )

    # Fichiers tests/
    with open("facturation_hybride/tests/__init__.py", "w") as f:
        f.write("# Package tests\n")

    # Fichiers docs/
    with open("facturation_hybride/docs/README.md", "w") as f:
        f.write(
            """
# Gestion de Facturation Hybride (SQLite + ArangoDB)

## Installation
1. Installer ArangoDB : [https://www.arangodb.com/download/](https://www.arangodb.com/download/)
2. Installer les dépendances : `pip install -r requirements.txt`
3. Initialiser les bases :
   - `python main.py --init-sqlite`
   - `python main.py --init-arango`
4. Synchroniser : `python main.py --sync`

## Utilisation
- Les données sont gérées au quotidien dans SQLite.
- Les analyses complexes (graphe) se font via ArangoDB/AQL.
"""
        )

    # Fichiers racine
    with open("facturation_hybride/requirements.txt", "w") as f:
        f.write(
            """
python-arango>=7.0
reportlab
"""
        )

    with open("facturation_hybride/main.py", "w") as f:
        f.write(
            """
from src.cli import main

if __name__ == "__main__":
    main()
"""
        )


if __name__ == "__main__":
    create_project_structure()
    print("Projet hybride généré dans le dossier 'facturation_hybride' !")
