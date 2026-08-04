import streamlit as st

st.set_page_config(
    page_title="EAST Product Hub",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 EAST Product Hub")

st.markdown("""
### Welcome to EAST Product Hub

Your one-stop learning portal for Progress products.

Learn:

✅ What the product does

✅ Why customers use it

✅ Business purpose

✅ Opportunity process

✅ Quote process

✅ Asset process

✅ Renewal process

✅ Common support scenarios

✅ Ask EAST AI
""")

# Product Categories

products = {
    "Digital Experience": [
        "ShareFile",
        "MOVEit",
        "Podio",
        "Kendo UI",
        "Telerik",
        "Sitefinity Cloud",
        "Sitefinity Insight",
        "Ucommerce",
        "Test Studio",
        "Fiddler Everywhere",
        "ThemeBuilder"
    ],
    "Infrastructure Management": [
        "LoadMaster",
        "Flowmon",
        "WhatsUp Gold",
        "Opsmith",
        "Chef",
        "Chef Infrastructure",
        "Chef Desktop",
        "Chef App Delivery",
        "Chef Compliance",
        "Chef 360"
    ],
    "Data & AI": [
        "MarkLogic",
        "Semaphore",
        "OpenEdge",
        "DataDirect Connectors",
        "Hybrid Data Pipeline",
        "OpenAccess",
        "Agentic RAG",
        "Progress Data Platform"
    ],
    "Decisioning": [
        "Corticon.js"
    ],
    "File Transfer": [
        "WS_FTP",
        "Automate MFT"
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

st.subheader("📖 Product Overview")

st.info(f"""
Selected Product: {product}

This section will provide:

• What the product does

• Business value

• Key features

• Typical customers

• Opportunity workflow

• Quote workflow

• Asset workflow

• Renewal workflow

• Related systems

• EAST support ownership
""")

st.divider()

st.subheader("🔄 Business Process")

st.markdown("""
