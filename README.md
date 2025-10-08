# 🤖 AI Lead Scorer Tool by Aman Mani Tripathi

## Overview
This is a simple **AI-powered lead scoring and validation tool** built using Python and Streamlit.  
It helps sales teams and business analysts identify **high-value AI-ready companies** by analyzing leads data, validating emails, and assigning a score (0–100) based on company metrics.

The tool is designed as a demo for **Caprae Capital’s AI-Readiness Pre-Screening Challenge**.

---

## Features
- Upload CSV file with company leads (`Company`, `Email`, `Industry`, `Employees`, `Revenue ($M)`, `Score`)  
- Automatic **email validation**  
- **AI-readiness scoring** highlight (Score >= 80 marked as top lead)  
- **Top 10 AI-ready companies** display  
- **Bar chart** visualization of all lead scores  
- **Download filtered/scored leads** as CSV  

---

## Requirements
- Python 3.8+  
- Packages:
  - streamlit
  - pandas

Install dependencies with:
```bash
pip install -r requirements.txt
