# TRUST-01 harness
pip install -e ".[test]" && pytest -q                   # rule-based only, no keys
trust01-run --config config.yaml --out runs/rule.jsonl
trust01-analyze runs/rule.jsonl
LLM runs (outside CI, after approval in governance/decision-log.md):
export AIEWA_LLM_BASE_URL=... AIEWA_LLM_API_KEY=... AIEWA_LLM_MODEL=...   # from your environment only; never commit keys
export AIEWA_ALLOW_PAID_CALLS=yes   # OFF by default; set only after Ewa approves the run (nothing paid without her decision)
trust01-run --config config.llm.yaml --out runs/llm.jsonl --allow-llm
The adapter targets any OpenAI-compatible /chat/completions endpoint.
