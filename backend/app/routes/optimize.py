from fastapi import APIRouter, HTTPException

from app.models.prompt import (
    PromptRequest,
    PromptResponse
)

from app.services.ollama_service import (
    optimize_with_ollama
)


router = APIRouter()


@router.post("/optimize", response_model=PromptResponse)
def optimize_prompt(request: PromptRequest):

    try:

        optimized = optimize_with_ollama(
            request.prompt
        )

        original_length = len(
            request.prompt.split()
        )

        optimized_length = len(
            optimized.split()
        )

        if original_length > 0:
            token_reduction_percentage = (
                (original_length - optimized_length)
                / original_length
            ) * 100
        else:
            token_reduction_percentage = 0


        return PromptResponse(
            optimized_prompt=optimized,
            original_length=original_length,
            optimized_length=optimized_length,
            token_reduction_percentage=round(
                token_reduction_percentage,
                2
            )
        )


    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )