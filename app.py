import streamlit as st

st.set_page_config(
    page_title="EAST Product Hub",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 EAST Product Hub")

products = [
    "ShareFile",
    "MOVEit",
    "OpenEdge",
    "WhatsUp Gold",
    "Flowmon",
    "Chef",
    "Telerik",
    "MarkLogic",
    "LoadMaster"
]

selected = st.selectbox("Select Product", products)

# URLs
SHAREFILE_KB = "https://sharefile.lightning.force.com/lightning/o/Knowledge__kav/list?filterName=Copy_of_Published_Articles"
PROGRESS_KB = "https://progress.lightning.force.com/lightning/o/Knowledge__kav/list?filterName=EA_Ops_Knowledge_Published_Articles"

if selected == "ShareFile":

    st.header("📁 ShareFile")

    st.write("""
    ShareFile is a secure file sharing and content collaboration platform.
    """)

    st.subheader("🧩 Key Features")

    st.write("""
    • Secure File Sharing
    • Client Portal
    • Workflow Automation
    • Folder Permissions
    • Mobile Access
    • File Sync
    """)

    st.markdown(f"[ShareFile Knowledge Base]({SHAREFILEOVEit":

    st.header("📦 MOVEit")

    st.write("""
    MOVEit is a Managed File Transfer (MFT) solution used for secure data transfers.
    """)

    st.subheader("🧩 Key Features")

    st.write("""
    • Secure File Transfer
    • Transfer Automation
    • Encryption
    • Audit Logging
    • Compliance Support
    """)

    st.markdown(f"[Progress Knowledge Base]({ted == "OpenEdge":

    st.header("🖥️ OpenEdge")

    st.write("""
    OpenEdge is a business application development platform and database.
    """)

    st.subheader("🧩 Key Features")

    st.write("""
    • Application Development
    • Database Platform
    • Business Logic
    • Scalability
    """)

    st.markdown(f"[Progress Knowledge Baselected == "WhatsUp Gold":

    st.header("📊 WhatsUp Gold")

    st.write("""
    WhatsUp Gold is an IT infrastructure monitoring solution.
    """)

    st.markdown(f"[Progress_KB}")

elif selected == "Flowmon":

    st.header("🌐 Flowmon")

    st.write("""
    Flowmon provides network visibility and security monitoring.
    """)

    st.markdown(f"[Progress Knowledge Base]({ted == "Chef":

    st.header("⚙️ Chef")

    st.write("""
    Chef is an infrastructure automation platform.
    """)

    st.markdown(f"{PROGRESS_KB}")

elif selected == "Telerik":

    st.header("💻 Telerik")

    st.write("""
    Telerik provides UI controls and developer tools.
    """)

    st.markdown(f"{PROGRESS_KB}")

elif selected == "MarkLogic":

    st.header("🗄️ MarkLogic")

    st.write("""
    MarkLogic is an enterprise data platform and database.
    """)

    st.markdown(f"{PROGRESS_KB}")

elif selected == "LoadMaster":

    st.header("⚖️ LoadMaster")

    st.write("""
    LoadMaster is a load balancing and application delivery solution.
    """)

    st.markdown(f"{PROGRESS_KB}")

st.divider()

st.header("🤖 Ask EAST AI")

question = st.text_input("Ask a question")

if question:
    st.info(f"You asked: {question}")
