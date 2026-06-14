import os
import json
import streamlit as st

from dotenv import load_dotenv
import google.generativeai as genai
from tavily import TavilyClient

tavily = TavilyClient(api_key=TAVILY_API_KEY)

from prompts import (
    CLAIM_EXTRACTION_PROMPT,
    VERIFY_PROMPT
)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

genai.configure(
    api_key=GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if not TAVILY_API_KEY:
    TAVILY_API_KEY = st.secrets["TAVILY_API_KEY"]


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
            search_depth="basic",
            max_results=5
        )

        print("========== TAVILY RESPONSE ==========")
        print(response)

        results = response.get("results", [])

        evidence = []

        for r in results:

            evidence.append(
                {
                    "title": r.get("title", ""),
                    "snippet": r.get("content", ""),
                    "url": r.get("url", "")
                }
            )

        print("========== EVIDENCE ==========")
        print(evidence)

        return evidence

    except Exception as e:

        print("TAVILY ERROR:", e)
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