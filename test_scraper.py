from scraper.scraper import fetch_page
from scraper.parser import extract_title
from scraper.change_detector import has_changed
from config.config import load_data, save_data

url = "https://example.com"

html = fetch_page(url)
current_title = extract_title(html)

data = load_data()
previous_title = data.get("last_title", "")

if has_changed(previous_title, current_title):
    print("Change detected!")
    save_data({"last_title": current_title})
else:
    print("No change detected.")
