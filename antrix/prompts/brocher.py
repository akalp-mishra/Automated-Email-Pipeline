brochure_prompt="""Customize ONLY the brochure structure. Do NOT include email content.

Company: {company_name}
Insights: {insights}
Base: {brochure}

[HEADER]
ANTRAAL 4.0 x {company_name}

[WHY THIS PARTNERSHIP]
<2–3 lines directly connecting company product/audience to event>

[WHAT YOU GET]
- <Benefit 1 specific to company>
- <Benefit 2 specific to company>
- <Benefit 3 specific to company>

[ACTIVATION IDEAS]
- <How their product/service is used in event>
- <How participants interact with them>

[REACH]
<1–2 lines about 300+ developers, but tied to company relevance>

[ASK]
<Exact sponsorship ask: prizes / credits / merch>

Rules:
- Output ONLY the brochure structure above - NO email, NO commentary
- Replace generic content; do NOT reuse base brochure wording blindly
- Every bullet must be company-specific
- No generic phrases
- No extra sections or text outside template
If any section is generic or not company-specific, rewrite it before finishing."""