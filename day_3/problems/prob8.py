import requests
import bs4
url = "https://ss64.com/bash" 
prefix = url
resp = requests.get(url) 
if resp.status_code == 200:
    html = resp.text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    selector = "a" 
    all_links_with_text = []
    for a in soup.select(selector):
        if 'href' in a.attrs:
            href = a.attrs['href']
        if not href.startswith(('https://', 'https://')):
            href = f"{prefix}/{href}"
        both = ( href, a.text)
        all_links_with_text.append(both)
    print(all_links_with_text[:2])
