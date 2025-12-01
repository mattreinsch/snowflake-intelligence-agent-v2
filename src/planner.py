from snowflake.cortex import complete

SYSTEM_PROMPT = """
You are an enterprise-grade planning agent.
Your job: break down the user query into tool-based steps.
Use only these tools:
- run_sql
- doc_rag
- policy_eval
- action

Return a JSON list of steps.
"""

def generate_plan(query: str):
    prompt = f"{SYSTEM_PROMPT}\n\nUser Query:\n{query}\n\nReturn ONLY JSON."

    result = complete(
        model="llama3.1-8b",
        prompt=prompt
    )

    return result.json()
