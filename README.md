# Fact Check Agent

## Overview
A web application that automatically fact-checks claims inside uploaded PDFs by extracting factual statements, searching live web sources, and generating verification reports.

## Features
- PDF Upload
- Claim Extraction
- Search Query Generation
- Live Web Search (Tavily)
- Fact Verification using Gemini
- Evidence Collection
- CSV Report Export

## Tech Stack
- Streamlit
- Gemini 2.5 Flash
- Tavily Search API
- PDFPlumber
- Python

## Architecture

PDF
↓
Claim Extraction (Gemini)
↓
Search Query Generation
↓
Tavily Web Search
↓
Evidence Collection
↓
Fact Verification (Gemini)
↓
Report Generation

## Screenshots
<img width="1430" height="828" alt="Screenshot 2026-06-14 at 7 52 18 PM" src="https://github.com/user-attachments/assets/adc1e886-45c8-4b5a-b602-8122127d2b97" />
<img width="1426" height="807" alt="Screenshot 2026-06-14 at 7 52 33 PM" src="https://github.com/user-attachments/assets/a64e8038-ca91-4071-b078-a6d88aad428b" />

