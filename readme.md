# Real-Time Data Processing Platform  
**API → Kafka → Spark → Dashboard**

Author: Dorra Kallel

---

## 1. General Overview

This project implements a real-time data engineering pipeline that ingests live data from a public REST API, streams it through Apache Kafka, processes it using Spark Structured Streaming, and visualizes insights in a live dashboard.

The system simulates a production-grade architecture used in modern data platforms for real-time analytics.

Pipeline flow:

API → Kafka → Spark Streaming → Aggregations → Dashboard

---

## 2. Business Context and Scenario

### 2.1 Chosen Scenario — Real-Time Markets Monitoring

We selected the **Markets API scenario** using cryptocurrency price data.

The objective is to simulate a monitoring platform used by financial analysts or trading platforms to observe asset prices in real time.

---

### 2.2 Business Goals

The system allows teams to:

- monitor real-time price evolution
- detect volatility spikes
- identify trends
- compare assets
- compute statistical indicators

---

### 2.3 Actors

- Data Team → maintains pipeline
- Analysts → analyze trends
- Business users → make decisions

---

## 3. Learning Objectives

This project demonstrates ability to:

- design streaming architectures
- implement API ingestion pipelines
- work with Kafka messaging systems
- build Spark Structured Streaming jobs
- perform windowed aggregations
- manage streaming state
- visualize real-time data

---

## 4. Technical Scope

### 4.1 Architecture Overview

Components:

1. API client (Python producer)
2. Kafka broker
3. Spark streaming processor
4. Real-time dashboard

---

### 4.2 Mandatory Components Implemented

✔ Real API used  
✔ Kafka ingestion pipeline  
✔ Spark Structured Streaming job  
✔ Window aggregations  
✔ Watermark handling  
✔ Checkpointing  
✔ Real-time dashboard  

---

### 4.3 Optional Enhancements Implemented

✔ Aggregated metrics topic  
✔ KPI calculations  
✔ Monitoring via Spark UI  

---

## 5. Scenario Selection and Specifications

### 5.1 Selected API

API: CoinGecko  
Endpoint:

https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd

Reasons:

- Free access
- No authentication
- JSON format
- High rate limits
- Low latency

Example JSON response:

{
  "bitcoin": {"usd": 65000},
  "ethereum": {"usd": 3500}
}

---

### 5.2 Functional Specifications

KPIs computed:

- average price
- max price
- min price
- event count
- last value
- trend curves

---

### 5.3 Technical Specifications

Data format: JSON  
Processing type: streaming  

Window configuration:

- window size → 5 minutes
- slide interval → 1 minute
- watermark → 2 minutes

Target latency:

< 10 seconds end-to-end

---

## 6. Architecture Details

### 6.1 Ingestion Layer — API + Kafka

The producer script:

- queries API every few seconds
- parses JSON
- adds timestamp
- sends events to Kafka topic

Topic:

raw_api_events

---

### 6.2 Processing Layer — Spark Streaming

Spark performs:

- readStream from Kafka
- JSON parsing with schema
- timestamp conversion
- watermarking
- window aggregations
- KPI calculations

---

### 6.3 Exposure Layer — Dashboard

Dashboard displays:

- live price curves
- KPIs
- latest values
- comparisons

Auto refresh interval: few seconds

---

### 6.4 Infrastructure Layer

Kafka runs using Docker Compose.

---

## 7. Implementation Steps

### 7.1 Project Initialization

Repository created with structured folders.

---

### 7.2 Architecture Design

Defined:

- Kafka topics
- event schema
- processing logic
- KPIs

---

### 7.3 Kafka Setup

Docker started Kafka broker.

Producer successfully sent messages.

---

### 7.4 Spark Streaming

Streaming job:

- reads Kafka
- parses JSON
- computes aggregations
- outputs metrics

---

### 7.5 Dashboard

Streamlit dashboard implemented with:

- time series chart
- KPI metrics
- real-time refresh

---

### 7.6 Monitoring

Spark UI used to monitor:

- batch time
- processed rows
- latency

URL:

http://localhost:4040

---

### 7.7 Reproducibility

Startup order:

1. start Kafka
2. start producer
3. start Spark
4. start dashboard

---

### 7.8 Documentation

Full documentation provided in README with:

- architecture
- setup instructions
- design decisions

---

## 8. Technical Requirements Compliance

### 8.1 API + Kafka

✔ JSON messages  
✔ schema mapping  
✔ error handling  

---

### 8.2 Streaming Processing

✔ Spark Structured Streaming  
✔ window aggregations  
✔ grouping by asset  

---

### 8.3 State Management

✔ checkpoint directory used  
✔ restart recovery works  

---

### 8.4 Visualization

✔ real-time dashboard  
✔ multiple charts  
✔ KPIs displayed  

---

### 8.5 Monitoring

✔ Spark UI used  
✔ logs available  

---

### 8.6 Deployment

✔ clear commands  
✔ reproducible setup  

---

## 9. Project Organization

Project structure:

project/
├── docker/
├── src/
├── scripts/
├── checkpoints/
└── README.md

---

## 10. Deliverables

### 10.1 Code

Includes:

- producer script
- streaming job
- dashboard
- docker config

---

### 10.2 Documentation

Includes:

- architecture description
- setup guide
- KPI explanation

---

### 10.3 Demonstration

System demonstrates:

- live API data ingestion
- Kafka streaming
- Spark processing
- updating dashboard

---

## 11. Evaluation Criteria Coverage

### Functionality

✔ Full pipeline working

### Technical Quality

✔ Windows + watermark  
✔ checkpointing  
✔ stable processing  

### Documentation

✔ structured README  
✔ reproducible instructions  

### Best Practices

✔ clean code structure  
✔ modular scripts  

---

## 12. Submission Notes

Requirements:

- Python 3.10+
- Docker installed
- Internet connection

---

## 13. Conclusion

This project reproduces a real-world streaming architecture used in industry for:

- financial analytics
- IoT monitoring
- real-time insights

It demonstrates practical skills required for modern Data Engineering roles, covering ingestion, streaming computation, state management, and visualization.

---

