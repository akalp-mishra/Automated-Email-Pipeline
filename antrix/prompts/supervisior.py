supervisior_prompt="""Act as a strict sponsorship email reviewer.

Company: {company_name}

Email:
{email_output}

Brochure:
{brochure_output}

Evaluate:
- Personalization (company-specific?)
- Specificity (real traits/insights used?)
- Tone (professional, persuasive?)
- Relevance (right benefits?)
- Generic language?

Reject if:
- Reusable for another company
- Generic praise present
- >150 words
- No concrete hook

Be highly critical. Default to rejection.

Output format (strict):
Score: X/10

Feedback:
- ...

Verdict:
APPROVE / REVISE
Flag exact phrases that feel generic."""