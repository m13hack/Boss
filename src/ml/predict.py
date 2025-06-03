import pickle

def load_model(path="models/rf_model.pkl"):
    with open(path, "rb") as f:
        return pickle.load(f)

def predict(model, features):
    import pandas as pd
    df = pd.DataFrame([features])
    return model.predict(df)[0]
