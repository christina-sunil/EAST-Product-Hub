import streamlit as st

st.set_page_config(
    page_title="EAST Product Hub",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 EAST Product Hub")

st.write("Welcome to the EAST Product Hub")

selected = st.selectbox(
    "Select Product",
    [
        "ShareFile",
        "MOVEit"
    ]
)

st.success(f"Selected Product: {selected}")

# =====================================================
# SHAREFILE
# =====================================================

if selected == "ShareFile":

    st.header("📘 ShareFile")

    st.subheader("What is ShareFile?")

    st.write("""
    ShareFile is a secure file sharing and content collaboration platform.
    Organizations use it to securely store, manage, and share documents
    with employees, customers, and partners.
    """)

    st.subheader("🧩 ShareFile Features")

    st.write("""
    • Secure File Sharing

    • Client Portal

    • Document Storage

    • Workflow Automation

    • Electronic Signatures

    • User Management

    • Folder Permissions

    • Secure Sharing Links

    • Mobile Access

    • File Sync
    """)

    st.subheader("🎯 Why Customers Use ShareFile")

    st.write("""
    • Secure collaboration

    • Share files externally

    • Manage documents

    • Improve customer experience

    • Meet security requirements
    """)

    st.subheader("🎫 Common EAST Tickets")

    st.write("""
    • User access issues

    • Folder permission problems

    • Login failures

    • Upload failures

    • Shared link issues

    • Sync issues
    """)

    st.subheader("🔧 Basic Troubleshooting")

    st.write("""
    1. Verify user account

    2. Check folder permissions

    3. Confirm group membership

    4. Test another browser

    5. Verify service availability
    """)

    st.subheader("📚 Knowledge Base")

    st.markdown("""
    - [ShareFile Knowledge Articles](https://sharefile.lightning.force.com/lightning/o/Knowledge__kav/list?filterName=Copy_of_Published_Articles)
    """)

    st.subheader("🎓 New Hire Learning Path")

    st.write("""
    Week 1
    • Learn ShareFile basics

    Week 2
    • Review common tickets

    Week 3
    • Handle basic cases

    Week 4
    • Learn escalation paths
    """)

# =====================================================
# MOVEIT
# =====================================================

elif selected == "MOVEit":

    st.header("📘 MOVEit")

    st.subheader("What is MOVEit?")

    st.write("""
    MOVEit is a Managed File Transfer (MFT) solution that securely transfers
    sensitive files between systems, organizations, and users.
    """)

    st.subheader("🧩 MOVEit Features")

    st.write("""
    • Secure File Transfer

    • Transfer Automation

    • Encryption

    • Compliance Reporting

    • Audit Logs

    • Role-Based Access

    • Workflow Automation

    • Scheduled Transfers

    • Secure External Transfer
    """)

    st.subheader("🎯 Why Customers Use MOVEit")

    st.write("""
    • Secure sensitive data

    • Meet compliance requirements

    • Automate transfers

    • Reduce manual work

    • Improve reliability
    """)

    st.subheader("🏗️ MOVEit Components")

    st.write("""
    • MOVEit Transfer

    • MOVEit Automation

    • Users & Groups

    • Hosts

    • Secure Folders

    • Transfer Tasks

    • Audit Logs
    """)

    st.subheader("🎫 Common EAST Tickets")

    st.write("""
    • Failed file transfers

    • User access issues

    • Authentication failures

    • Certificate problems

    • Task failures

    • Connectivity issues
    """)

    st.subheader("🔧 Basic Troubleshooting")

    st.write("""
    1. Check logs

    2. Verify credentials

    3. Check connectivity

    4. Verify certificates

    5. Review automation tasks
    """)

    st.subheader("📚 Knowledge Base")

    st.write("""
    Add MOVEit KB links here.
    """)

    st.subheader("🎓 New Hire Learning Path")

    st.write("""
    Week 1
    • Learn MOVEit fundamentals

    Week 2
    • Understand Transfer & Automation

    Week 3
    • Troubleshoot common issues

    Week 4
    • Learn escalation guidelines
    """)

# =====================================================
# ASK EAST AI
# =====================================================

st.header("🤖 Ask EAST AI")

question = st.text_input("Ask a question")

if question:
    st.info(f"You asked: {question}")

st.subheader("🎓 New Hire Learning Path")

st.write("""

Week 1

...

Week 4

...
""")

# =====================================================
12
# OPENEDGE
13
# =====================================================

elif selected == "OpenEdge":

st.header("🖥️ OpenEdge")

st.subheader("What is OpenEdge?")

st.write(""
OpenEdge is Progress Software's application development platform
and database used to build, deploy, and manage business-critical
applications.
""")

st.subheader("🧩 OpenEdge Features")
st.write("""

• Application Development

• Relational Database

• Business Logic Processing

• Secure Data Management

• Scalability

