
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import html2text

def crawl(url, max_depth=1, within_domain=True):
    visited = set()
    converter = html2text.HTML2Text()
    converter.ignore_links = False
    
    def valid_url(link):
        '''Check if the URL is within the same domain (if required)'''
        return (link not in visited and
                (not within_domain or link.startswith(url)))

    def crawl_page(url, depth):
        if depth > max_depth:
            return
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()  # Raise an exception for bad status codes
            soup = BeautifulSoup(response.text, 'html.parser')
            markdown = converter.handle(str(soup))
            
            # Process the content here (e.g., print, store, etc.)
            print(f"URL: {url}")
            print(markdown[:200])  # Print the first 200 chars of the markdown content
            
            visited.add(url)
            links = [urljoin(url, tag['href']) for tag in soup.find_all('a', href=True) if valid_url(tag['href'])]
            
            for link in links:
                crawl_page(link, depth + 1)
                
        except Exception as e:
            print(f"Failed to access {url}: {e}")

    crawl_page(url, 0)

# Example of usage:
# crawl("http://example.com", max_depth=2)
