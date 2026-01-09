# 🩺 Pediatrics Clinical Note Summarizer — Streamlit App

This Streamlit app surfaces your fine‑tuned **Pediatrics** model from Milestone 3. 
Paste the **fine‑tuned model ID** and enter a short pediatric visit description; the app returns a structured SOAP‑style note.

## Requirements
- Python 3.10+
- OpenAI API key with access to your fine‑tuned model
- Fine‑tuned model ID (e.g., `ft:gpt-4o-mini-2024-07-18:org:custom:peds-notes-v1`)

## Run
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

pip install -r requirements.txt

# Set API key (PowerShell)
setx OPENAI_API_KEY "sk-REPLACE_ME"
# Or bash
# export OPENAI_API_KEY="sk-REPLACE_ME"

streamlit run streamlit_app.py
```


## Notes
The included PHI redaction is **naive** and for demo only.
