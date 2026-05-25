## 2024-05-18 - Small Chunk Size Anti-Pattern in Large Video Downloads
**Learning:** Using a small chunk size (e.g., 1KB / 1024 bytes) with `response.iter_content` when downloading large video files, combined with a progress bar like `tqdm`, causes massive CPU overhead and disk I/O thrashing because `tqdm` updates progress and writes to disk for every tiny chunk downloaded.
**Action:** When downloading large files, use a larger chunk size (e.g., 1MB / `1024*1024`) to significantly reduce the frequency of progress bar updates and disk write operations, improving performance.
## 2026-05-25 - Repetitive Requests Without Connection Pooling Anti-Pattern
**Learning:** The codebase previously made independent `requests.get()` calls inside loops, forcing repetitive TCP/SSL handshakes for each image/episode.
**Action:** Use `requests.Session()` to leverage connection pooling and eliminate repetitive handshake overhead when downloading multiple resources from the same host.
