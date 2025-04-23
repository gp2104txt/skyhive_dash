import streamlit as st
import pandas as pd
import numpy as np
import datetime

st.set_page_config(layout="wide")

# ----- Dashboard 1: Single Simulator Overview -----
st.title("🛩️ Single Simulator Live Operations Dashboard")

col1, col2, col3 = st.columns(3)

# Simulation Core Status
with col1:
    st.subheader("🎮 Simulation Core Status")
    sim_state = st.radio("Simulation State", ["INIT", "RUNNING", "PAUSED", "FAULTED"])
    st.metric("Scenario Time Elapsed", "{:0.1f} min".format(np.random.uniform(10, 60)))
    st.metric("Remaining Time", "{:0.1f} min".format(np.random.uniform(10, 60)))
    st.map(pd.DataFrame({"lat": [45.07], "lon": [7.69]}))  # Example coordinates

# System Health Matrix
with col2:
    st.subheader("💾 Computing Cluster Health")
    machines = ["IG_PC", "MainSim_PC", "MotionCtrl_PC"]
    for m in machines:
        st.text(m)
        st.progress(np.random.randint(30, 100))
        st.text(f"Temp: {np.random.randint(40, 80)}°C")

# Motion & Control
with col3:
    st.subheader("🕹️ Motion & Control")
    st.line_chart(pd.DataFrame(np.random.randn(10, 3), columns=['X', 'Y', 'Z']))
    st.text("Control Loop Latency: {} ms".format(np.random.randint(3, 20)))

# Environmental & Power
col4, col5 = st.columns(2)

with col4:
    st.subheader("🌡️ Environment")
    st.metric("Air Temp", f"{np.random.uniform(20.0, 25.0):.1f} °C")
    st.metric("Humidity", f"{np.random.uniform(30, 50):.0f}%")
    st.metric("Air Quality Index", f"{np.random.randint(0, 100)}")

with col5:
    st.subheader("🔌 Power & UPS")
    st.metric("Current Draw", f"{np.random.uniform(3.5, 5.0):.1f} kW")
    st.metric("UPS Time Left", f"{np.random.randint(5, 30)} min")

# Predictive & Support
st.subheader("🧠 Predictive Insights & Support")
col6, col7 = st.columns(2)

with col6:
    st.text("Top 3 Predictive Failures")
    st.write("1. Disk IG_PC - 92% wear")
    st.write("2. GPU MainSim_PC - temp trending up")
    st.write("3. Projector 2 bulb - 1200h usage")

with col7:
    st.text("Support Tools")
    st.button("📋 Dump Logs")
    st.button("🔄 Restart Subsystem")

# ----- Dashboard 2: Fleet-Wide View -----
st.title("🌍 Fleet-Wide Simulator Monitoring")

# Geo Map
st.subheader("🗺️ Simulator Global Locations")
locations = pd.DataFrame({
    'lat': [45.07, 48.85, 34.05],
    'lon': [7.69, 2.35, -118.25],
    'status': ['🟢', '🟡', '🔴']
})
st.map(locations)

# Fleet KPIs
col8, col9, col10 = st.columns(3)
with col8:
    st.metric("Avg Uptime (7d)", "98.2%")
with col9:
    st.metric("Open Tickets", "14")
with col10:
    st.metric("Worst Incident Rate", "Sim-03 (5/day)")

# Fleet Alerts
st.subheader("📋 Fleet Alerts & Predictions")
st.write("- Sim-01: Projector 1 nearing EOL (1400h)\n- Sim-07: UPS Battery Degradation\n- Sim-12: Abnormal thermal rise")

# Trends
st.subheader("📊 Global Ops Analytics")
st.area_chart(pd.DataFrame(
    {
        "Failures": np.random.randint(0, 5, 10),
        "Fix Time (h)": np.random.rand(10) * 3
    }
))

st.write("\n🔧 *Powered by Streamlit. Designed for proactive ops.*")
