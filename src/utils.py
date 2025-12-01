import datetime

def log_event(event_type: str, payload: dict):
    print(f"[{datetime.datetime.utcnow()}] {event_type}: {payload}")
