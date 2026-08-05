import streamlit as st
import pandas as pd

# Page Setup
st.set_page_config(
    page_title="EAST Product Hub",
    page_icon="🚀",
    layout="wide"
)

# Header
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

# Read CSV File
df = pd.read_csv("data/products.csv")

# Product Selection
product = st.selectbox(
    "Select Product",
    sorted(df["Product"].unique())
)

# Get Product Information
selected = df[df["Product"] == product].iloc[0]

st.success(f"Selected Product: {product}")

st.divider()

# Product Information
col1, col2 = st.columns(2)

with col1:
    st.subheader("📖 Product Overview")
    st.info(selected["Overview"])

    st.subheader("👥 Common Users")
    st.info(selected["Users"])

with col2:
    st.subheader("🔗 Related Systems")
    st.info(selected["Systems"])

    st.subheader("🎫 Support Areas")
    st.info(selected["Support"])

st.divider()

# Business Process
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

# EAST Support Section
st.subheader("🛠 EAST Support Responsibilities")

st.markdown("""
- Opportunity Support
- Quote Support
- Asset Creation
- License Activation
- Renewals
- Customer Requests
- Data Updates
- Escalations
""")

st.divider()

# AI Assistant Section
st.subheader("🤖 Ask EAST AI")

st.markdown("""
Example Questions:

• What does this product do?

• Who uses this product?

• What systems are involved?

• How does Opportunity work?

• How does Quote work?

• How does Renewal work?

• What does EAST support?
""")

question = st.text_input(
    "Ask a question about the selected product"
)

if question:
    st.success("Future AI response will be displayed here")

st.divider()

st.caption(
    "EAST Product Hub | Progress Product Learning & Support Portal"
)
