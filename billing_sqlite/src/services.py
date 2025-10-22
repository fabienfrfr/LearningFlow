
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from src.database import get_db_connection

def generate_invoice(invoice_id, output_path="facture.pdf"):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT c.nom, p.nom, SUM(u.quantite * u.prix_unitaire)
        FROM Factures f
        JOIN Projets p ON f.id_projet = p.id
        JOIN Clients c ON p.id_client = c.id
        JOIN UnitesDOeuvre u ON u.id_projet = p.id
        WHERE f.id = ?
        GROUP BY c.nom, p.nom
        """, (invoice_id,))
        client, projet, montant = cursor.fetchone()

    # Générer un PDF
    c = canvas.Canvas(output_path, pagesize=letter)
    c.drawString(100, 750, f"Facture pour {client} - Projet: {projet}")
    c.drawString(100, 730, f"Montant total : {montant} €")
    c.save()
    print(f"Facture générée : {output_path}")
