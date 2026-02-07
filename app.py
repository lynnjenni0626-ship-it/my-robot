import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime
from io import BytesIO

# 1. Page Settings
st.set_page_config(page_title="My AI Robot", layout="wide")

# 2. Robot Memory (Keeps data while the app is open)
if 'robot_memory' not in st.session_state:
    st.session_state.robot_memory = pd.DataFrame(
        columns=["Timestamp", "AI_Insight", "Confidence_Score", "System_Status"]
    )

# 3. The Robot Brain Logic
def run_robot_cycle():
    timestamp = datetime.now().strftime("%H:%M:%S")
    score = round(np.random.uniform(90.0, 99.9), 2)
    insights = [
        "Analyzing Market Trends...", 
        "Optimizing Database...", 
        "Scanning for Errors...", 
        "Efficiency at Peak Performance"
    ]
    
    new_entry = {
        "Timestamp": timestamp,
        "AI_Insight": np.random.choice(insights),
        "Confidence_Score": score,
        "System_Status": "Healthy"
    }
    
    # Add new result to our list
    st.session_state.robot_memory = pd.concat(
        [pd.DataFrame([new_entry]), st.session_state.robot_memory], 
        ignore_index=True
    ).head(20) # Keep last 20 rows so it doesn't get too crowded

# 4. Visual Dashboard Interface
st.title("🤖 My Autonomous AI Robot")
st.write("This robot runs 'like clockwork' and updates every 30 seconds.")

# Run the robot
run_robot_cycle()

# Top Row: Big Numbers
latest = st.session_state.robot_memory.iloc[0]
c1, c2, c3 = st.columns(3)
c1.metric("Robot Status", "ONLINE ✅")
c2.metric("Latest Score", f"{latest['Confidence_Score']}%")
c3.metric("Last Update", latest["Timestamp"])

# Middle Row: Visual Intelligence Chart
st.subheader("📈 Performance Trend (Visual Intelligence)")
if len(st.session_state.robot_memory) > 1:
    chart_data = st.session_state.robot_memory.copy()
    st.line_chart(chart_data.set_index('Timestamp')['Confidence_Score'])

# Bottom Row: Data Log
st.subheader("📄 Robot Production Log")
st.table(st.session_state.robot_memory)

# 5. Export to Excel Feature
def convert_to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Robot_Log')
    return output.getvalue()

st.divider()
excel_file = convert_to_excel(st.session_state.robot_memory)
st.download_button(
    label="📥 Download Excel Report",
    data=excel_file,
    file_name=f"Robot_Report_{datetime.now().strftime('%Y-%m-%d')}.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

# 6. The Clockwork (Auto-refresh)
time.sleep(30)
st.rerun()

