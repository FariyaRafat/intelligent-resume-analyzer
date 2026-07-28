# AI Resume Analyzer & Resume Editor

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)](https://flask.palletsprojects.com/)
[![Google Gemini](https://img.shields.io/badge/Google-Gemini-blue.svg)](https://ai.google.dev/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

An AI-powered Resume Analyzer that evaluates resumes against job descriptions, generates an ATS compatibility score, identifies missing keywords, provides section-wise feedback, and allows users to edit PDF/DOCX resumes directly in the browser using the Google Gemini API.

---

## Overview

AI Resume Analyzer helps job seekers optimize their resumes for Applicant Tracking Systems (ATS). Users can upload a resume, provide a target job description, receive AI-generated insights, edit the resume inside the application, re-analyze it, and download the improved version.

---

## Features

- AI-powered ATS Score (0–100)
- Resume vs Job Description Analysis
- Keyword Matching & Missing Keyword Detection
- Section-wise Resume Evaluation
- Grammar & Writing Suggestions
- Strengths & Weakness Analysis
- PDF Resume Editing
- DOCX Resume Editing
- Resume Re-analysis After Editing
- Download Updated Resume
- Responsive User Interface

---

## Tech Stack

### Backend

- Python
- Flask
- Google GenAI SDK
- pdfplumber
- pypdf
- ReportLab
- python-docx
- python-dotenv
- Pillow

### AI

- Google Gemini API

### Frontend

- HTML5
- CSS3
- JavaScript

---

## Project Structure

```text
intelligent-resume-analyzer/
│
├── app.py
├── gemini_service.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
│
├── static/
│   ├── css/
│   └── js/
│
├── templates/
│
├── uploads/        # Generated at runtime
├── edited/         # Generated at runtime
├── analysis/       # Generated at runtime
└── __pycache__/    # Auto-generated
```

> **Note:** The `uploads`, `edited`, `analysis`, and `__pycache__` folders are generated automatically when the application runs and should not be committed to GitHub.

---

## Installation

```bash
# Clone the repository
git clone https://github.com/FariyaRafat/intelligent-resume-analyzer.git

# Navigate to the project
cd intelligent-resume-analyzer

# Create a virtual environment (optional)
python -m venv venv

# Activate virtual environment

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
FLASK_SECRET_KEY=YOUR_SECRET_KEY
```

---

## Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## Usage

1. Upload a resume (PDF or DOCX).
2. Enter the target job role.
3. Paste the job description.
4. Click **Analyze Resume**.
5. Review:
   - ATS Score
   - Keyword Match
   - Missing Keywords
   - Section-wise Feedback
   - Grammar Suggestions
   - Strengths & Weaknesses
6. Edit the resume if required.
7. Click **Re-analyze** to compare improvements.
8. Download the updated resume.

---

## Future Enhancements

- User Authentication
- Resume History
- Resume Version Comparison
- Cover Letter Generator
- Interview Question Generator
- Resume Templates
- Resume Analytics Dashboard

---

## License

This project is licensed under the Apache License 2.0. See the `LICENSE` file for details.

---

## Author

**Fariya Rafat**

M.Tech (Advanced Computing)  
Maulana Azad National Institute of Technology (MANIT), Bhopal

GitHub: https://github.com/FariyaRafat

---

If you found this project useful, consider giving it a star.