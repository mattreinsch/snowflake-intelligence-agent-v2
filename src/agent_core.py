import json
from toolbelt.sql_tools import run_sql
from toolbelt.doc_tools import read_document
from toolbelt.policy_tools import classify_content, apply_governance_policy

class IntelligenceAgent:

    def __init__(self, session=None):
        self.session = session
        self.trace = []

    def log(self, entry):
        self.trace.append(entry)

    def plan(self, query):
        # Cortex-powered planning (placeholder)
        plan = [
            {"step": "analyze_question", "description": "Interpret user intent"},
            {"step": "run_sql", "description": "Pull relevant structured data"},
            {"step": "read_docs", "description": "Augment with documents"},
            {"step": "policy_eval", "description": "Check governance rules"},
            {"step": "summarize", "description": "Produce final answer"}
        ]
        self.log({"plan_generated": plan})
        return plan

    def run_step(self, step):
        if step["step"] == "run_sql":
            result = run_sql(self.session, "SELECT CURRENT_TIMESTAMP;")
            self.log({"sql_result": result})
            return result

        if step["step"] == "read_docs":
            result = read_document("./examples/sample.pdf")
            self.log({"doc_result": result})
            return result

        if step["step"] == "policy_eval":
            label = classify_content("Sample text")
            self.log({"policy_classification": label})
            apply_governance_policy(label)
            return label

    def run(self, query):
        plan = self.plan(query)

        outputs = []
        for step in plan:
            out = self.run_step(step)
            outputs.append(out)

        return {
            "answer": "This is a placeholder response.",
            "trace": self.trace
        }

if __name__ == "__main__":
    agent = IntelligenceAgent()
    resp = agent.run("Why did revenue drop last week?")
    print(json.dumps(resp, indent=2))
