import os
from dotenv import load_dotenv
import openai
import openai
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai.chat_models import ChatOpenAI


prompt_template = PromptTemplate(
    input_variables=["original_resume", "job_description"],
    template="""

Based on the following original resume and job description, generate a tailored resume that highlights relevant skills, experiences, and qualifications aligning with the job requirements. Ensure that the tailored resume:

1. Emphasizes key skills and experiences mentioned in the job description.
2. Uses industry-specific keywords from the job description.
3. Rearranges or modifies sections to prioritize the most relevant information.
4. Adjusts the objective or summary statement to reflect the desired role.
5. Includes measurable achievements and specific examples where applicable and make them bold or highlighted.
6. Omits or de-emphasizes less relevant information.
7. Format the final output in crafty and beautiful markdown.

**Original Resume**:
{original_resume}

**Job Description**:
{job_description}

**Tailored Resume**:

"""
)

def get_cv_chain(api_key:str):
    llm = ChatOpenAI(model="gpt-4", api_key=api_key)
    cv_chain = LLMChain(prompt=prompt_template, llm=llm)
    return cv_chain


def craft_resume(original_resume:str, job_description: str, chain: LLMChain):
    try:
        inputs = {"original_resume": original_resume, "job_description": job_description}
        tailored_resume = chain.invoke(inputs)
        return tailored_resume['text']
    except Exception as e:
        return e.__str__()