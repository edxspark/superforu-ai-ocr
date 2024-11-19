#!/usr/bin/venv python
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI, UploadFile, File, Form
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

load_dotenv()
STORAGE_PATH = os.getenv("STORAGE_PATH")

app = FastAPI(
    title="AI-VL-OCR",
    version="1.0",
    description="SGIT AI Invoice",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Upload file
@app.post("/ai/vl/ocr")
def ai_vl_ocr(file: UploadFile = File(...)):
    return "OK"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=6006)