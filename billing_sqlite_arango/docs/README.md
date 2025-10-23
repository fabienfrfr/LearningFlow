
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
