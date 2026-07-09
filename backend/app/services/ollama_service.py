import requests


OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL = "qwen2.5:1.5b"

def optimize_with_ollama(prompt: str) -> str:
    instruction = f"""
You are a professional prompt optimization engine.

Transform the user's prompt into a concise and effective AI instruction.

Rules:
1. Remove filler words and unnecessary conversational phrases.
2. Preserve all technical terms.
3. Preserve requirements and constraints.
4. Never remove:
   - environments (production, staging, development)
   - technologies (AWS, Terraform, Kubernetes, Docker)
   - numbers
   - configurations
   - security requirements
   - performance requirements
5. Improve clarity and structure.
6. Reduce unnecessary tokens where possible.
7. Return ONLY the optimized prompt.
8. Do not add explanations.
9. Do not add new information.

User prompt:

{prompt}

Optimized prompt:
"""
    

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": instruction,
            "stream": False
        }
    )

    response.raise_for_status()

    result = response.json()

    return result["response"].strip().strip('"')