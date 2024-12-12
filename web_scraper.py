import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/Subhas_Chandra_Bose"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.title.string if soup.title else 'No title found'
    print("Title of the page:", title)
    headings = soup.find_all(['h1', 'h2', 'h3'])
    print("\nHeadings on the page:")
    for heading in headings:
        print(heading.get_text(strip=True))
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")