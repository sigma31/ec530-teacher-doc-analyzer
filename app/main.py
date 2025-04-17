from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as api_router
from app.core.config import settings

app = FastAPI(
    title="Teacher Grading Assistant",
    description="An API tool for grading student answers using LLMs",
    version="0.1.0",
)

# CORS setup (useful for frontend integration or testing)
# Recommended for development so that broswers don't block requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Edit this in final build
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API endpoints
app.include_router(api_router, prefix="/api")

# Health check
@app.get("/")
def read_root():
    return {"message": "Teacher Grading Assistant API is running!"}
