import httpx
from bs4 import BeautifulSoup
from typing import List
import undetected_chromedriver as uc
from core.models import AnimeItem, Episode
from core.browser import solve_challenge_silently

class Anime3rbPlugin:
    name = "Anime3rb"
    domain = "anime3rb.com"
    base_url = "https://anime3rb.com"

    def search(self, query: str) -> List[AnimeItem]:
        results = []
        try:
            with httpx.Client(timeout=10) as client:
                res = client.get(f"{self.base_url}/search?q={query}")
                soup = BeautifulSoup(res.text, 'html.parser')
                # Usually standard card layouts. Adapting based on prior structure review.
                for card in soup.select('div.anime-card, a.movie-card'):
                    title = card.select_one('h3, .title').text.strip()
                    url = card.get('href')
                    if url and not url.startswith('http'):
                        url = self.base_url + url
                    results.append(AnimeItem(title=title, url=url))
        except Exception as e:
            print(f"[Anime3rb] Search error: {e}")
        return results

    def get_latest_episodes(self) -> List[Episode]:
        return []

    def get_episodes(self, anime_url: str) -> List[Episode]:
        results = []
        try:
            with httpx.Client(timeout=10) as client:
                res = client.get(anime_url)
                soup = BeautifulSoup(res.text, 'html.parser')
                # Assuming typical list grouping
                for li in soup.select('.episodes-list a, ul.episodes a'):
                    results.append(Episode(
                        title=li.text.strip(),
                        url=self.base_url + li['href'] if not li['href'].startswith('http') else li['href']
                    ))
        except Exception as e:
            print(f"[Anime3rb] Episodes error: {e}")
        return results

    def resolve_download_links(self, episode_url: str, driver: uc.Chrome = None) -> List[str]:
        # Emulating standard anime3rb logic
        urls = []
        try:
            with httpx.Client(timeout=10) as client:
                res = client.get(episode_url)
                soup = BeautifulSoup(res.text, 'html.parser')
                # Extract servers
                servers = soup.select('.download-servers a.server-btn, .downloads a')
                for s in servers:
                    if s.has_attr('href'):
                        urls.append(s['href'])
        except Exception as e:
            print(f"[Anime3rb] Error resolving downloads: {e}")
        return urls
