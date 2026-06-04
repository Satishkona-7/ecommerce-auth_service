from fastapi import FastAPI

from app.routes.auth_routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Auth Service"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/api/auth/health")
def health():

    return {
        "status": "UP"
    }