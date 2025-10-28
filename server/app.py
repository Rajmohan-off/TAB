from flask import Flask, request, jsonify
from datetime import datetime
from server.db import get_engine, init_db, get_session, SensorReading

app = Flask(__name__)
engine = get_engine()
init_db(engine)

@app.route('/ingest', methods=['POST'])
def ingest():
    data = request.get_json()
    session = get_session(engine)
    reading = SensorReading(device_id=data['device_id'], timestamp=datetime.utcnow(), voltage_primary=data['voltage_primary'], voltage_secondary=data['voltage_secondary'], current_primary=data['current_primary'], current_secondary=data['current_secondary'])
    session.add(reading)
    session.commit()
    session.close()
    return jsonify({'status':'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
