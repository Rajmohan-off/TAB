import os, pickle, pandas as pd
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'isolation_model.pkl')

def load_model():
    with open(MODEL_PATH, 'rb') as f:
        data = pickle.load(f)
    return data['model'], data['features']

def prepare_features(reading):
    vp, vs, ip, isec = reading.values()
    vdiff = vp - vs
    idiff = ip - isec
    return pd.DataFrame([{'voltage_primary': vp, 'voltage_secondary': vs, 'current_primary': ip, 'current_secondary': isec, 'v_diff': vdiff, 'i_diff': idiff}])

def is_anomaly(reading):
    model, features = load_model()
    df = prepare_features(reading)[features].fillna(0)
    score = model.decision_function(df)[0]
    pred = model.predict(df)[0]
    return {'is_anomaly': pred == -1, 'score': float(score)}
