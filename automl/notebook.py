import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return


@app.cell
def _():
    from autogluon.timeseries import TimeSeriesDataFrame, TimeSeriesPredictor
    import pandas as pd

    # 1. Chargement d'un dataset standard (M4 Daily)
    data = TimeSeriesDataFrame.from_path(
        "https://autogluon.s3.amazonaws.com/datasets/timeseries/m4_daily_subset/train.csv"
    )

    # 2. Entraînement (on exclut le Deep Learning pour rester léger)
    # On règle prediction_length=1 pour avoir une base de comparaison immédiate
    predictor = TimeSeriesPredictor(target="target", prediction_length=1, freq="D")

    predictor.fit(
        data,
        presets="medium_quality", # Équilibre performance/poids
        excluded_model_types=["DeepAR", "TemporalFusionTransformer"], # Pas de DL = pas de Ray
        num_val_windows=1
    )

    # 3. Prédiction (génère la valeur "normale" attendue pour le pas de temps suivant)
    predictions = predictor.predict(data)

    # 4. Calcul de l'anomalie : l'écart entre le réel et la prévision
    # On prend la dernière valeur réelle connue et on la compare à la prédiction
    last_known_values = data.groupby("item_id").tail(1)
    # Calcul du résidu (écart absolu)
    error = abs(last_known_values["target"] - predictions["mean"])

    # 5. Détection des anomalies (ex: top 5% des écarts)
    threshold = error.quantile(0.95)
    anomalies = error[error > threshold]

    print("Anomalies détectées sur les items :")
    print(anomalies)






    from autogluon.tabular import TabularPredictor

    # URL vers un dataset standard (Adult Income)
    train_url = "https://autogluon.s3.amazonaws.com/datasets/Inc/train.csv"
    test_url = "https://autogluon.s3.amazonaws.com/datasets/Inc/test.csv"

    # 1. Entraînement (AutoGluon télécharge, nettoie et stacke les modèles)
    # 'label' est le nom de la colonne cible dans ce dataset
    predictor = TabularPredictor(label="class").fit(
        train_url, 
        excluded_model_types=['NN_TORCH', 'FASTAI'], # On vire le deep learning
        presets="good_quality", 
        num_stack_levels=0,
        auto_stack=False
    )

    # 2. Prédiction
    predictions = predictor.predict(test_url)

    # Affichage pour vérification
    print(predictions.head())
    return


if __name__ == "__main__":
    app.run()
