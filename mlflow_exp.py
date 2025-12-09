import mlflow
print("MLflow imported")

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor

print("Scikit-learn imported")

mlflow.set_tracking_uri("http://127.0.0.1:5001")
mlflow.autolog()

print("Autolog enabled")

db = load_diabetes()
print("Dataset loaded")

X_train, X_test, y_train, y_test = train_test_split(db.data, db.target)
print("Data split done")

rf = RandomForestRegressor(
    n_estimators=20,  # beaucoup moins d'arbres
    max_depth=4,      # arbres moins profonds
    max_features="sqrt",  # sélection plus rapide
    n_jobs=-1         # multi-core activé
)

print("Model created")

rf.fit(X_train, y_train)
print("Model trained")

print("🎉 Run MLflow terminé")
