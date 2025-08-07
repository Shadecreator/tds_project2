# agent_core.py

import os
from openai import AsyncOpenAI
from dotenv import load_dotenv
from code_executor import run_python_code
from validator import validate_output

load_dotenv()
client = AsyncOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")
)

async def process_analysis_task(task: str):
    # 1. Ask GPT to generate code
    prompt = f"""You are an expert data analyst and Python programmer.
Given the task below, create clean and efficient Python code to perform the analysis.

Task description:
{task}

Important:  
- Return only valid Python code implementing the analysis.  
- If plotting is requested, save the plot as a PNG (under 100KB) and encode it as a base64 string to be returned as specified.  
- Do not explain your code or output anything but the code.  
- Follow the output format requirements strictly.
"""
    
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
