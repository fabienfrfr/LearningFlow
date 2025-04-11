import mlflow
import mlflow.sklearn
import polars as pl
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from load_data import load_data_from_timescaledb

def train_model():
    # Paramètres de connexion à TimescaleDB
    conn_params = {
        'dbname': 'your_dbname',
        'user': 'your_user',
        'password': 'your_password',
        'host': 'your_host',
        'port': 'your_port'
    }
    query = "SELECT * FROM your_timeseries_table;"

    # Charger les données depuis TimescaleDB
    data = load_data_from_timescaledb(query, conn_params)

    # Préparer les données
    X = data.drop('label')
    y = data['label']

    # Séparer les données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X.to_numpy(), y.to_numpy(), test_size=0.2, random_state=42)

    # Initialiser MLflow
    mlflow.start_run()

    # Entraîner le modèle Isolation Forest
    model = IsolationForest(contamination=0.01)  # Ajuste 'contamination' selon ton jeu de données
    model.fit(X_train)

    # Prédire les anomalies
    y_pred = model.predict(X_test)
    y_pred = [1 if x == -1 else 0 for x in y_pred]

    # Évaluer le modèle
    report = classification_report(y_test, y_pred, output_dict=True)

    # Loguer les métriques avec MLflow
    mlflow.log_metrics({
        'precision_anomaly': report['1']['precision'],
        'recall_anomaly': report['1']['recall'],
        'f1_score_anomaly': report['1']['f1-score']
    })

    # Loguer le modèle avec MLflow
    mlflow.sklearn.log_model(model, "isolation_forest_model")

    # Terminer la run MLflow
    mlflow.end_run()

if __name__ == "__main__":
    train_model()