from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def mentor_tip(question, answer):
    prompt = f"""
    Interview Question:
    {question}

    Candidate Answer:
    {answer}

    Give short hidden coaching tips.
    Suggest STAR method if useful.
    Keep it concise.
    """

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
