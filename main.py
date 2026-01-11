from scraper.scraper import fetch_page
from scraper.parser import extract_title
from scraper.change_detector import has_changed
from config.config import load_data, save_data
from alerts.email_alert import send_email_alert


def run():
    url = "https://example.com"

    html = fetch_page(url)
    current_title = extract_title(html)

    data = load_data()
    previous_title = data.get("last_title", "")

    if has_changed(previous_title, current_title):
        send_email_alert(
            subject="Website Change Detected",
            body=f"Title changed to: {current_title}"
        )
        save_data({"last_title": current_title})
    else:
        pass  # No change


if __name__ == "__main__":
    run()
