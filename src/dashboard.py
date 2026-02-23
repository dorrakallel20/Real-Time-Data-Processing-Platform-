import streamlit as st
import pandas as pd
import json
from kafka import KafkaConsumer
import plotly.express as px

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Real-Time Crypto Monitor",
    layout="wide"
)

st.title("🚀 Real-Time Crypto Streaming Dashboard")

# ---------- KAFKA CONNECTION ----------
@st.cache_resource
def get_consumer():
    return KafkaConsumer(
        "raw_events",
        bootstrap_servers="localhost:9092",
        value_deserializer=lambda x: json.loads(x.decode("utf-8")),
        auto_offset_reset="latest",
        enable_auto_commit=True
    )

consumer = get_consumer()

# ---------- DATA STORAGE ----------
data = []

placeholder = st.empty()

# ---------- STREAM LOOP ----------
for message in consumer:
    data.append(message.value)

    # limit memory (keep last 100 rows)
    if len(data) > 100:
        data.pop(0)

    df = pd.DataFrame(data)

    # ---------- DATA CLEANING ----------
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp")

    with placeholder.container():

        # ---------- KPIs ----------
        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Records", len(df))
        col2.metric("BTC Latest", f"${df['btc'].iloc[-1]:,.2f}")
        col3.metric("ETH Latest", f"${df['eth'].iloc[-1]:,.2f}")
        col4.metric("Last Update", df["timestamp"].iloc[-1].strftime("%H:%M:%S"))

        st.divider()

        # ---------- PRICE CHART ----------
        fig = px.line(
            df,
            x="timestamp",
            y=["btc", "eth"],
            markers=True,
            title="Live Crypto Prices"
        )

        fig.update_layout(
            xaxis_title="Timestamp",
            yaxis_title="Price (USD)",
            legend_title="Currency",
            hovermode="x unified"
        )

        st.plotly_chart(fig, use_container_width=True)

        # ---------- CHANGE CHART ----------
        df["btc_change"] = df["btc"].diff()
        df["eth_change"] = df["eth"].diff()

        fig2 = px.bar(
            df,
            x="timestamp",
            y=["btc_change", "eth_change"],
            title="Price Change Per Tick"
        )

        st.plotly_chart(fig2, use_container_width=True)

        # ---------- TABLE ----------
        st.subheader("Latest Record")
        st.dataframe(df.tail(1), use_container_width=True)

        # ---------- DOWNLOAD ----------
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
    label="Download CSV",
    data=csv,
    file_name="crypto_stream.csv",
    mime="text/csv",
    key="download_crypto"  # <-- add a unique key here
)
