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

products = {
    "Digital Experience": [
        "ShareFile",
        "MOVEit",
        "Podio",
        "Kendo UI",
        "Telerik"
    ],
    "Infrastructure": [
        "LoadMaster",
        "Flowmon",
        "WhatsUp Gold",
        "Chef"
    ],
    "Data & AI": [
        "MarkLogic",
        "OpenEdge",
        "Semaphore"
    ]
}

category = st.selectbox(
    "Select Category",
    list(products.keys())
)

product = st.selectbox(
    "Select Product",
    products[category]
)

st.success(f"Selected Product: {product}")

st.divider()

st.subheader("📖 Product Knowledge")

if product == "ShareFile":
    try:
        with open("data/sharefile.txt", "r") as file:
            content = file.read()

        st.text(content)

    except Exception as e:
        st.error(f"Unable to load ShareFile information: {e}")

else:
    st.info(f"Knowledge page for {product} coming soon.")

st.divider()

st.subheader("🤖 Ask EAST AI")

question = st.text_input(
    "Ask a question about the product"
)

if question:
    st.write(question)

st.divider()

st.caption("EAST Product Hub")
