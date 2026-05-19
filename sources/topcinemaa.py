import httpx
from bs4 import BeautifulSoup
from typing import List
import undetected_chromedriver as uc
from core.models import AnimeItem, Episode
from core.browser import solve_challenge_silently

class TopCinemaaPlugin:
    name = "TopCinemaa"
    domain = "topcinemaa.com"
    base_url = "https://topcinemaa.com"

    def search(self, query: str) -> List[AnimeItem]:
        return []

    def get_latest_episodes(self) -> List[Episode]:
        return []

    def get_episodes(self, anime_url: str) -> List[Episode]:
        return []

    def resolve_download_links(self, episode_url: str, driver: uc.Chrome = None) -> List[str]:
        """
        May require the stealth driver if they implement heavy caching logic or bot protection.
        """
        urls = []
        if driver:
            try:
                html = solve_challenge_silently(driver, episode_url)
                soup = BeautifulSoup(html, 'html.parser')
                links = soup.select('.downloadBox a, .servers-list a')
                for l in links:
                    if l.has_attr('href') and not '#' in l['href']:
                        urls.append(l['href'])
            except Exception as e:
                print(f"[TopCinemaa] Driver resolution error: {e}")
        return urls
