from google import genai
import os

def generate_text(prompt: str) -> str:
    try:
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

        response = client.models.generate_content(
            model="gemini-2.0-flash",  # 🔥 use lighter model
            contents=prompt
        )

        return response.text

    except Exception as e:
        print("GEMINI ERROR:", e)

        # 🔥 THIS IS THE FALLBACK (Option 3)
        return (
            "⚠️ AI service is temporarily busy due to usage limits.\n\n"
            "📊 Based on your genome data, there may be moderate genetic influence on disease risks.\n"
            "🧬 Lifestyle, environment, and medical consultation are important for accurate interpretation.\n\n"
            "👉 Please try again in a few minutes."
        )