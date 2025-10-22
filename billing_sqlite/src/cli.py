
import argparse
from src.database import init_db, get_db_connection
from src.services import generate_invoice

def main():
    parser = argparse.ArgumentParser(description="Gestion de facturation")
    parser.add_argument("--init-db", action="store_true", help="Initialiser la base de données")
    parser.add_argument("--generate-invoice", type=int, help="Générer une facture (ID)")
    args = parser.parse_args()

    if args.init_db:
        init_db()
        print("Base de données initialisée.")
    elif args.generate_invoice:
        generate_invoice(args.generate_invoice)
    else:
        print("Utilisation : python main.py --init-db ou --generate-invoice ID")

if __name__ == "__main__":
    main()
