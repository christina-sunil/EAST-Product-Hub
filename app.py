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

st.write(f"""
**Product:** {product}

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

st.subheader("🎫 Common Support Requests")

st.markdown("""
- License activation
- Contact updates
- Opportunity updates
- Quote corrections
- Asset creation
- Renewal assistance
- Customer access issues
- Billing questions
""")

st.divider()

st.subheader("🤖 Ask EAST AI")

question = st.text_input(
    "Ask a question about the selected product"
)

if question:
    st.write("Question:")
    st.write(question)

    st.success(
        "Future version: AI will answer using product documentation, SOPs, KB articles and EAST knowledge."
    )

st.divider()

st.caption(
    "EAST Product Hub | Progress Product Learning & Support Portal"
)
