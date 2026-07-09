from pydantic import BaseModel


class PromptRequest(BaseModel):
    prompt: str


class PromptResponse(BaseModel):
    optimized_prompt: str
    original_length: int
    optimized_length: int
    token_reduction_percentage: float