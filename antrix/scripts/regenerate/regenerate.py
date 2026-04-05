from ...prompts.mixed import regenerate_prompt


def regenerate(company, email, brochure, feedback, ai_client):
    """
    Regenerate email and brochure based on feedback.
    
    Args:
        company: Company name
        email: Current email content
        brochure: Current brochure content
        feedback: Feedback from supervisor
        ai_client: OpenAI client instance
    
    Returns:
        tuple: (improved_email, improved_brochure)
    """
    prompt = regenerate_prompt.format(
        company_name=company,
        email_output=email,
        brochure_output=brochure,
        review_feedback=feedback
    )

    response = ai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    text = response.choices[0].message.content

    # Robust parsing with fallback
    if "Improved Email:" in text and "Improved Brochure:" in text:
        improved_email = text.split("Improved Brochure:")[0].replace("Improved Email:", "").strip()
        improved_brochure = text.split("Improved Brochure:")[-1].strip()
    else:
        # Fallback: treat entire response as email
        improved_email = text.strip()
        improved_brochure = brochure

    return improved_email, improved_brochure