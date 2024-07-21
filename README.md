# Tailored CV for Jobs

**Course:** OMC207 Mini Project, Second Semester MCA
**NOTE**: This branch uses `Bring Your Own Key`.
## Overview

The **Resume Tailoring Application** is a Streamlit-based tool designed to help users customize their resumes to match specific job descriptions. By leveraging the capabilities of the GPT-4o model, this application ensures that resumes are tailored to highlight relevant skills, experiences, and qualifications as per the job requirements, thus enhancing the chances of success in job applications.

## Introduction

This project is part of the OMC207 Mini Project for the second semester of the MCA program. The main objective is to develop an application that assists users in tailoring their resumes according to specific job descriptions, making them more relevant and appealing to potential employers.


## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Core Functions](#core-functions)
6. [Streamlit Integration](#streamlit-integration)
7. [Testing and Deployment](#testing-and-deployment)
8. [References](#references)


### Project Summary

1. **Table of Contents:**
    - Chapter 1: Introduction and Overview
    - Chapter 2: User Input Interface
    - Chapter 3: Core Functions and Logic
    - Chapter 4: Integration with Streamlit
    - Chapter 5: Testing and Deployment
    - References

2. **Chapter 1: Introduction and Overview**
    - **Introduction (1.1):** Overview of the resume tailoring application and its purpose.
    - **Problem Statement (1.2):** The need for customizing resumes to match specific job descriptions to improve job application success rates.

3. **Chapter 2: User Input Interface**
    - **User Input Fields (2.1):** Details on the text areas provided for job description and original resume inputs.
    - **User Experience Design (2.2):** Explanation of the design choices to enhance user experience.

4. **Chapter 3: Core Functions and Logic**
    - **Function Definitions (3.1):** Detailed explanation of the `get_cv_chain` and `craft_resume` functions.
        - **get_cv_chain Function (3.1.1):** Initializes the LLMChain with the provided API key.
        - **craft_resume Function (3.1.2):** Crafts a tailored resume based on the inputs provided.
    - **Error Handling (3.2):** How the functions manage errors and exceptions.

5. **Chapter 4: Integration with Streamlit**
    - **Streamlit Setup (4.1):** Step-by-step process of setting up the Streamlit application.
    - **User Interface Components (4.2):** Description of the UI components used in Streamlit (buttons, text areas, etc.).
    - **Function Invocation (4.3):** How the functions are called within the Streamlit app.
    - **Displaying Results (4.4):** How the tailored resume is displayed to the user.

6. **Chapter 5: Testing and Deployment**
    - **Testing (5.1):** Methods for testing the functionality and performance of the application.
    - **Deployment (5.2):** Steps for deploying the application using Streamlit.

7. **References**
    - Listing of references and resources used in the development of the project, including documentation for Streamlit, Langchain, OpenAI API, and any other relevant sources.

## Features

- User-friendly interface for inputting job descriptions and original resumes.
- Utilizes GPT-4 to generate tailored resumes.
- Emphasizes relevant skills and experiences based on the job description.
- Provides an easy way to customize and refine resumes for different job applications.

## Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/ideepankarsharma2003/TailoredCVforJobs.git
    cd TailoredCVforJobs
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```


## Usage

1. **Run the Streamlit App:**
    ```bash
    streamlit run app.py
    ```

2. **Input Details:**
    - Paste the job description into the "Job Description" text area.
    - Paste your original resume into the "Original Resume" text area.
    - Click the "Tailor Resume" button to generate the tailored resume.

3. **View Results:**
    - The tailored resume will be displayed in the text area below the input fields.

## Core Functions

### get_cv_chain

This function initializes the `LLMChain` with the provided API key, using the GPT-4 model to tailor resumes.

### craft_resume

This function takes the original resume and job description as inputs, uses the `LLMChain` to generate a tailored resume, and handles any errors that may occur during the process.

## Streamlit Integration

The Streamlit app provides a simple and interactive interface for users to input their resumes and job descriptions. It leverages the core functions to generate and display tailored resumes.

### Streamlit Setup

- Input fields for job description and original resume.
- Button to trigger the tailoring process.
- Display area for the tailored resume.

## Testing and Deployment

### Testing

- Ensure the application works as expected by inputting various resumes and job descriptions.
- Verify the tailored resumes are relevant and well-structured.

### Deployment

- Deploy the application using Streamlit's sharing platform or other cloud services like Heroku or AWS.

## References

- [Streamlit Documentation](https://docs.streamlit.io/)
- [OpenAI API Documentation](https://beta.openai.com/docs/)
- [Langchain Documentation](https://langchain.readthedocs.io/)
