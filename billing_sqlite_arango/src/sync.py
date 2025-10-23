
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
