from fastapi import FastAPI
from app.routes.optimize import router as optimize_router

app = FastAPI(
    title="Prompt Optimizer API",
    version="1.0.0"
)


@app.get("/")
def health_check():
    return {
        "status": "running",
        "service": "prompt optimizer"
    }


app.include_router(
    optimize_router,
    prefix="/api"
)