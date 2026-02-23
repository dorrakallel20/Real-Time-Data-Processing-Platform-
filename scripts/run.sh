#!/bin/bash

set -e

echo "🚀 Starting infrastructure..."

# Start Docker services (Kafka, Zookeeper, etc.)
docker compose up -d

echo "⏳ Waiting for services to initialize..."
sleep 10


echo "📡 Starting Kafka Producer..."
python src/api_producer.py &


echo "⚡ Starting Spark Streaming..."
PYSPARK_SUBMIT_ARGS="--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1 pyspark-shell" \
python streaming_app.py &


echo "📊 Launching Dashboard..."
streamlit run src/dashboard.py


echo "✅ System running successfully!"