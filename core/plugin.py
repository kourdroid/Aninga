from typing import List, Protocol, runtime_checkable
from .models import AnimeItem, Episode
import undetected_chromedriver as uc

@runtime_checkable
class ScraperPlugin(Protocol):
    """
    The universal protocol that all scraper plugins must implement.
    This guarantees loose coupling between the CLI/GUI and the source implementations.
    """
    name: str      # e.g., "Witanime"
    domain: str    # e.g., "witanime.pics"
    
    def search(self, query: str) -> List[AnimeItem]:
        """Search the source for an anime via standard request/httpx"""
        ...
        
    def get_latest_episodes(self) -> List[Episode]:
        """Fetch the latest released episodes shown on the site's homepage"""
        ...

    def get_episodes(self, anime_url: str) -> List[Episode]:
        """Retrieve all episodes for a given anime URL"""
        ...
        
    def resolve_download_links(self, episode_url: str, driver: uc.Chrome = None) -> List[str]:
        """
        Given an episode URL, resolve the actual video file URLs.
        If the site has anti-bot paths (like blkom), this method can utilize the stealth driver.
        Returns a list of raw video URLs (e.g. .mp4).
        """
        ...
