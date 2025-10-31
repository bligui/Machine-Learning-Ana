# random_forest_heart.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score, roc_curve
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

RANDOM_STATE = 42

def preprocess(df):
    # Preencher valores ausentes (mediana apenas para numéricos)
    df.fillna(df.median(numeric_only=True), inplace=True)

    # Encoding categórico conforme seu mapeamento
    df["Sex"] = df["Sex"].map({"M": 1, "F": 0})
    df["ChestPainType"] = df["ChestPainType"].map({"TA": 0, "ATA": 1, "NAP": 2, "ASY": 3})
    df["RestingECG"] = df["RestingECG"].map({"Normal": 0, "ST": 1, "LVH": 2})
    df["ExerciseAngina"] = df["ExerciseAngina"].map({"Y": 1, "N": 0})
    df["ST_Slope"] = df["ST_Slope"].map({"Up": 0, "Flat": 1, "Down": 2})

    return df

def load_and_prepare(url):
    df = pd.read_csv(url)
    df = preprocess(df)
    # drop duplicatas se houver (você mencionou que já foram removidas, mas por segurança)
    df = df.drop_duplicates().reset_index(drop=True)
    return df

def train_evaluate(df, target_col="HeartDisease", use_scaler=None):
    # Separar X e y
    X = df.drop(columns=[target_col])
    y = df[target_col]

    # Registrar colunas numéricas (para scaler)
    numeric_cols = X.select_dtypes(include=[np.number]).columns.tolist()

    # Aplicar scaler opcional
    if use_scaler == "minmax":
        scaler = MinMaxScaler()
        X[numeric_cols] = scaler.fit_transform(X[numeric_cols])
    elif use_scaler == "standard":
        scaler = StandardScaler()
        X[numeric_cols] = scaler.fit_transform(X[numeric_cols])
    # caso use_scaler is None, mantém variáveis como estão (RandomForest não precisa de scale)

    # Split estratificado
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=RANDOM_STATE, stratify=y
    )

    # Instanciar modelo (hiperparâmetros iniciais razoáveis)
    rf = RandomForestClassifier(
        n_estimators=200,
        max_depth=None,
        max_features="sqrt",
        class_weight="balanced",  # útil caso haja desbalanceamento
        random_state=RANDOM_STATE,
        n_jobs=-1
    )

    rf.fit(X_train, y_train)

    # Previsões
    y_pred = rf.predict(X_test)
    y_proba = rf.predict_proba(X_test)[:, 1] if hasattr(rf, "predict_proba") else None

    # Métricas
    acc = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, digits=4)
    cm = confusion_matrix(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_proba) if y_proba is not None else None

    print("=== Resultados ===")
    print(f"Acurácia: {acc:.4f}")
    if roc_auc is not None:
        print(f"ROC AUC: {roc_auc:.4f}")
    print("\nRelatório de Classificação:\n", report)
    print("\nMatriz de Confusão:\n", cm)

    # Validação cruzada (estratificada) - AUC ou Accuracy
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)
    cv_acc = cross_val_score(rf, X, y, cv=skf, scoring="accuracy", n_jobs=-1)
    cv_auc = cross_val_score(rf, X, y, cv=skf, scoring="roc_auc", n_jobs=-1)
    print(f"\nCV Accuracy (5-fold): {cv_acc.mean():.4f} ± {cv_acc.std():.4f}")
    print(f"CV ROC AUC (5-fold): {cv_auc.mean():.4f} ± {cv_auc.std():.4f}")

    # Importâncias de características (ordenadas)
    feat_imp = pd.DataFrame({
        "feature": X.columns,
        "importance": rf.feature_importances_
    }).sort_values("importance", ascending=False).reset_index(drop=True)
    print("\nFeature importances (top 10):\n", feat_imp.head(10).to_string(index=False))

    # Plot ROC curve se available
    if y_proba is not None:
        fpr, tpr, _ = roc_curve(y_test, y_proba)
        plt.figure()
        plt.plot(fpr, tpr, label=f"ROC curve (AUC = {roc_auc:.3f})")
        plt.plot([0, 1], [0, 1], linestyle="--")
        plt.xlabel("False Positive Rate")
        plt.ylabel("True Positive Rate")
        plt.title("ROC Curve")
        plt.legend(loc="lower right")
        plt.show()

    # Plot feature importances
    plt.figure(figsize=(8, 6))
    sns.barplot(data=feat_imp.head(20), x="importance", y="feature")
    plt.title("Top 20 Feature Importances")
    plt.tight_layout()
    plt.show()

    return rf, feat_imp, (X_train, X_test, y_train, y_test)

def grid_search_rf(X, y):
    # Exemplo de busca simples de hiperparâmetros
    param_grid = {
        "n_estimators": [100, 200, 400],
        "max_depth": [None, 6, 10],
        "max_features": ["sqrt", 0.3, 0.5]
    }
    rf = RandomForestClassifier(class_weight="balanced", random_state=RANDOM_STATE, n_jobs=-1)
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)
    grid = GridSearchCV(rf, param_grid, cv=skf, scoring="roc_auc", n_jobs=-1, verbose=1)
    grid.fit(X, y)
    print("Melhores parâmetros:", grid.best_params_)
    print("Melhor score (ROC AUC):", grid.best_score_)
    return grid

if __name__ == "__main__":
    URL = "https://raw.githubusercontent.com/bligui/Machine-Learning-Ana/refs/heads/main/dados/heart.csv"
    df = load_and_prepare(URL)
    print("Dataset shape:", df.shape)
    print("Target distribution:\n", df["HeartDisease"].value_counts(normalize=True))

    # Treinar/evaluar sem escalonamento (recomendado para RandomForest)
    rf_model, feat_imp, splits = train_evaluate(df, target_col="HeartDisease", use_scaler=None)

    # Se quiser, realizar Grid Search (pode demorar dependendo do tamanho do grid)
    # Comentado por padrão; descomente para rodar.
    # X_all = df.drop(columns=["HeartDisease"])
    # y_all = df["HeartDisease"]
    # grid = grid_search_rf(X_all, y_all)
