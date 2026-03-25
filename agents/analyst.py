from utils.mistral_client import call_mistral
from utils.code_runner import run_code

def analyze_data(df, question):
    prompt = f"""
You are a Python data analyst.

STRICT RULES:
- Return ONLY valid Python code
- NO explanations
- NO markdown (no ``` )
- NO comments
- Use only existing columns in dataframe
- DataFrame name is: df
- Store final output in variable: result

Dataset columns:
{list(df.columns)}

Question:
{question}
"""

    code = call_mistral(prompt)

    print("\n🧠 RAW OUTPUT:\n", code)

    output = run_code(code, df)

    return output