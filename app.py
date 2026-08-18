import streamlit as st

st.set_page_config(
    page_title="EAST Product Hub",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 EAST Product Hub")
st.write("Welcome to the EAST Product Hub")

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

if selected == "ShareFile":
    st.header("📁 ShareFile")
    st.write("ShareFile is a secure file sharing and content collaboration platform.")
    st.subheader("Knowledge Base")
    st.markdown("[ShareFile Knowledge Base](https://sharefile.lightning.force.com/lightning/o/Knowledge__kav/list?filterName=Copy_of_Published_Articles)")

elif selected == "MOVEit":
    st.header("📦 MOVEit")
    st.write("MOVEit is a Managed File Transfer (MFT) solution used for secure file transfers.")
    st.subheader("Knowledge Base")
    st.markdown("[Progress Knowledge Base](https://progress.lightning.force.com/lightning/o/Knowledge__kav/list?filterName=EA_Ops_Knowledge_Published_Articles)")

elif selected == "OpenEdge":
    st.header("🖥️ OpenEdge")
    st.write("OpenEdge is a business application development platform and database.")
    st.subheader("Knowledge Base")
    st.markdown("[Progress Knowledge Base](https://progress.lightning.force.com/lightning/o/Knowledge__kav/list?filterName=EA_Ops_Knowledge_Published_Articles)")

elif selected == "WhatsUp Gold":
    st.header("📊 WhatsUp Gold")
    st.write("WhatsUp Gold is an IT infrastructure monitoring solution.")
    st.subheader("Knowledge Base")
    st.markdown("[Progress Knowledge Base](https://progress.lightning.force.com/lightning/o/Knowledge__kav/list?filterName=EA_Ops_Knowledge_Published_Articles)")

elif selected == "Flowmon":
    st.header("🌐 Flowmon")
    st.write("Flowmon provides network visibility and security monitoring.")
    st.subheader("Knowledge Base")
    st.markdown("[Progress Knowledge Base](https://progress.lightning.force.com/lightning/o/Knowledge__kav/list?filterName=EA_Ops_Knowledge_Published_Articles)")

elif selected == "Chef":
    st.header("⚙️ Chef")
    st.write("Chef is an infrastructure automation platform.")
    st.subheader("Knowledge Base")
    st.markdown("[Progress Knowledge Base](https://progress.lightning.force.com/lightning/o/Knowledge__kav/list?filterName=EA_Ops_Knowledge_Published_Articles)")

elif selected == "Telerik":
    st.header("💻 Telerik")
    st.write("Telerik provides UI controls and developer tools.")
    st.subheader("Knowledge Base")
    st.markdown("[Progress Knowledge Base](https://progress.lightning.force.com/lightning/o/Knowledge__kav/list?filterName=EA_Ops_Knowledge_Published_Articles)")

elif selected == "MarkLogic":
    st.header("🗄️ MarkLogic")
    st.write("MarkLogic is an enterprise data platform and database.")
    st.subheader("Knowledge Base")
    st.markdown("[Progress Knowledge Base](https://progress.lightning.force.com/lightning/o/Knowledge__kav/list?filterName=EA_Ops_Knowledge_Published_Articles)")

elif selected == "LoadMaster":
    st.header("⚖️ LoadMaster")
    st.write("LoadMaster is a load balancing and application delivery solution.")
    st.subheader("Knowledge Base")
    st.markdown("[Progress Knowledge Base](https://progress.lightning.force.com/lightning/o/Knowledge__kav/list?filterName=EA_Ops_Knowledge_Published_Articles)")

st.divider()

st.header("🤖 Ask EAST AI")

question = st.text_input("Ask a question")

if question:
    st.info(f"You asked: {question}")
