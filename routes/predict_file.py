from fastapi import APIRouter, UploadFile, File
import tempfile

from utils.input_detector import detect_input_type
from services.pdf_service import extract_text_from_pdf
from services.vcf_service import parse_vcf
from services.snp_service import parse_snp
from routes.predict import predict
router = APIRouter()

@router.post("/predict-file")
async def predict_file(file: UploadFile = File(...)):
    content = await file.read()

    try:
        # 🔥 Detect file type safely
        file_type = detect_input_type(file.filename.lower())

        # 🔹 PDF handling
        if file_type == "pdf":
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(content)
                tmp_path = tmp.name

            text = process_pdf(tmp_path)

        # 🔹 VCF handling
        elif file_type == "vcf":
            text = process_vcf(content.decode(errors="ignore"))

        # 🔹 SNP handling
        elif file_type == "snp":
            text = process_snp(content.decode(errors="ignore"))

        # 🔹 Default (txt/csv)
        else:
            text = content.decode(errors="ignore")

        # 🔥 Run prediction
        result = predict_from_text(text)

        return result

    except Exception as e:
        print("FILE ERROR:", e)
        return {"error": str(e)}