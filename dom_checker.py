import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import sys

urls = {
    'Anime3rb': 'https://anime3rb.com/',
    'Anime4up': 'https://w1.anime4up.rest/home8/',
    'TopCinema': 'https://topcinemaa.com/category/مسلسلات-انمي/'
}

with open('dom_structure.txt', 'w', encoding='utf-8') as f:
    for name, url in urls.items():
        f.write(f"\n========================================\nAnalyzing {name}\n========================================\n")
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36'})
        try:
            html = urllib.request.urlopen(req, timeout=15).read().decode('utf-8')
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.title.string.strip() if soup.title else 'No Title'
            f.write(f"[TITLE]: {title}\n")
            
            links = soup.find_all('a', href=True)
            episode_links = [a for a in links if '/episode/' in a['href'] or '-الحلقة-' in urllib.parse.unquote(a['href'])]
            anime_links = [a for a in links if '/anime/' in a['href'] or '/titles/' in a['href']]
            
            f.write(f"Total episode links found: {len(episode_links)}\n")
            f.write(f"Total anime links found: {len(anime_links)}\n")

            if episode_links:
                ep = episode_links[0]
                f.write(f"\n[SAMPLE EPISODE LINK]: {ep['href']}\n")
                f.write(f" - Tag: <{ep.name}> Classes: {ep.get('class', [])}\n")
                if ep.parent:
                    f.write(f" - Parent Tag: <{ep.parent.name}> Classes: {ep.parent.get('class', [])}\n")
                    if ep.parent.parent:
                        f.write(f" - Grandparent Tag (Grid?): <{ep.parent.parent.name}> Classes: {ep.parent.parent.get('class', [])}\n")
            
            if anime_links:
                an = anime_links[0]
                f.write(f"\n[SAMPLE ANIME LINK]: {an['href']}\n")
                f.write(f" - Tag: <{an.name}> Classes: {an.get('class', [])}\n")
                if an.parent:
                    f.write(f" - Parent Tag: <{an.parent.name}> Classes: {an.parent.get('class', [])}\n")
                    if an.parent.parent:
                        f.write(f" - Grandparent Tag (Grid?): <{an.parent.parent.name}> Classes: {an.parent.parent.get('class', [])}\n")

        except Exception as e:
            f.write(f"[ERROR]: Request failed: {e}\n")
