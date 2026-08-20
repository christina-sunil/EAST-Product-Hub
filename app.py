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
"LoadMaster",
"Agentic RAG",
"Corticon",
"DataDirect",
"Data Platform",
"Semaphore",
"Fiddler",
"Kendo UI",
"Automate MFT",
"WS_FTP",
"Podio",
"Sitefinity",
"Test Studio",
"Opsmith"
]

selected = st.selectbox("Select Product", products)

SHAREFILE_KB = "https://sharefile.lightning.force.com/lightning/o/Knowledge__kav/list?filterName=Copy_of_Published_Articles"
PROGRESS_KB = "https://progress.lightning.force.com/lightning/o/Knowledge__kav/list?filterName=EA_Ops_Knowledge_Published_Articles"


if selected == "ShareFile":

    st.header("📁 ShareFile")

    st.subheader("What is ShareFile?")

    st.write("""
ShareFile is a secure file sharing and content collaboration platform used to store,
manage and share files securely with customers, partners and internal teams.
""")

    st.subheader("Key Features")

    st.write("""
- Secure file sharing
- Client portal
- Workflow automation
- Folder permissions
- Mobile access
- File sync
""")

    st.subheader("Common Ticket Patterns")

    st.write("""
- ShareFile access requests
- User role and permission updates
- Intranet content access issues
- Bulk file sync requests
- Bulk file export requests
- ShareFile and Salesforce integration questions
- Shared folder access issues
""")

    st.subheader("Knowledge Base")

    st.markdown(
        "[ShareFile Knowledge Base](https://sharefile.lightning.force.com/lightning/o/Knowledge__kav/list?filterName=Copy_of_Published_Articles)"
    )


elif selected == "MOVEit":

    st.header("📦 MOVEit")

    st.subheader("What is MOVEit?")

    st.write("""
MOVEit is a Managed File Transfer solution used to securely transfer sensitive files
between systems, users and organizations.
""")

    st.subheader("Key Features")

    st.write("""
- Secure file transfer
- Transfer automation
- Encryption
- Audit logging
- Compliance support
- Scheduled transfers
- Secure external transfer
""")

    st.subheader("Common Ticket Patterns")

    st.write("""
- MOVEit Transfer build updates
- MOVEit service pack requests
- MOVEit hotfix requests
- MOVEit WAF security update requests
- MOVEit reporting and access requests
- MOVEit Automation migration-related requests
""")

    st.subheader("Knowledge Base")

    st.markdown(
        "[Progress Knowledge Base](https://progress.lightning.force.com/lightning/o/Knowledge__kav/list?filterName=EA_Ops_Knowledge_Published_Articles)"
    )


elif selected == "OpenEdge":

    st.header("🖥️ OpenEdge")

    st.subheader("What is OpenEdge?")

    st.write("""
OpenEdge is a Progress application development platform and database used to build,
deploy and manage business-critical applications.
""")

    st.subheader("Key Features")

    st.write("""
- Application development
- Database platform
- Business logic processing
- Secure data management
- Scalability
- Cloud deployment support
""")

    st.subheader("Common Ticket Patterns")

    st.write("""
- OpenEdge community or group access issues
- OpenEdge account or license movement requests
- OpenEdge KAM rule updates
- OpenEdge form and product mapping requests
- OpenEdge content or marketing support requests
""")

    st.subheader("Knowledge Base")

    st.markdown(
        "[Progress Knowledge Base](https://progress.lightning.force.com/lightning/o/Knowledge__kav/list?filterName=EA_Ops_Knowledge_Published_Articles)"
    )


elif selected == "WhatsUp Gold":

    st.header("📊 WhatsUp Gold")

    st.subheader("What is WhatsUp Gold?")

    st.write("""
WhatsUp Gold is an IT infrastructure monitoring solution used to monitor networks,
servers, applications and devices.
""")

    st.subheader("Key Features")

    st.write("""
- Network monitoring
- Server monitoring
- Application monitoring
- Performance monitoring
- Alerting
- Reporting
""")

    st.subheader("Common Ticket Patterns")

    st.write("""
- WhatsUp Gold price list updates
- WhatsUp Gold renewal quote issues
- WhatsUp Gold and NTA license association requests
- WhatsUp Gold customer or user reporting requests
- WhatsUp Gold renewal opportunity or quote mismatch issues
""")

    st.subheader("Knowledge Base")

    st.markdown(
        "[Progress Knowledge Base](https://progress.lightning.force.com/lightning/o/Knowledge__kav/list?filterName=EA_Ops_Knowledge_Published_Articles)"
    )


elif selected == "Flowmon":

    st.header("🌐 Flowmon")

    st.subheader("What is Flowmon?")

    st.write("""
Flowmon is a network visibility, performance monitoring and security analytics solution.
""")

    st.subheader("Key Features")

    st.write("""
- Network visibility
- Traffic analysis
- Threat detection
- Security analytics
- Performance monitoring
- Incident investigation
""")

    st.subheader("Common Ticket Patterns")

    st.write("""
- Flowmon reseller or data field issues
- Flowmon customer reporting requests
- Flowmon partner or product mapping updates
- Flowmon infrastructure customer list requests
""")

    st.subheader("Knowledge Base")

    st.markdown(
        "[Progress Knowledge Base](https://progress.lightning.force.com/lightning/o/Knowledge__kav/list?filterName=EA_Ops_Knowledge_Published_Articles)"
    )


elif selected == "Chef":

    st.header("⚙️ Chef")

    st.subheader("What is Chef?")

    st.write("""
Chef is an infrastructure automation platform used to automate server configuration,
deployment and compliance management.
""")

    st.subheader("Key Features")

    st.write("""
- Configuration management
- Infrastructure automation
- Compliance automation
- Continuous delivery
- Policy enforcement
""")

    st.subheader("Common Ticket Patterns")

    st.write("""
- Chef release or software list updates
- Chef product reporting requests
- Chef partner or product setup updates
- Chef infrastructure customer list requests
""")

    st.subheader("Knowledge Base")

    st.markdown(
        "[Progress Knowledge Base](https://progress.lightning.force.com/lightning/o/Knowledge__kav/list?filterName=EA_Ops_Knowledge_Published_Articles)"
    )


elif selected == "Telerik":

    st.header("💻 Telerik")

    st.subheader("What is Telerik?")

    st.write("""
Telerik provides UI controls, reporting tools and developer productivity solutions
for .NET and JavaScript applications.
""")

    st.subheader("Key Features")

    st.write("""
- UI components
- Reporting tools
- Document processing
- Testing tools
- Developer productivity
""")

    st.subheader("Common Ticket Patterns")

    st.write("""
- Telerik order asset and account matching issues
- Telerik contact and account cleanup requests
- Telerik partner or product setup updates
- Telerik asset ownership or renewal ownership issues
""")

    st.subheader("Knowledge Base")

    st.markdown(
        "[Progress Knowledge Base](https://progress.lightning.force.com/lightning/o/Knowledge__kav/list?filterName=EA_Ops_Knowledge_Published_Articles)"
    )


elif selected == "MarkLogic":

    st.header("🗄️ MarkLogic")

    st.subheader("What is MarkLogic?")

    st.write("""
MarkLogic is an enterprise data platform and database used to manage structured
and unstructured data.
""")

    st.subheader("Key Features")

    st.write("""
- Enterprise database
- Search capabilities
- Data integration
- Security
- Scalability
- Data management
""")

    st.subheader("Common Ticket Patterns")

    st.write("""
- MarkLogic support contact field updates
- MarkLogic Support Link enablement requests
- MarkLogic case severity handling updates
- MarkLogic reporting or export requests
- MarkLogic customer access or Salesforce case setup requests
""")

    st.subheader("Knowledge Base")

    st.markdown(
        "[Progress Knowledge Base](https://progress.lightning.force.com/lightning/o/Knowledge__kav/list?filterName=EA_Ops_Knowledge_Published_Articles)"
    )


elif selected == "LoadMaster":

    st.header("⚖️ LoadMaster")

    st.subheader("What is LoadMaster?")

    st.write("""
LoadMaster is a load balancing and application delivery solution used to improve
application performance, availability and security.
""")

    st.subheader("Key Features")

    st.write("""
- Load balancing
- High availability
- SSL offloading
- Application delivery
- Traffic management
- Disaster recovery support
""")

    st.subheader("Common Ticket Patterns")

    st.write("""
- LoadMaster asset visibility issues
- LoadMaster support queue or email notification updates
- LoadMaster quote or renewal mismatch issues
- LoadMaster asset or account discrepancy requests
- LoadMaster customer asset mapping requests
""")

    st.subheader("Knowledge Base")

    st.markdown(
        "[Progress Knowledge Base](https://progress.lightning.force.com/lightning/o/Knowledge__kav/list?filterName=EA_Ops_Knowledge_Published_Articles)"
    )
else:

st.header(selected)

st.subheader("Business Unit")

st.write("To be confirmed")

st.subheader("👤 Product Owner")

st.write("To be confirmed")

st.subheader("🎯 SME / Product Contacts")

st.write("To be confirmed")

st.subheader("🛠️ Tools Used")

st.write("To be confirmed")

st.subheader("📚 Knowledge Base")

st.write("Content coming soon.")

st.divider()

st.header("🤖 Ask EAST AI")

question = st.text_input("Ask a question")

if question:
    st.info(f"You asked: {question}")
