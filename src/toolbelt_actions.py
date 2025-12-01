import requests
import os

SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK_URL")

def run_action(action: str, params: dict):
    if action == "send_slack":
        return _send_slack(params["message"])
    return {"error": "Unknown action"}

def _send_slack(message: str):
    if not SLACK_WEBHOOK:
        return {"error": "No Slack webhook configured"}
    response = requests.post(SLACK_WEBHOOK, json={"text": message})
    return {"status": response.status_code}
