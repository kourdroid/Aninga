## 2024-05-18 - Small Chunk Size Anti-Pattern in Large Video Downloads
**Learning:** Using a small chunk size (e.g., 1KB / 1024 bytes) with `response.iter_content` when downloading large video files, combined with a progress bar like `tqdm`, causes massive CPU overhead and disk I/O thrashing because `tqdm` updates progress and writes to disk for every tiny chunk downloaded.
**Action:** When downloading large files, use a larger chunk size (e.g., 1MB / `1024*1024`) to significantly reduce the frequency of progress bar updates and disk write operations, improving performance.

## 2024-05-24 - Missing Connection Pooling in Loops
**Learning:** Independent `requests.get()` calls within loops in `download_manga` and `download_anime` create a new TCP/SSL connection for each download, creating significant overhead when fetching many images or video episodes from the same host.
**Action:** Always wrap loop-based downloads with `with requests.Session() as session:` and use `session.get()` to leverage connection pooling and eliminate repetitive handshake latency.
