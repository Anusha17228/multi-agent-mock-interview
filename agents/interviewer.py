from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_question(company, role, resume):
    prompt = f"""
    You are a senior interviewer at {company}.

    Candidate role:
    {role}

    Candidate resume:
    {resume}

    Ask ONE realistic and difficult interview question.
    """

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
