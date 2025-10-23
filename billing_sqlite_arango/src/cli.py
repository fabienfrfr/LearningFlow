
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
