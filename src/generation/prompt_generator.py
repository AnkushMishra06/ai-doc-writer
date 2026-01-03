from typing import Dict
from pathlib import Path
from google import genai
from google.genai import types

client = genai.Client()

PROMPT_TEMPLATE_PATH = Path("docs/prompt_template.md")

def build_prompt(sample: Dict) -> str:
    template = load_prompt_template()

    prompt = template.format(
        entity_type = sample.get("code_entity_type", ""),
        entity_name = sample.get("entity_name", ""),
        signature = sample.get("entity_name", ""),
        parameters = ", ".join(sample.get("parameters", [])),
        return_type = sample.get("return_type", ""),
        code_block = sample.get("code_block", "")
    )
    return prompt

def call_llm(prompt: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        config = types.GenerateContentConfig(thinking_config=types.ThinkingConfig(thinking_budget=0), temperature=0.2, max_output_tokens=300),
        contents=prompt
    )
    return response.text.strip()

def load_prompt_template() -> str:
    if not PROMPT_TEMPLATE_PATH.exists():
        raise FileNotFoundError(f"Prompt template file not found: {PROMPT_TEMPLATE_PATH}")
    return PROMPT_TEMPLATE_PATH.read_text(encoding="utf-8")

def generate_docstring_with_prompt(sample: Dict) -> str:
    prompt = build_prompt(sample)
    return call_llm(prompt)