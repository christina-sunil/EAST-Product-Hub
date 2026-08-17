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

# Product Knowledge Section

if selected == "ShareFile":

st.subheader("📘 What is ShareFile?")

st.subheader("🌐 Progress Product Portfolio")
st.markdown("""

### Explore Progress Products
 
- [View All Progress Products](https://www.progress.com/products)

ShareFile is part of the Progress Digital Experience portfolio.

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

st.write("""
ShareFile is a secure file sharing and content collaboration platform.
Organizations use it to store, manage, and securely share files with employees,
customers, and business partners.
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
Files can then be securely shared using permissions, user accounts,
folders, and secure sharing links.
""")

st.subheader("🎫 Common EAST Tickets")

st.write("""
    • Folder access issues

    • User login problems

    • Permission-related cases

    • File upload failures

    • Shared link issues

    • Sync application issues
    """)

st.subheader("🔧 Basic Troubleshooting")

st.write("""
    1. Verify user account status

    2. Confirm correct permissions

    3. Check folder ownership

    4. Test in another browser

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

st.subheader("💡 What I've Learned")

    st.write("""
    Add lessons learned from EAST tickets and customer cases here.
    """)

else:

st.subheader("Product Overview")

    st.write(f"""
    Knowledge for {selected} will be added soon.
    """)

# Ask EAST AI Section

st.subheader("Ask EAST AI")

question = st.text_input(
    "Ask a question"
)

if question:
    st.info(f"You asked: {question}")
