def clean_code(code):
    # remove markdown if model still sends it
    code = code.replace("```python", "").replace("```", "")
    return code.strip()


def run_code(code, df):
    code = clean_code(code)

    local_vars = {"df": df}

    try:
        exec(code, {}, local_vars)
        return local_vars.get("result", "No result returned")
    except Exception as e:
        return f"Error: {str(e)}"