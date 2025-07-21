import os
import streamlit as st
from scripts import craft_resume_streaming

# Determine environment
ENV = os.getenv("ENV", "prod")  # Default to "prod" if not set

# Sidebar for BYOK if not in dev mode
if ENV == "dev":
    openai_api_key = os.getenv("OPENAI_API_KEY")
    st.sidebar.success("Running in DEV mode (using .env key)")
else:
    st.sidebar.header("🔑 OpenAI API Key (BYOK)")
    openai_api_key = st.sidebar.text_input("Enter your OpenAI API key:", type="password")
    if openai_api_key:
        st.sidebar.success("API key loaded successfully!")
    else:
        st.sidebar.warning("Please enter your OpenAI API key to proceed.")

st.title("Resume Tailoring Application")
st.write("This app will tailor your resume according to the job description you provide.")

job_description = st.text_area("Job Description", height=200, placeholder="Paste the job description here...")
original_resume = st.text_area("Original Resume", height=400, placeholder="Paste your original resume here...")

if st.button("Tailor Resume"):
    if not openai_api_key:
        st.error("❌ API key missing! Please set it in the sidebar.")
    elif job_description and original_resume:
        st.subheader("Tailored Resume")
        tailored_resume_placeholder = st.empty()
        full_resume = ""

        with st.spinner("Tailoring your resume..."):
            for chunk in craft_resume_streaming(original_resume, job_description, openai_api_key):
                full_resume += chunk
                tailored_resume_placeholder.markdown(full_resume, unsafe_allow_html=True)

        st.success("✅ Resume tailored successfully!")
    else:
        st.warning("Please provide both a job description and your original resume.")
