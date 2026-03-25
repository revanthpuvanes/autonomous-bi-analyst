from utils.mistral_client import call_mistral

def generate_report(question, analysis):
    prompt = f"""
You are a business analyst.

STRICT RULES:
- Use ONLY the provided analysis
- Do NOT invent reasons
- Do NOT assume missing data
- If reason is unknown, say "insufficient data"

Question: {question}
Analysis result: {analysis}

Output:
- Key finding
- Reason (ONLY if supported)
- Recommendation
"""

    return call_mistral(prompt)