email_prompt="""Write a sponsorship email using this EXACT structure.

Company: {company_name}
Insights: {insights}

[SUBJECT]
<One sharp, specific line tied to company insight>

[EMAIL]
<Hook: 1–2 lines referencing a real product/initiative/audience match>

<Context: 1 line about ANTRAAL 4.0 + 300+ developers>

<Value: 2–3 lines explaining why THIS company benefits specifically>

<Ask: 1 clear, direct sponsorship ask (prizes/credits/merch)>

<Close: 1 short line + signature>

Rules:
- Max 130 words total
- Every section must use company-specific detail
- No generic praise (e.g., “innovative”, “leading”)
- Output ONLY [SUBJECT] and [EMAIL] sections - NO other content, NO brochure
- If any section is generic, rewrite before finishing"""