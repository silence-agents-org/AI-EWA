# SUPERSEDED — kanoniczna wersja: `harness/TRUST_01/trust01/llm.py`; kept, not deleted (deletion only on Ewa's explicit order); map: docs/INDEX.md.
"""Provider-agnostic LLM investor (OpenAI-compatible endpoint). Never used in CI.

Paid API calls are OFF by default. A real network call happens only if ALL of these hold:
1. the run was started with ``--allow-llm`` and ``budget.max_llm_calls > 0`` (see run.py);
2. ``AIEWA_LLM_BASE_URL``, ``AIEWA_LLM_API_KEY`` and ``AIEWA_LLM_MODEL`` are set in the environment
   (keys are never hard-coded or stored in the repository);
3. ``AIEWA_ALLOW_PAID_CALLS=yes`` is set explicitly — only after Ewa's approval is recorded in
   governance/decision-log.md (standing rule: nothing paid without her decision).
"""
from __future__ import annotations

import json
import os
import re
import urllib.request
from dataclasses import dataclass
from typing import Callable, Optional, Tuple

from .engine import GameView

SYSTEM_PROMPT = ("You are a participant in an economic decision study. "
                 "Answer only with the JSON object requested.")
_SEND_RE = re.compile(r'"send"\s*:\s*(-?\d+)')


class LLMConfigError(RuntimeError):
    pass


class ParseFailure(RuntimeError):
    pass


@dataclass
class LLMSettings:
    base_url: str
    api_key: str
    model: str
    temperature: float = 1.0
    max_tokens: int = 50
    timeout: int = 60

    @classmethod
    def from_env(cls, temperature: float = 1.0, max_tokens: int = 50) -> "LLMSettings":
        vals = {k: os.environ.get(f"AIEWA_LLM_{k.upper()}", "") for k in ("base_url", "api_key", "model")}
        missing = [k for k, v in vals.items() if not v]
        if missing:
            raise LLMConfigError(f"missing env vars: {', '.join('AIEWA_LLM_' + m.upper() for m in missing)}")
        return cls(temperature=temperature, max_tokens=max_tokens, **vals)


def render_prompt(view: GameView) -> str:
    p = view.partner_name
    lines = [f"You play a repeated investment game with {p}.",
             f"Each round you receive {view.endowment} points and choose how many to send (0-{view.endowment}).",
             f"Sent points are multiplied by {view.multiplier} and given to {p}, who may return some.",
             f"This is round {view.round_index + 1} of {view.n_rounds}."]
    for h in view.history:
        note = ""
        if h.loss_cause == "partner_choice":
            note = f" {p} chose to return 0."
        elif h.loss_cause == "random_device":
            note = f" A random device, not {p}, set the return to 0."
        lines.append(f"Round {h.round_index + 1}: you sent {h.sent}, you got back {h.returned}.{note}")
    if view.future_rule:
        lines.append(view.future_rule)
    lines.append('Reply with JSON only: {"send": <integer>}')
    return "\n".join(lines)


def parse_send(text: Optional[str], endowment: int = 10) -> Optional[int]:
    m = _SEND_RE.search(text or "")
    if not m:
        return None
    v = int(m.group(1))
    return v if 0 <= v <= endowment else None


def http_transport(settings: LLMSettings, messages: list, seed: int) -> Tuple[str, str]:
    if os.environ.get("AIEWA_ALLOW_PAID_CALLS", "") != "yes":
        raise LLMConfigError("paid API calls are disabled by default; set AIEWA_ALLOW_PAID_CALLS=yes "
                             "only after Ewa's approval is recorded in governance/decision-log.md")
    body = json.dumps({"model": settings.model, "messages": messages,
                       "temperature": settings.temperature, "max_tokens": settings.max_tokens,
                       "seed": seed}).encode()
    req = urllib.request.Request(settings.base_url.rstrip("/") + "/chat/completions", data=body,
                                 headers={"Content-Type": "application/json",
                                          "Authorization": f"Bearer {settings.api_key}"})
    with urllib.request.urlopen(req, timeout=settings.timeout) as resp:
        payload = json.load(resp)
    return payload["choices"][0]["message"]["content"], payload.get("model", settings.model)


class LLMInvestor:
    def __init__(self, settings: LLMSettings, transport: Callable = http_transport,
                 max_retries: int = 2, seed: int = 0, log: Optional[Callable[[dict], None]] = None):
        self.settings, self.transport = settings, transport
        self.max_retries, self.seed = max_retries, seed
        self.log = log or (lambda event: None)
        self.calls = 0

    def decide(self, view: GameView) -> int:
        messages = [{"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": render_prompt(view)}]
        for attempt in range(self.max_retries + 1):
            text, served = self.transport(self.settings, messages, self.seed)
            self.calls += 1
            value = parse_send(text, view.endowment)
            self.log({"event": "llm_call", "round": view.round_index, "attempt": attempt,
                      "raw": text, "served_model": served, "parsed": value})
            if value is not None:
                return value
        raise ParseFailure(f"no valid send after {self.max_retries + 1} attempts")
