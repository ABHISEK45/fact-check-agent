# 📄 Fact Check Agent

An AI-powered fact-checking application that extracts factual claims from PDF documents, searches the live web for supporting evidence, verifies claims using Gemini, and stores the generated reports in PostgreSQL.

## Features

- Upload PDF documents
- Extract factual claims using Google Gemini
- Generate targeted search queries for extracted claims
- Search the live web using Tavily
- Verify claims against retrieved web evidence
- Classify claims as:
  - Verified
  - False
  - Inaccurate
  - Insufficient Evidence
- Generate explanations and corrected facts
- Display sources used for verification
- Store fact-checking reports and claims in PostgreSQL
- Export results as CSV

## Architecture

```text
PDF Upload
    ↓
PDF Text Extraction
    ↓
Gemini
Claim Extraction
    ↓
Tavily
Live Web Search
    ↓
Gemini
Evidence-based Verification
    ↓
PostgreSQL
Report & Claim Storage
    ↓
CSV Report