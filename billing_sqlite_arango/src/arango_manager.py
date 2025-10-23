
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
