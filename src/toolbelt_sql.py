def run_sql(session, sql: str):
    try:
        df = session.sql(sql).collect()
        return {"rows": df}
    except Exception as e:
        return {"error": str(e), "sql": sql}
