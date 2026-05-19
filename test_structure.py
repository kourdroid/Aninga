import urllib.request
import re
from bs4 import BeautifulSoup

urls = {
    'Anime3rb': 'https://anime3rb.com/',
    'Anime4up': 'https://w1.anime4up.rest/home8/',
    'TopCinema': 'https://topcinemaa.com/category/مسلسلات-انمي/'
}

for name, url in urls.items():
    print(f"\n{'='*40}")
    print(f"Analyzing {name} ({url})")
    print(f"{'='*40}")
    
    # We use a spoofed User-Agent to ensure we get proper HTML back
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    )
    
    try:
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        
        # 1. Title
        print(f"[TITLE]: {soup.title.string.strip() if soup.title else 'No Title'}")
        
        # 2. Extract standard content links (Anime listings, Episodes)
        links = soup.find_all('a', href=True)
        episode_links = [a for a in links if '/episode/' in a['href'] or '-الحلقة-' in urllib.parse.unquote(a['href'])]
        anime_links = [a for a in links if '/anime/' in a['href'] or '/titles/' in a['href']]
        
        if episode_links:
            # Analyze the first episode element to get its structure/classes
            ep = episode_links[0]
            print(f"\n[SAMPLE EPISODE LINK]: {ep['href']}")
            print(f" - Classes: {ep.get('class', [])}")
            parent = ep.parent
            print(f" - Parent Tag: <{parent.name}> Classes: {parent.get('class', [])}")
            
            # Find the common container list (like a grid)
            grandparent = parent.parent if parent else None
            if grandparent:
                print(f" - Grandparent Tag (Grid?): <{grandparent.name}> Classes: {grandparent.get('class', [])}")
        
        if anime_links:
            # Analyze the first anime element
            an = anime_links[0]
            print(f"\n[SAMPLE ANIME LINK]: {an['href']}")
            print(f" - Classes: {an.get('class', [])}")
            parent = an.parent
            print(f" - Parent Tag: <{parent.name}> Classes: {parent.get('class', [])}")
            
    except Exception as e:
        print(f"[ERROR]: Request failed for {name}: {e}")
