import httpx
from bs4 import BeautifulSoup
from typing import List
import undetected_chromedriver as uc
from core.models import AnimeItem, Episode

class Anime4upPlugin:
    name = "Anime4up"
    domain = "w1.anime4up.rest"
    base_url = "https://w1.anime4up.rest"

    def search(self, query: str) -> List[AnimeItem]:
        results = []
        try:
            with httpx.Client(timeout=10) as client:
                res = client.get(f"{self.base_url}/?s={query}")
                soup = BeautifulSoup(res.text, 'html.parser')
                cards = soup.select(".anime-card-details, .post-item")
                for card in cards:
                    a = card.select_one('h3 a, .title a')
                    if a:
                        results.append(AnimeItem(title=a.text.strip(), url=a['href']))
        except Exception as e:
            print(f"[Anime4up] Search error: {e}")
        return results

    def get_latest_episodes(self) -> List[Episode]:
        return []

    def get_episodes(self, anime_url: str) -> List[Episode]:
        results = []
        try:
            with httpx.Client(timeout=10) as client:
                res = client.get(anime_url)
                soup = BeautifulSoup(res.text, 'html.parser')
                eps = soup.select(".episodes-card a, .episode-link")
                for ep in eps:
                    results.append(Episode(title=ep.text.strip(), url=ep['href']))
        except Exception as e:
            print(f"[Anime4up] Episodes error: {e}")
        return results

    def resolve_download_links(self, episode_url: str, driver: uc.Chrome = None) -> List[str]:
        urls = []
        try:
            with httpx.Client(timeout=10) as client:
                res = client.get(episode_url)
                soup = BeautifulSoup(res.text, 'html.parser')
                down_links = soup.select(".download-links a.btn")
                for dl in down_links:
                    if dl.has_attr('href'):
                        urls.append(dl['href'])
        except Exception as e:
            pass
        return urls
