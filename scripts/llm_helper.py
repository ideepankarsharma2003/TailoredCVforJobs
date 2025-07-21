import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def craft_resume_streaming(original_resume: str, job_description: str, api_key: str):
    client = OpenAI(api_key=api_key)

    prompt = f"""
Based on the following original resume and job description, generate a tailored resume that highlights relevant skills, experiences, and qualifications aligning with the job requirements. Ensure that the tailored resume:

1. Emphasizes key skills and experiences mentioned in the job description.
2. Uses industry-specific keywords from the job description.
3. Rearranges or modifies sections to prioritize the most relevant information.
4. Adjusts the objective or summary statement to reflect the desired role.
5. Includes measurable achievements and specific examples where applicable and make them **bold**.
6. Omits or de-emphasizes less relevant information.
7. Format the final output in **crafty and beautiful markdown**.

**Original Resume**:
{original_resume}

**Job Description**:
{job_description}

**Tailored Resume**:
"""

    stream = client.chat.completions.create(
        model="gpt-4o-mini",  # Or "gpt-4o" for better quality
        messages=[
            {"role": "system", "content": "You are an expert resume writer and career coach."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        stream=True
    )

    for chunk in stream:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content
