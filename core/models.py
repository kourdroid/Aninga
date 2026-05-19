from pydantic import BaseModel
from typing import List, Optional

class Episode(BaseModel):
    title: str
    url: str
    number: Optional[float] = None
    
    # Direct raw .mp4 or m3u8 URLs if successfully resolved
    direct_urls: Optional[List[str]] = None

class AnimeItem(BaseModel):
    title: str
    url: str
    cover_image: Optional[str] = None
    episodes: List[Episode] = []
    
    # Metadata
    description: Optional[str] = None
    status: Optional[str] = None
    release_year: Optional[int] = None
