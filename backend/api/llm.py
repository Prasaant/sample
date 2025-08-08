"""Simple placeholder for a custom LLM.
In a real application this would load a trained model.
"""

def generate_response(prompt: str, session_id: str | None = None) -> str:
    return f"Echo: {prompt}"
