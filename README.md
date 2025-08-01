# Court Case Data Dashboard

This project was built for the internship task: **Court Case Data Dashboard Using Web Scraping**.

## ✅ Project Overview

This Flask-based web application allows users to enter Indian court case details (case type, number, and year), and fetches real-time data from the eCourts India portal using web scraping.

### 🔍 Technologies Used:
- Python
- Flask
- BeautifulSoup (for scraping)
- Bootstrap (for UI)

---

## 📥 User Inputs:
- **Case Type**: (e.g., MACP, CIVI, CR, NIA)
- **Case Number**: (e.g., 1234)
- **Filing Year**: (e.g., 2018)

✅ These are entered on the web form and submitted to fetch case status.

---

## 📤 Output Shown:
- Case Title (e.g., MACP No. 1416/2017)
- Petitioner vs Respondent
- Filing Date
- Next Hearing Date
- Latest Order (PDF Link if available)

---

## ⚠️ Valid Input Note:
This project depends on real data from [https://services.ecourts.gov.in](https://services.ecourts.gov.in). 
Please use actual, verifiable court case details for accurate results.

**Example (you must verify on portal first):**
- Case Type: CIVI
- Case No: 123
- Year: 2019

If values are invalid, you will see:
❌ “Invalid input or court not supported”

---

## ▶ How to Run

```bash
pip install -r requirements.txt
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## ✅ Submission Checklist (from PDF requirements)
- [x] Web Interface (index.html with Bootstrap UI)
- [x] Flask Backend
- [x] Web Scraper using BeautifulSoup
- [x] Displays Petitioner, Respondent, Dates, PDF
- [x] Handles invalid inputs with error message
- [x] requirements.txt included
- [x] README with clear instructions ✅

