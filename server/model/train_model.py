import os, pickle, pandas as pd
from sklearn.ensemble import IsolationForest
from sqlalchemy import select
from server.db import SensorReading, get_engine, get_session

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'isolation_model.pkl')

def load_data_from_db(engine):
    session = get_session(engine)
    stmt = select(SensorReading)
    rows = session.execute(stmt).scalars().all()
    session.close()
    data = [{'voltage_primary': r.voltage_primary, 'voltage_secondary': r.voltage_secondary, 'current_primary': r.current_primary, 'current_secondary': r.current_secondary} for r in rows]
    return pd.DataFrame(data)

def train_and_save(engine, contamination=0.01):
    df = load_data_from_db(engine)
    if df.empty:
        print('No data in DB to train on.')
        return
    df['v_diff'] = df.voltage_primary - df.voltage_secondary
    df['i_diff'] = df.current_primary - df.current_secondary
    features = df[['voltage_primary','voltage_secondary','current_primary','current_secondary','v_diff','i_diff']].fillna(0)
    clf = IsolationForest(n_estimators=200, contamination=contamination, random_state=42)
    clf.fit(features)
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump({'model': clf, 'features': list(features.columns)}, f)
    print('Model saved')
