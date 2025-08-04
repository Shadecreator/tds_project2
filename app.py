# app.py

from fastapi import FastAPI, UploadFile, File
from agent_core import handle_task

app = FastAPI()

@app.post("/api/")
async def analyze(file: UploadFile = File(...)):
    content = (await file.read()).decode()
    result = await handle_task(content)
    return {"response": result}
