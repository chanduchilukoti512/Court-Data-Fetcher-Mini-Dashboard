from flask import Flask, render_template, request
from scraper import fetch_case_details
from db import log_query
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    case_type = request.form['case_type'].strip().upper()
    case_number = request.form['case_number'].strip()
    filing_year = request.form['filing_year'].strip()

    data, raw_response = fetch_case_details(case_type, case_number, filing_year)
    log_query(case_type, case_number, filing_year, raw_response)

    if "Invalid Parameter" in raw_response:
        return render_template("result.html", error="❌ Invalid input or court not supported. Please try a valid case.")

    if data:
        return render_template('result.html', data=data)

    return render_template('result.html', error="⚠️ Something went wrong. Please try again later.")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

