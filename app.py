import streamlit as st

st.set_page_config(
    page_title="EAST Product Hub",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 EAST Product Hub")

st.write("Welcome to EAST Product Hub")

products = [
    "ShareFile",
    "MOVEit",
    "Telerik",
    "MarkLogic",
    "OpenEdge",
    "LoadMaster",
    "Chef",
    "Flowmon",
    "WhatsUp Gold"
]

selected = st.selectbox(
    "Select Product",
    products
)

st.success(f"Selected Product: {selected}")

st.subheader("Product Overview")

st.write(
    "This is the EAST Product Hub. Product knowledge will be displayed here."
)

st.subheader("Ask EAST AI")

question = st.text_input(
    "Ask a question"
)

if question:
    st.write(f"You asked: {question}")
