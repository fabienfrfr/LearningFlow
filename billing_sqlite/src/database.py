
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "facturation.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        # Création des tables
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
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS BonsDeLivraison (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_projet INTEGER,
            date TEXT,
            details TEXT,
            FOREIGN KEY (id_projet) REFERENCES Projets(id)
        )
        """)
        conn.commit()

def get_db_connection():
    return sqlite3.connect(DB_PATH)
