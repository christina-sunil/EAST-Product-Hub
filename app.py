import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="EAST Product Hub",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 EAST Product Hub")

st.markdown("""
### Welcome to EAST Product Hub

Learn everything about Progress products:

✅ Product Overview

✅ Business Purpose

✅ Opportunity Process

✅ Quote Process

✅ Asset Process

✅ Renewal Process

✅ Common Support Requests

✅ Ask EAST AI
""")

# Load CSV
df = pd.read_csv("data/products.csv")

# Product selection
product = st.selectbox(
    "Select Product",
    sorted(df["Product"].unique())
)

# Get selected row
selected = df[df["Product"] == product].iloc[0]

st.success(f"Selected Product: {product}")

st.divider()

st.subheader("📖 Product Overview")
st.write(selected["Overview"])

st.subheader("👥 Common Users")
st.write(selected["Users"])

st.subheader("🔗 Related Systems")
st.write(selected["Systems"])

st.subheader("🎫 Support Areas")
st.write(selected["Support"])

st.divider()

st.subheader("🔄 Standard Business Process")

st.code("""
Lead
↓
Opportunity
↓
Quote
↓
Order
↓
Provisioning
↓
Asset
↓
Renewal
""")

st.divider()

st.subheader("🤖 Ask EAST AI")

question = st.text_input(
    "Ask a question about the selected product"
)

if question:
    st.info(
        f"Future AI Response for: {question}"
    )

st.divider()

st.caption("EAST Product Hub")
