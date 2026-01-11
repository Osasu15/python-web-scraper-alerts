from scraper.scraper import fetch_page
from scraper.parser import extract_title

url = "https://example.com"

html = fetch_page(url)
title = extract_title(html)

print("Page title:", title)
