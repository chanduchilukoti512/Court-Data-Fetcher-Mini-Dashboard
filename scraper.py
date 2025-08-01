import requests
from bs4 import BeautifulSoup

def fetch_case_details(case_type, case_number, filing_year):
    try:
        url = "https://services.ecourts.gov.in/ecourtindia_v6/cases/case_no.php"
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        # ✅ Using Haryana (HR), dist_code 8, court_code 1
        data = {
            "state_code": "AP",         # Haryana
            "dist_code": "8",           # Try 8 (Palwal/Faridabad alt)
            "court_code": "1",          # Civil Court
            "case_type": case_type,
            "case_no": case_number,
            "case_year": filing_year
        }

        response = requests.post(url, headers=headers, data=data, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")

        with open("court_response.html", "w", encoding="utf-8") as f:
            f.write(soup.prettify())

        # Default values
        petitioner = respondent = filing_date = next_hearing = pdf_link = "Not Available"

        rows = soup.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if len(cells) == 2:
                key = cells[0].get_text(strip=True).lower()
                val = cells[1].get_text(strip=True)

                if "petitioner" in key:
                    petitioner = val
                elif "respondent" in key:
                    respondent = val
                elif "filing" in key:
                    filing_date = val
                elif "next" in key:
                    next_hearing = val
                elif "order" in key or "judgment" in key:
                    a_tag = cells[1].find("a")
                    if a_tag and a_tag.get("href"):
                        pdf_link = "https://services.ecourts.gov.in" + a_tag["href"]

        parties = f"{petitioner} vs {respondent}"

        parsed_data = {
            "case_title": f"{case_type} No. {case_number}/{filing_year}",
            "parties": parties,
            "filing_date": filing_date,
            "next_hearing": next_hearing,
            "pdf_link": pdf_link
        }

        return parsed_data, response.text

    except Exception as e:
        return None, str(e)