import mlflow
import polars as pl
from sklearn.metrics import classification_report
from load_data import load_data_from_timescaledb

def monitor_model(run_id):
    # Paramètres de connexion à TimescaleDB
    conn_params = {
        'dbname': 'your_dbname',
        'user': 'your_user',
        'password': 'your_password',
        'host': 'your_host',
        'port': 'your_port'
    }
    query = "SELECT * FROM your_timeseries_table WHERE time >= '2023-02-01' AND time < '2023-03-01';"

    # Charger les nouvelles données pour le monitoring depuis TimescaleDB
    data = load_data_from_timescaledb(query, conn_params)

    X_new = data.drop('label')
    y_new = data['label']

    # Charger le modèle depuis MLflow
    model_uri = f"runs:/{run_id}/isolation_forest_model"
    model = mlflow.sklearn.load_model(model_uri)

    # Prédire les anomalies
    y_pred = model.predict(X_new.to_numpy())
    y_pred = [1 if x == -1 else 0 for x in y_pred]

    # Évaluer le modèle
    report = classification_report(y_new.to_numpy(), y_pred, output_dict=True)
    print(report)

if __name__ == "__main__":
    run_id = "YOUR_RUN_ID"  # Remplace par l'ID de ta run MLflow
    monitor_model(run_id)