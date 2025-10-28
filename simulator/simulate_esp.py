import requests, random, time
SERVER = 'http://127.0.0.1:5000/ingest'
while True:
    data = {'device_id':'transformer_001','voltage_primary':random.uniform(220,240),'voltage_secondary':random.uniform(2.1,2.3),'current_primary':random.uniform(3,10),'current_secondary':random.uniform(20,50)}
    requests.post(SERVER, json=data)
    print('Posted', data)
    time.sleep(2)
