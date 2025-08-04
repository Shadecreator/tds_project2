# validator.py

import os
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()
client = AsyncOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")
)

async def validate_output(task, output):
    prompt = f"""
Task:
{task}

The following output was produced by a data agent:

{output}

Check if it answers the question correctly. If not, fix and format it as a JSON array or object as needed. If plots are included, ensure they're base64 encoded.
"""
    response = await client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content
