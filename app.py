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
