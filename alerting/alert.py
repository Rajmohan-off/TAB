def send_alert(device_id, reading, pred):
    print(f'ALERT: {device_id} anomaly detected -> {pred}')