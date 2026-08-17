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

# SHAREFILE

if selected == "ShareFile":

    st.subheader("📘 What is ShareFile?")

    st.write("""
    ShareFile is a secure file sharing and content collaboration platform.
    Organizations use it to store, manage, and securely share files with employees,
    customers, and business partners.
    """)

    st.subheader("🌐 Progress Product Portfolio")

    st.markdown("""
    ### Explore Progress Products

    - [View All Progress Products](https://www.progress.com/products)

    Related Progress products include:

    - ShareFile
    - MOVEit
    - WS_FTP
    - Podio
    - Sitefinity
    - Telerik
    - Kendo UI
    - Test Studio
    - OpenEdge
    - MarkLogic
    - DataDirect
    - Chef
    - Flowmon
    - LoadMaster
    - WhatsUp Gold
    """)

    st.subheader("🎯 Why Customers Use It")

    st.write("""
    • Secure file sharing

    • Client collaboration

    • Document management

    • Remote access to files

    • Improved security and compliance
    """)

    st.subheader("⚙️ How It Works")

    st.write("""
    Users upload files and folders into ShareFile storage locations.

    Files can then be securely shared using permissions, folders,
    user accounts, and secure sharing links.
    """)

    st.subheader("🎫 Common EAST Tickets")

    st.write("""
    • Folder access issues

    • User login issues

    • Permission-related cases

    • File upload failures

    • Shared link issues

    • Sync application issues
    """)

    st.subheader("🔧 Basic Troubleshooting")

    st.write("""
    1. Verify user account status

    2. Confirm permissions

    3. Check folder ownership

    4. Test another browser

    5. Verify service availability

    6. Review recent changes
    """)

    st.subheader("⬆️ When To Escalate")

    st.write("""
    Escalate if:

    • Backend issue is suspected

    • Platform outage exists

    • Data loss is reported

    • Authentication failures continue

    • Administrative intervention is required
    """)

    st.subheader("📚 Useful KBs")

    st.markdown("""
    ### ShareFile Resources

    - [Order Services Published Articles](https://sharefile.lightning.force.com/lightning/o/Knowledge__kav/list?filterName=Copy_of_Published_Articles)
    """)

    st.subheader("🎓 New Hire Learning Path")

    st.write("""
    Week 1
    • Learn ShareFile fundamentals
    • Review key terminology
    • Read ShareFile KB articles

    Week 2
    • Understand common ticket types
    • Learn troubleshooting basics

    Week 3
    • Handle simple access and permission cases
    • Learn escalation paths

    Week 4
    • Review advanced cases
    • Shadow senior engineers
    """)

# MOVEIT

elif selected == "MOVEit":

    st.subheader("📘 What is MOVEit?")

    st.write("""
    MOVEit is a managed file transfer (MFT) solution that securely transfers
    sensitive files between users, systems, and organizations.
    """)

# TELERIK

elif selected == "Telerik":

    st.subheader("📘 What is Telerik?")

    st.write("""
    Telerik provides .NET and JavaScript developer tools, UI controls,
    reporting, and productivity solutions.
    """)

# MARKLOGIC

elif selected == "MarkLogic":

    st.subheader("📘 What is MarkLogic?")

    st.write("""
    MarkLogic is an enterprise database platform used to store and manage
    structured and unstructured data.
    """)

# OPENEDGE

elif selected == "OpenEdge":

    st.subheader("📘 What is OpenEdge?")

    st.write("""
    OpenEdge is an application development platform and database
    for building business applications.
    """)

# LOADMASTER

elif selected == "LoadMaster":

    st.subheader("📘 What is LoadMaster?")

    st.write("""
    LoadMaster is a load balancing solution that improves
    application performance, availability, and security.
    """)

# CHEF

elif selected == "Chef":

    st.subheader("📘 What is Chef?")

    st.write("""
    Chef is an infrastructure automation platform used to configure,
    deploy, and manage servers and applications.
    """)

# FLOWMON

elif selected == "Flowmon":

    st.subheader("📘 What is Flowmon?")

    st.write("""
    Flowmon provides network monitoring, visibility,
    performance analytics, and security insights.
    """)

# WHATSUP GOLD

elif selected == "WhatsUp Gold":

    st.subheader("📘 What is WhatsUp Gold?")

    st.write("""
    WhatsUp Gold is an IT infrastructure monitoring platform
    used for monitoring networks, systems, servers, and applications.
    """)

# ASK EAST AI

st.subheader("🤖 Ask EAST AI")

question = st.text_input("Ask a question")

if question:
    st.info(f"You asked: {question}")
