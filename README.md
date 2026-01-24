# Python Web Scraper Alert System

A production-ready Python automation system that monitors a website for changes and sends email alerts when updates are detected.  
The system runs unattended via Windows Task Scheduler and includes logging, error handling, and persistent state tracking.

---

##  Features

- Automated daily web scraping
- HTML parsing using BeautifulSoup
- Change detection using persisted JSON state
- Email alerts via SMTP
- Secure configuration using environment variables
- Background execution with Windows Task Scheduler
- Persistent logging for debugging and monitoring
- Resilient error handling to prevent silent failures

---

##  Architecture Overview

python-web-scraper-alerts/
│
├── scraper/
│ ├── scraper.py 
│ ├── parser.py 
│ └── change_detector.py 
│
├── alerts/
│ └── email_alert.py 
│
├── config/
│ └── config.py 
│
├── data/
│ └── prices.json 
│
├── logs/
│ └── scraper.log 
│
├── main.py 
├── test_scraper.py 
├── test_email.py 
└── README.md


---

##  How It Works

1. Fetches the target webpage
2. Parses the page title
3. Compares the result with the previous stored value
4. Sends an email alert if a change is detected
5. Logs execution results and errors
6. Runs automatically on a schedule

---

##  Automation

The system runs daily using **Windows Task Scheduler**, executing the virtual environment’s Python interpreter directly.  
This allows the script to run unattended, even when the user is not logged in.

---

##  Security

- Sensitive credentials stored in a `.env` file
- `.env` excluded from version control via `.gitignore`
- No secrets committed to GitHub

---

##  Future Improvements

- Support for multiple URLs
- Price and stock tracking
- Database storage (SQLite / PostgreSQL)
- Slack / Discord notifications
- ML-based anomaly detection on page changes
