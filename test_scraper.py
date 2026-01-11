from scraper.scraper import fetch_page

url = "https://example.com"
html = fetch_page(url)

print("Page fetched successfully!")
print(html[:500])
