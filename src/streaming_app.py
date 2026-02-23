from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, window
from pyspark.sql.types import StructType, StructField, StringType, FloatType, TimestampType

spark = SparkSession.builder.appName("CryptoStreaming").getOrCreate()

# Read from Kafka
df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "raw_events") \
    .option("startingOffsets", "latest") \
    .load()

# Define schema
schema = StructType([
    StructField("timestamp", StringType(), True),
    StructField("btc", FloatType(), True),
    StructField("eth", FloatType(), True)
])

# Parse JSON
json_df = df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")

# Convert timestamp to TimestampType
json_df = json_df.withColumn("event_time", col("timestamp").cast(TimestampType()))

# Windowed aggregation (1-min sliding window, 5-min tumbling)
agg_df = json_df.groupBy(window(col("event_time"), "5 minutes", "1 minute")) \
    .avg("btc", "eth") \
    .orderBy("window")

# Output to console
query = agg_df.writeStream \
    .outputMode("complete") \
    .format("console") \
    .option("truncate", "false") \
    .start()

query.awaitTermination()
