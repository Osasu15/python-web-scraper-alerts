import logging
from pathlib import Path
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "scraper.log"

logging.basicConfig(
    filename=str(LOG_FILE),
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    force=True
)



#
from scraper.scraper import fetch_page
from scraper.parser import extract_title
from scraper.change_detector import has_changed
from config.config import load_data, save_data
from alerts.email_alert import send_email_alert


def run():
    logging.info("Scraper started")

    try:
        url = "https://example.com"

        html = fetch_page(url)
        current_title = extract_title(html)

        data = load_data()
        previous_title = data.get("last_title", "")

        if has_changed(previous_title, current_title):
            logging.info("Change detected")
            send_email_alert(
                subject="Website Change Detected",
                body=f"Title changed to: {current_title}"
            )
            save_data({"last_title": current_title})
            logging.info("Alert sent and data updated")
        else:
            logging.info("No change detected")

    except Exception as e:
        logging.error(f"Scraper failed: {e}", exc_info=True)
if __name__ == "__main__":
    run()
