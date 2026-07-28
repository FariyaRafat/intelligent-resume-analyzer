import json
import re
from google import genai
from dotenv import load_dotenv
import os
import pdfplumber
from docx import Document

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)


def extract_text_from_resume(filepath, ext):
    text = ""

    if ext == "pdf":
        with pdfplumber.open(filepath) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

    elif ext in ("docx", "doc"):
        doc = Document(filepath)
        for para in doc.paragraphs:
            text += para.text + "\n"

    return text.strip()


def analyze_resume(resume_text, role, job_description):
    prompt = f"""
You are an expert ATS analyzer.

Return ONLY valid JSON.

Target Role:
{role}

Job Description:
{job_description}

Resume:
{resume_text}

Return JSON:
{{
  "ats_score": 0,
  "score_breakdown": {{
    "keyword_match": 0,
    "skills_relevance": 0,
    "experience_match": 0,
    "formatting_quality": 0,
    "education_match": 0
  }},
  "missing_keywords": [],
  "matched_keywords": [],
  "section_analysis": {{
    "contact_info": {{"status":"good","issues":[],"suggestions":[]}},
    "professional_summary": {{"status":"good","issues":[],"suggestions":[]}},
    "skills": {{"status":"good","issues":[],"suggestions":[],"missing_skills":[]}},
    "work_experience": {{"status":"good","issues":[],"suggestions":[]}},
    "education": {{"status":"good","issues":[],"suggestions":[]}},
    "projects": {{"status":"good","issues":[],"suggestions":[]}},
    "certifications": {{"status":"good","issues":[],"suggestions":[]}}
  }},
  "grammar_errors": [],
  "overall_recommendation": "",
  "strengths": [],
  "weaknesses": []
}}
"""

    try:
        response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt,
    )

        result_text = response.text.strip()

        result_text = re.sub(
            r"^```json\s*|\s*```$",
            "",
            result_text,
            flags=re.MULTILINE,
        )

        return json.loads(result_text)

    except json.JSONDecodeError as e:
        return {
            "error": "JSON parse failed",
            "details": str(e)
        }

    except Exception as e:
        return {
            "error": "Gemini API error",
            "details": str(e)
        }

    