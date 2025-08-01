import sqlite3

def log_query(case_type, case_number, filing_year, raw_response):
    conn = sqlite3.connect('court_queries.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS queries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_type TEXT,
            case_number TEXT,
            filing_year TEXT,
            raw_response TEXT
        )
    ''')
    c.execute('''
        INSERT INTO queries (case_type, case_number, filing_year, raw_response)
        VALUES (?, ?, ?, ?)
    ''', (case_type, case_number, filing_year, raw_response))
    conn.commit()
    conn.close()
