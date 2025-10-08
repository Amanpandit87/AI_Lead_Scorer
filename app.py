import streamlit as st
import pandas as pd
import re

st.set_page_config(page_title="AI Lead Scorer", page_icon="🤖", layout="wide")
st.title("🤖 AI Lead Scorer Tool")
st.write("Upload your leads CSV and get AI-readiness score + top companies easily.")

# ---------- Upload CSV ----------
uploaded_file = st.file_uploader("📂 Upload your leads CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # ---------- Email Validation ----------
    def validate_email(email):
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if re.match(pattern, email):
            return True 
        return False

    df["Email_Valid"] = df["Email"].apply(validate_email)

    # ---------- Highlight Top AI Leads ----------
    df["Top_Lead"] = df["Score"].apply(lambda x: "✅" if x >= 80 else "")

    # ---------- Display Table ----------
    st.subheader("📊 Analyzed Leads")
    st.dataframe(df)

    # ---------- Top 10 Leads ----------
    st.subheader("🏆 Top 10 AI-Ready Companies")
    top10 = df.sort_values(by="Score", ascending=False).head(10)
    st.table(top10[["Company", "Email", "Industry", "Employees", "Revenue ($M)", "Score"]])

    # ---------- Bar Chart ----------
    st.subheader("📈 AI Readiness Score Chart")
    st.bar_chart(df.set_index("Company")["Score"])

    # ---------- Download CSV ----------
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="⬇️ Download Scored Leads CSV",
        data=csv,
        file_name="scored_leads_50.csv",
        mime="text/csv"
    )

else:
    st.info("👆 Please upload a CSV file (e.g., leads_50.csv) to start the analysis.")
