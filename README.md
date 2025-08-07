# My Data Analyst Agent

This project is an intelligent data analyst agent API that accepts analysis tasks, data files, and returns answers—including computations, correlations, and base64-encoded plots.

## Features

- Upload a `questions.txt` file describing your analysis questions.
- Optional attachments like CSVs, images, or JSON data.
- Automatic parsing of tasks and generating Python code to perform data analysis.
- Secure execution of generated code in a sandbox environment.
- Returns answers in structured JSON and plots as base64 PNG images (<100KB).
- Deployed as a REST API using FastAPI.

## Setup

1. Clone the repository:
```
git clone https://github.com/yourusername/my-data-analyst-agent.git
cd my-data-analyst-agent
```

2. Create a virtual environment and install dependencies:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Set your environment variables in `.env`:
```
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_BASE_URL=https://aipipe.org/openai/v1  # optional
```

## Running Locally

Start the FastAPI server:

```
uvicorn app:app --reload
```

API will be available at `http://localhost:8000/api/`.

## Usage

Make a POST request with `questions.txt` and optional data files.

Example `curl` command:

```
curl -X POST "http://localhost:8000/api/" \
  -F "questions.txt=@questions.txt" \
  -F "data.csv=@data.csv"
```

Response will be a JSON array or object with answers and base64-encoded plots where applicable.

## Deployment

- Deploy your app on platforms like Render, Railway, Heroku, or your own server.
- Ensure environment variables are set securely.
- Verify endpoint accessibility before submission.

## Customizations and Improvements

- Customized GPT prompt to match project style and output requirements.
- Added enhanced error handling and code execution logging.
- Extended plotting options and output validation.

---

## 3. Documentation Tips

- Add a `docs/` folder with usage examples.
- Write sample input files and the expected output files.
- Document your internal modules and functions with docstrings.
- Maintain a changelog of your modifications vs. original repo.

