from bs4 import BeautifulSoup

def extract_title(html: str) -> str:
    """
    Extract the page title from HTML.
    """
    soup = BeautifulSoup(html, "lxml")
    title = soup.find("title")

    if not title:
        raise ValueError("No <title> tag found")

    return title.text.strip()
