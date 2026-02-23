import requests
import json
import time
from kafka import KafkaProducer
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"

while True:
    try:
        res = requests.get(URL, timeout=5)
        data = res.json()

        btc = data.get("bitcoin", {}).get("usd")
        eth = data.get("ethereum", {}).get("usd")

        if btc is None or eth is None:
            print("API returned invalid data:", data)
            time.sleep(5)
            continue

        event = {
            "timestamp": datetime.utcnow().isoformat(),
            "btc": btc,
            "eth": eth
        }

        producer.send("raw_events", event)
        print("sent:", event)

    except Exception as e:
        print("error:", e)

    time.sleep(20)


