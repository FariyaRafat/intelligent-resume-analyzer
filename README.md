# AI Resume Analyzer & PDF Editor

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)](https://flask.palletsprojects.com/)
[![Gemini](https://img.shields.io/badge/Gemini-2.0_Flash-orange.svg)](https://ai.google.dev/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An AI-powered Resume Analyzer that evaluates resumes against job descriptions, generates an ATS compatibility score, provides section-wise improvement suggestions, and enables PDF/DOCX editing directly in the browser using **Google Gemini 2.0 Flash**.

---

## Overview

The AI Resume Analyzer helps job seekers optimize their resumes by comparing them with a target job description. The application provides ATS scoring, keyword analysis, AI-generated feedback, grammar suggestions, and built-in editing capabilities for both PDF and DOCX resumes.

---

## Features

- ATS Compatibility Score (0–100)
- Job Description Matching
- Keyword Analysis (Matched & Missing Keywords)
- Section-wise Resume Feedback
- Grammar and Writing Suggestions
- Live PDF Editing
- DOCX Editing Support
- Re-analysis After Editing
- Export Resume in Original Format
- Responsive Web Interface

---

## Tech Stack

### Backend

- Flask
- pdfplumber
- pypdf
- ReportLab
- python-docx
- Pillow

### AI

- Google Gemini 2.0 Flash

### Frontend

- HTML5
- CSS3
- Vanilla JavaScript

---

## Project Structure

```text
AI_Resume_Analyzer/
│── app.py
│── requirements.txt
│── static/
│   ├── css/
│   ├── js/
│   └── images/
│── templates/
│── uploads/
│── outputs/
│── utils/
└── README.md
```

---

## Installation

```bash
# Clone the repository
git clone https://github.com/FariyaRafat/intelligent-resume-analyzer.git

# Navigate to the project directory
cd intelligent-resume-analyzer

# Create a virtual environment (optional)
python -m venv venv

# Activate the environment

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the application
python app.py
```

---

## Usage

1. Upload a resume in **PDF** or **DOCX** format.
2. Paste the target job description.
3. Analyze the resume.
4. Review:
   - ATS Score
   - Keyword Analysis
   - Section-wise Suggestions
   - Grammar Feedback
5. Edit the resume if required.
6. Re-analyze the updated version.
7. Download the final resume.

---

## Future Enhancements

- User Authentication
- Resume History
- Multiple Resume Templates
- Cover Letter Generator
- Interview Question Generator
- Resume Version Comparison

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Author

**Fariya Rafat**

M.Tech (Advanced Computing)  
Maulana Azad National Institute of Technology (MANIT), Bhopal

GitHub: https://github.com/FariyaRafat

---

If you find this project useful, consider starring the repository.