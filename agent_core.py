# agent_core.py

import os
from openai import AsyncOpenAI
from dotenv import load_dotenv
from code_executor import run_generated_code
from validator import validate_output

load_dotenv()
client = AsyncOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")
)

async def handle_task(task: str):
    # 1. Ask GPT to generate code
    prompt = f"""You are a data analyst. Given the task below, write the required Python code.
Task:
{task}

Only output the Python code."""
    
    response = await client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    code = response.choices[0].message.content.strip().removeprefix("```python").removesuffix("```")

    # 2. Execute generated code
    result = run_generated_code(code)

    # 3. Validate + format response
    final_response = await validate_output(task, result)

    return final_response
