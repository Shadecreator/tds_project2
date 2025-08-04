
# 🤖 Data Analyst Agent API

A powerful FastAPI application that acts like a **Data Analyst Agent**, capable of:

- Accepting natural language prompts (from `.txt` files)
- Analyzing **text or image files**
- Scraping and processing data
- Running Python code dynamically
- Generating plots
- Returning JSON/text answers in seconds

---

## 🚀 Features

✅ Accepts `.txt` or image (`.png`, `.jpg`) files  
✅ Supports any file name (not limited to `question.txt`)  
✅ Automatically understands the task and handles it end-to-end  
✅ Generates base64 plots under 100KB for image responses  
✅ Uses OpenAI LLMs for planning, validation, and reasoning  
✅ Modular, clean architecture (easy to scale and debug)  

---

## 🧠 How It Works

The app uses LLMs (like GPT-4) to **parse your question**, **plan steps**, and **run analysis**.

### ✨ Flow:

1. **User uploads a file** (can be a `.txt` task or an image chart)
2. `app.py` handles the upload and routes to `handle_task()`
3. `agent_core.py`:
   - Reads the question (text or image)
   - Decides what actions to take
   - Calls scraping, code execution, and analysis tools
4. **Image files** are processed via `image_encoder.py` using Vision LLMs
5. **Python code** is generated and safely executed by `code_executor.py`
6. Final result is validated by `validator.py` for format correctness
7. Response is returned as JSON or list of answers + plot (base64-encoded)

---

## 📁 Folder Structure

```

.
├── .env                  # Environment file with OpenAI/AIPipe keys
├── agent_core.py         # Main logic for task planning and orchestration
├── app.py                # FastAPI entry point
├── code_executor.py      # Safely executes generated Python code
├── image_encoder.py      # Handles image input + OCR + Vision GPT
├── question.txt          # Sample input file (can be any .txt file)
├── question_2.txt        # Another sample
├── README.md             # Project documentation
├── requirements.txt      # Python packages
├── validator.py          # Validates LLM-generated responses
└── **pycache**/          # Python cache folder

````

---

## ⚙️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/VS-Abhijith/data-analyst-agent.git
cd data-analyst-agent
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set your environment variables

Create a `.env` file:

```
OPENAI_API_KEY=your_key_here
OPENAI_BASE_URL=https://aipipe.org/openai/v1  # optional if using AIPipe
```

### 4. Start the server

```bash
uvicorn app:app --reload
```

---

## 📤 Example Usage

### Upload a `.txt` file:

```bash
curl -X POST http://127.0.0.1:8000/api/ -F "file=@mytask.txt"
```

### Upload an image:

```bash
curl -X POST http://127.0.0.1:8000/api/ -F "file=@myplot.png"
```

🟢 You can upload any file name. Output is automatically structured.

---

## 🔍 Example Output (Text Request)

```json
{
  "response": [
    1,
    "Titanic",
    0.485782,
    "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA..."
  ]
}
```

---

## 👨‍💻 Author

* GitHub: [VS-Abhijith](https://github.com/VS-Abhijith)
* LinkedIn: [Abhijith VS](https://www.linkedin.com/in/vsabhijith)

---

## 📜 License

This project is licensed under the **MIT License**.