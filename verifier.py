import os
import json

from dotenv import load_dotenv
import google.generativeai as genai
from tavily import TavilyClient

from prompts import (
    CLAIM_EXTRACTION_PROMPT,
    VERIFY_PROMPT
)

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

tavily = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


def extract_claims(text):

    prompt = CLAIM_EXTRACTION_PROMPT.format(
        text=text[:15000]
    )

    response = model.generate_content(prompt)

    cleaned = (
        response.text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    try:
        return json.loads(cleaned)

    except Exception:
        return []


def search_web(query):

    try:

        response = tavily.search(
            query=query,
            max_results=3,
            search_depth="basic"
        )

        evidence = []

        for result in response.get(
            "results",
            []
        ):

            evidence.append(
                {
                    "title": result.get(
                        "title",
                        ""
                    ),
                    "snippet": result.get(
                        "content",
                        ""
                    )[:500],
                    "url": result.get(
                        "url",
                        ""
                    )
                }
            )

        return evidence

    except Exception as e:

        print(
            f"TAVILY ERROR: {e}"
        )

        return []


def verify_all_claims(claims_with_evidence):

    prompt = VERIFY_PROMPT.format(
        claims_and_evidence=json.dumps(
            claims_with_evidence,
            indent=2
        )
    )

    response = model.generate_content(prompt)

    cleaned = (
        response.text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    try:
        return json.loads(cleaned)

    except Exception:

        return [
            {
                "claim": "Parsing Error",
                "verdict": "Unknown",
                "confidence": "0%",
                "correct_fact": "",
                "explanation": cleaned,
                "sources_used": []
            }
        ]