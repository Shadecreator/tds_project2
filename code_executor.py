# code_executor.py

import io
import contextlib

def run_python_code(code: str) -> str:
    output = io.StringIO()
    try:
        with contextlib.redirect_stdout(output):
            exec(code, {})
        return output.getvalue()
    except Exception as e:
        return f"[ERROR] {str(e)}"
