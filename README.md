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
(Add screenshots here)

## Setup
...