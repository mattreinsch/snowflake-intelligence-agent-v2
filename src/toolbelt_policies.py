from snowflake.cortex import complete

def evaluate_policies(session, table: str):
    classification_prompt = f"Classify sensitivity for table {table}. Return label only."

    label = complete(
        model="llama3.1-8b",
        prompt=classification_prompt
    ).text.strip()

    sql = f"ALTER TABLE {table} ADD TAG classification = '{label}';"

    try:
        session.sql(sql).collect()
        return {"label": label, "tag_applied": sql}
    except Exception as e:
        return {"error": str(e)}
