from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def evaluate_answer(answer):
    prompt = f"""
    Evaluate this answer on:

    1. Clarity
    2. Leadership
    3. Ownership
    4. Communication
    5. Technical Depth

    Give score out of 10 for each.

    Answer:
    {answer}
    """

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
