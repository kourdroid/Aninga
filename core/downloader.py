import httpx
import asyncio
import os
from typing import Callable, Awaitable, Any

class AsyncDownloader:
    """
    High-performance async download engine using httpx.
    Eliminates UI freezing by chunking and executing in the asyncio event loop.
    """
    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    async def download_file(
        self, 
        url: str, 
        filename: str, 
        progress_callback: Callable[[int, int], Any] = None
    ):
        filepath = os.path.join(self.output_dir, filename)
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        
        async with httpx.AsyncClient(timeout=60.0, follow_redirects=True, headers=headers) as client:
            async with client.stream("GET", url) as response:
                response.raise_for_status()
                total_bytes = int(response.headers.get("Content-Length", 0))
                downloaded = 0
                
                with open(filepath, "wb") as f:
                    async for chunk in response.aiter_bytes(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                            downloaded += len(chunk)
                            
                            if progress_callback:
                                # We support both sync and async callbacks
                                if asyncio.iscoroutinefunction(progress_callback):
                                    await progress_callback(downloaded, total_bytes)
                                else:
                                    progress_callback(downloaded, total_bytes)
                                    
        return filepath
