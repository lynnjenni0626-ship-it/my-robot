import streamlit as st
import pandas as pd
from st_paywall import add_auth

# 1. THE BOUNCER: This stops people until they pay
add_auth(required=True)

st.title("🤖 Premium Robot Dashboard")
st.write(f"Welcome back, **{st.session_state.user_email}**!")

# 2. THE DATA: Your specialized robot insights
data = {
    "AI_Insight": ["Market Analysis", "Trend Prediction", "Efficiency Audit"],
    "Value_Score": [98.5, 94.2, 97.8],
    "Status": ["Complete", "Ready", "Optimized"]
}
df = pd.DataFrame(data)

st.subheader("📊 Your AI Insights")
st.table(df)

# 3. THE PRODUCT: The download button for your reports
st.subheader("📥 Download Your Expert Report")
csv = df.to_csv(index=False).encode('utf-8')

st.download_button(
    label="Download Expert Report (.CSV)",
    data=csv,
    file_name='Expert_Robot_Report.csv',
    mime='text/csv',
)

st.success("Your subscription is ACTIVE. You have full access!")
