"""BeautifulSoup example — parse a local HTML file and list links."""
from bs4 import BeautifulSoup
from pathlib import Path

HTML = Path(__file__).parent / "sample_page.html"

def main():
    print("BeautifulSoup demo — parsing local HTML:", HTML)
    html = HTML.read_text(encoding='utf-8')
    soup = BeautifulSoup(html, "html.parser")
    print("Title:", soup.title.string)
    links = [a.get('href') for a in soup.find_all('a')]
    print("Found links:")
    for href in links:
        print("-", href)

if __name__ == '__main__':
    main()
