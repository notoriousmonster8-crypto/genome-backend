import google.generativeai as genai
import os
import time
key = os.getenv("GEMINI_API_KEY")
print("USING GEMINI KEY:", key)

genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-2.5-flash")

def generate_text(prompt: str):
    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        print("GEMINI ERROR:", e)

        # 🔥 Retry once (quota often resets quickly)
        try:
            time.sleep(5)
            response = model.generate_content(prompt)
            return response.text
        except Exception as e2:
            print("GEMINI RETRY FAILED:", e2)

            # 🔥 Fallback (VERY IMPORTANT)
            return """
            AI explanation temporarily unavailable due to API limits.

            Based on your genome:
            - Higher risk values indicate stronger genetic influence
            - Lower values indicate weaker association

            Please try again later.
            """