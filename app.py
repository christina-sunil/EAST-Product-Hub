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

✅ Common Users

✅ Related Systems

✅ Support Areas

✅ Standard Business Process

✅ Ask EAST AI
""")

try:
    # Read Product Data
    df = pd.read_csv("data/products.csv")

    # Product Selection
    product = st.selectbox(
        "Select Product",
        sorted(df["Product"].unique())
    )

    # Selected Product Information
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

    # Support Section
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

    # AI Section
    st.subheader("🤖 Ask EAST AI")

    st.markdown("""
Example Questions:

• What does this product do?

• Why do customers use it?

• What systems are involved?

• How does the Opportunity process work?

• How does the Quote process work?

• What support does EAST provide?
""")

    question = st.text_input(
        "Ask a question about the selected product"
    )

    if question:
        st.success(
            f"Question received: {question}"
        )

except Exception as e:
    st.error(f"Application Error: {e}")

st.divider()

st.caption(
    "EAST Product Hub | Progress Product Learning & Support Portal"
)
