import streamlit as st
from scripts import get_cv_chain, craft_resume  



st.title("Resume Tailoring Application")

st.write("This app will tailor your resume according to the job description you provide.")


job_description = st.text_area("Job Description", height=200, placeholder="Paste the job description here...")
original_resume = st.text_area("Original Resume", height=400, placeholder="Paste your original resume here...")
api_key= st.sidebar.text_input("OpenAi API key")

if st.button("Tailor Resume"):
    if job_description and original_resume and api_key:
        cv_chain = get_cv_chain(api_key)
        with st.spinner("Tailoring your resume..."):
            tailored_resume = craft_resume(original_resume, job_description, cv_chain)
            if isinstance(tailored_resume, str):
                st.subheader("Tailored Resume")
                st.markdown(tailored_resume)
            else:
                st.error("An error occurred while tailoring your resume. Please try again.")
    elif not api_key:
        st.warning("Please enter the OpenAI API key.")
    else:
        st.warning("Please provide both a job description and your original resume.")
