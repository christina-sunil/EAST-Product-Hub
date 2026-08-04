import streamlit as st

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

products = [
    "ShareFile",
    "Telerik",
    "MOVEit",
    "MarkLogic",
    "OpenEdge",
    "LoadMaster",
    "Flowmon",
    "WhatsUp Gold",
    "Chef"
]

selected = st.selectbox(
    "Select Product",
    products
)

if selected:
    st.success(f"Selected Product: {selected}")

st.subheader("🤖 Ask EAST AI")

question = st.text_input(
    "Ask a product question"
)

if question:
    st.write(f"Question: {question}")

