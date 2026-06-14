CLAIM_EXTRACTION_PROMPT = """
You are an expert fact extraction system.

Extract factual claims that can be independently verified.

Focus on:
- Statistics
- Dates
- Percentages
- Financial figures
- Rankings
- Technical facts

For EACH claim generate a short search query that would help verify it.

Return STRICT JSON ONLY.

Example:

[
  {{
    "claim": "Google was founded in 1998",
    "type": "date",
    "search_query": "Google founded year"
  }}
]

TEXT:

{text}
"""

VERIFY_PROMPT = """
You are an expert fact-checking system.

Verify claims using ONLY the supplied web evidence.

Claims and Evidence:

{claims_and_evidence}

Rules:

1. Verified
   - Evidence strongly supports the claim

2. Inaccurate
   - Claim is partially correct or outdated

3. False
   - Evidence contradicts the claim

4. Insufficient Evidence
   - Evidence is empty or weak

Return STRICT JSON ONLY.

[
  {{
    "claim": "",
    "verdict": "",
    "confidence": "",
    "correct_fact": "",
    "explanation": "",
    "sources_used": []
  }}
]
"""