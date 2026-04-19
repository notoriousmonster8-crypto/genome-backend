from fastapi import APIRouter, UploadFile, File
from agents.graph import build_graph
from database.db import SessionLocal
from database.models import History
import json

router = APIRouter()
graph = build_graph()

@router.post("/predict")
async def predict(data: dict):
    result = graph.invoke({"input": data["genome"]})

    # Save history
    db = SessionLocal()
    record = History(
        genome=data["genome"],
        result=json.dumps(result)
    )
    db.add(record)
    db.commit()

    return result

from services.pdf_service import extract_text_from_pdf

@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    content = await file.read()

    if file.filename.endswith(".pdf"):
        with open("temp.pdf", "wb") as f:
            f.write(content)

        text = extract_text_from_pdf("temp.pdf")

        # Simple mapping → convert medical text to pseudo genome
        genome = "".join([
            "G" if "high" in text.lower() else "A",
            "C" if "risk" in text.lower() else "T"
        ]) * 50

    else:
        genome = content.decode()

    return {"genome": genome}