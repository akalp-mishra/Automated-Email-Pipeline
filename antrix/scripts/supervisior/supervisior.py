import requests
from .helper import extract_score, extract_feedback, extract_verdict, extract_brochure, extract_email
from ...prompts.mixed import supervisior_prompt

def call_ai_supervisor(company, email, brochure):
    """Call AI supervisor for content review."""
    try:
        prompt = supervisior_prompt.format(
            company_name=company,
            email_output=email,
            brochure_output=brochure
        )

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi3-supervisor",
                "prompt": prompt,
                "stream": False
            },
            timeout=60  # Increased timeout to 60 seconds for Ollama
        )
        response.raise_for_status()
        return response.json().get("response", "")
    except requests.exceptions.Timeout:
        print(f"Warning: Supervisor AI timeout (Ollama may not be running)")
        return ""
    except requests.exceptions.RequestException as e:
        print(f"Warning: Supervisor AI unavailable: {e}")
        return ""

def supervisor_check(company, email, brochure, retries):

    if company.lower() not in email.lower():
        return {"status": "retry", "score": 0, "feedback": "Missing company name"}
    
    review = call_ai_supervisor(company, email, brochure)

    score= extract_score(review)
    feedback = extract_feedback(review)
    verdict = extract_verdict(review)
    email_output = extract_email(review)
    brochure_output = extract_brochure(review)

    if score >= 8:
        return {
            "status": "approved",
            "score": score,
            "feedback": feedback
        }

    elif retries < 2:
        return {
            "status": "retry",
            "score": score,
            "feedback": feedback
        }

    else:
        return {
            "status": "failed",
            "score": score,
            "feedback": feedback
        }