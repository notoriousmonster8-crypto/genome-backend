from fastapi import APIRouter, UploadFile, File
import tempfile

# 🔹 Variant + Family Pipeline
from services.variant_parser import extract_rsids
from services.variant_engine import compute_variant_risk
from services.family_parser import extract_family_history
from services.risk_fusion import combine_risks

# 🔹 File Processing
from utils.input_detector import detect_input_type
from services.pdf_service import extract_text_from_pdf
from services.vcf_service import parse_vcf
from services.snp_service import parse_snp

# 🔹 Explanation Agent
from agents.explanation_agent import explanation_agent_node

router = APIRouter()


# ============================================
# 🧬 PREDICT (TEXT INPUT)
# ============================================
@router.post("/predict")
def predict(data: dict):
    try:
        genome = data.get("genome", "")
        family = data.get("family_history", "")

        if not genome and not family:
            return {"error": "No input provided"}

        # 🔹 Step 1: Extract rsIDs
        rsids = extract_rsids(genome)
        print("RSIDs:", rsids)

        # 🔹 Step 2: Genetic Risk
        genetic_risk = compute_variant_risk(rsids)
        print("Genetic Risk:", genetic_risk)

        # 🔹 Step 3: Family Risk
        family_data = extract_family_history(family)
        print("Family Data:", family_data)

        # 🔹 Step 4: Combine Risks
        final_risk = combine_risks(genetic_risk, family_data)
        print("Final Risk:", final_risk)

        # 🔹 Step 5: Explanation
        state = {"risks": final_risk}
        state = explanation_agent_node(state)

        return state

    except Exception as e:
        print("PREDICT ERROR:", e)
        return {"error": str(e)}


# ============================================
# 📂 UPLOAD (FILE INPUT)
# ============================================
@router.post("/upload")
async def upload(
    genome_file: UploadFile = File(...),
    family_file: UploadFile = File(None)
):
    try:
        # -------------------------
        # 🧬 GENOME FILE
        # -------------------------
        genome_content = await genome_file.read()
        genome_type = detect_input_type(genome_file.filename.lower())

        if genome_type == "pdf":
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(genome_content)
                genome_text = process_pdf(tmp.name)

        elif genome_type == "vcf":
            genome_text = process_vcf(genome_content.decode(errors="ignore"))

        elif genome_type == "snp":
            genome_text = process_snp(genome_content.decode(errors="ignore"))

        else:
            genome_text = genome_content.decode(errors="ignore")

        # -------------------------
        # 👨‍👩‍👧 FAMILY FILE
        # -------------------------
        family_text = ""

        if family_file:
            family_content = await family_file.read()
            family_type = detect_input_type(family_file.filename.lower())

            if family_type == "pdf":
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                    tmp.write(family_content)
                    family_text = process_pdf(tmp.name)
            else:
                family_text = family_content.decode(errors="ignore")

        # -------------------------
        # 🔥 REUSE SAME LOGIC
        # -------------------------
        result = predict({
            "genome": genome_text,
            "family_history": family_text
        })

        return result

    except Exception as e:
        print("UPLOAD ERROR:", e)
        return {"error": str(e)}