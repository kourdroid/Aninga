import httpx
from bs4 import BeautifulSoup
from typing import List
import undetected_chromedriver as uc

from core.models import AnimeItem, Episode
# Implicitly matching ScraperPlugin via structural typing checks in manager.py

class WitanimePlugin:
    name = "Witanime"
    domain = "witanime.pics"
    base_url = "https://witanime.pics"

    def search(self, query: str) -> List[AnimeItem]:
        results = []
        try:
            with httpx.Client(timeout=10) as client:
                resp = client.get(f"{self.base_url}/?search_param=animes&s={query}")
                soup = BeautifulSoup(resp.text, 'html.parser')
                items = soup.select(".anime-card-container")
                for item in items:
                    title_elem = item.select_one(".anime-card-title a")
                    if title_elem:
                        results.append(AnimeItem(
                            title=title_elem.text.strip(),
                            url=title_elem['href']
                        ))
        except Exception as e:
            print(f"[Witanime] Search error: {e}")
        return results

    def get_latest_episodes(self) -> List[Episode]:
        results = []
        try:
            with httpx.Client(timeout=10) as client:
                resp = client.get(self.base_url)
                soup = BeautifulSoup(resp.text, 'html.parser')
                episodes = soup.select(".episodes-card-container")
                for ep in episodes:
                    a_tag = ep.select_one(".episodes-card-title a")
                    if a_tag:
                        results.append(Episode(
                            title=a_tag.text.strip(),
                            url=a_tag['href']
                        ))
        except Exception as e:
            print(f"[Witanime] get_latest_episodes error: {e}")
        return results

    def get_episodes(self, anime_url: str) -> List[Episode]:
        results = []
        try:
            with httpx.Client(timeout=10) as client:
                resp = client.get(anime_url)
                soup = BeautifulSoup(resp.text, 'html.parser')
                ep_links = soup.select(".episode-link a")
                for a in ep_links:
                    results.append(Episode(
                        title=a.text.strip(),
                        url=a['href']
                    ))
        except Exception as e:
            print(f"[Witanime] get_episodes error: {e}")
        return results

    def resolve_download_links(self, episode_url: str, driver: uc.Chrome = None) -> List[str]:
        """
        Witanime puts download links directly on the episode page or through a simple redirect.
        We emulate the legacy logic that was in main.py: looking for 'panel-body' and 'btn-white'.
        """
        urls = []
        try:
            with httpx.Client(timeout=10) as client:
                resp = client.get(episode_url)
                soup = BeautifulSoup(resp.text, 'html.parser')
                # Find all download links inside panel-body
                links = soup.select(".panel-body a.btn-white")
                for link in links:
                    if link.has_attr("href"):
                        urls.append(link["href"])
        except Exception as e:
            print(f"[Witanime] Error resolving download links: {e}")
        return urls
