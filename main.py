from fastapi import FastAPI
from routes.api import router
from routes.history import router as history_router
from auth.auth_routes import router as auth_router
from database.models import Base
from database.db import engine
from fastapi.middleware.cors import CORSMiddleware
from routes.chat import router as chat_router
from dotenv import load_dotenv
import os
from routes.predict_file import router as predict_file_router

load_dotenv()

print("LOADED KEY:", os.getenv("GEMINI_API_KEY"))
app = FastAPI()
Base.metadata.create_all(bind=engine)
# CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(router)
app.include_router(history_router)
app.include_router(auth_router)
app.include_router(chat_router)
app.include_router(predict_file_router)
@app.get("/")
def root():
    return {"message": "Genome API running"}