# Snowflake Intelligence Agent V2  
Self-Directed Reasoning • Multi-Modal RAG • SQL Tooling • Governance Autopilot

The **Snowflake Intelligence Agent V2** is a self-directed, multi-modal AI system that:
- Analyzes structured data (Snowflake tables)
- Reads unstructured content (PDFs, documents)
- Evaluates governance policies using Cortex
- Produces reasoned action traces
- Executes actions through "tools" (SQL, Slack, webhooks, scrapers)

It turns Snowflake into an **autonomous decision layer** — not just a warehouse.

This repository includes:
- Full agent core (planning → execution → summarization)
- A SQL toolbelt (secure SQL generation + execution)
- Document RAG pipeline
- Governance engine using Cortex classification
- Action tools (Slack, webhooks, notifications)
- A Snowflake Notebook demo
- SQL scripts for setting up example datasets & policies



                    ┌───────────────────────────┐
                    │  USER / EXECUTIVE REQUEST │
                    └─────────────┬─────────────┘
                                  ▼
                     ┌────────────────────────┐
                     │   INTELLIGENCE AGENT   │
                     │ (Planning + Reasoning) │
                     └─────────────┬──────────┘
                                   ▼
       ┌──────────────────────────────────────────────────────┐
       │                        TOOLBELT                      │
       │  ┌────────────┬────────────┬────────────┬─────────┐  │
       │  │ SQL Query   │ Doc RAG    │ Policy Eval│ Actions│  │
       │  │ Generator   │ (PDFs/Docs)│ Engine     │ (Slack,│  │
       │  │             │            │            │ Webhooks) │
       │  └────────────┴────────────┴────────────┴─────────┘  │
       └──────────────────────────────────────────────────────┘
                                    ▼
                 ┌──────────────────────────────────────────┐
                 │       GOVERNANCE AUTOPILOT (Cortex)      │
                 │ column sensitivity → tags → row policies │
                 │        document sensitivity scoring      │
                 └──────────────────────────────────────────┘
                                    ▼
                       ┌────────────────────────┐
                       │     ACTION RESULTS     │
                       │   Logs, traces, SLOs   │
                       └────────────────────────┘


## ✨ Features

### 🔍 1. Structured Data Analysis ("What happened?")
- Automatic schema validation  
- Policy-aware SQL generation  
- Chart/table friendly output  
- Full reasoning trace  

---

### 🧠 2. Cross-Domain Reasoning ("Why did it happen?")
- Joins across sales, marketing, inventory, support  
- RAG over staged PDFs (promotions, policies, recalls)  
- Multi-step cause analysis  
- Cortex summarization  

---

### 🕵️ 3. Governance Autopilot ("Who broke the rules?")
Powered by **Snowflake Cortex**  

- Document sensitivity classification  
- Column classification (PII, PCI, HR, Legal, Public)  
- Auto-tagging of Snowflake columns  
- Auto-generation of row-access policies  
- Governance logging  

---

### 🛠️ 4. Custom Tools (Web scrapers, notifications, APIs)
- Slack notifier  
- Email sender  
- HTTP fetcher  
- Python web scraper  
- Extend with any custom tool  

---

### 🔎 5. Full Reasoning Trace
Every run produces:
- Original question  
- Generated plan  
- Tool calls  
- SQL executed  
- Document snippets used  
- Policy evaluations  
- Final summarized answer  

Perfect for enterprise auditability.

---

## 📂 Project Contents

### `/src`
- `agent_core.py` — Main agent interface  
- `planner.py` — Cortex planning + step generation  
- `toolbelt_sql.py` — SQL execution, safety checks  
- `toolbelt_docs.py` — PDF/text embedding + RAG  
- `toolbelt_policies.py` — governance classification + tagging  
- `toolbelt_actions.py` — Slack/email/API actions  
- `utils.py` — shared helpers  

### `/sql`
- `create_demo_objects.sql` — Demo SALES/INVENTORY/SUPPORT tables  
- `sample_governance_policies.sql` — Example tags + row-access policies  

### `/notebooks`
- `intelligence_agent_demo.ipynb` — Full demo notebook  

---

## 🧪 Running the Notebook

1. Open a Snowflake Notebook  
2. Upload the `/src` folder  
3. Install dependencies: Snowpark + Cortex  
4. Run the demo notebook to execute:
   - "What happened?"
   - "Why did it happen?"
   - "Who broke the rules?"

---

## 📝 License
MIT License — feel free to build on this.

---

## ⭐ If this project helps you…
- Star the repo  
- Share your adaptations (finance, supply chain, compliance)  
- Follow Matt on LinkedIn  
- Subscribe to the weekly Data Drift newsletter  
