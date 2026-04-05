import re

def extract_score(text):
    match = re.search(r"Score:\s*(\d+)", text)
    return int(match.group(1)) if match else 0


def extract_verdict(text):
    if "APPROVE" in text:
        return "approved"
    return "revise"


def extract_feedback(text):
    return text.split("Feedback:")[-1]

def extract_email(text):
    match = re.search(r"Email:\s*(.*?)(?:\n|$)", text, re.DOTALL)
    return match.group(1).strip() if match else ""

def extract_brochure(text):
    match = re.search(r"Brochure:\s*(.*)", text, re.DOTALL)
    return match.group(1).strip() if match else ""