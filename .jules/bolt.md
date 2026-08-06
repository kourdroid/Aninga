## 2024-05-18 - Small Chunk Size Anti-Pattern in Large Video Downloads
**Learning:** Using a small chunk size (e.g., 1KB / 1024 bytes) with `response.iter_content` when downloading large video files, combined with a progress bar like `tqdm`, causes massive CPU overhead and disk I/O thrashing because `tqdm` updates progress and writes to disk for every tiny chunk downloaded.
**Action:** When downloading large files, use a larger chunk size (e.g., 1MB / `1024*1024`) to significantly reduce the frequency of progress bar updates and disk write operations, improving performance.
## 2024-05-14 - HTTP Connection Pooling for Faster Image Downloads
**Learning:** Sequential image downloading without reusing HTTP connections (via `requests.get`) creates enormous overhead due to repeated TCP/SSL handshakes.
**Action:** When making multiple iterative requests to the same host, always wrap the loop in a `requests.Session()` context manager to enable connection pooling and avoid redundant handshakes. Also ensure large chunk sizes (e.g., 1MB) for `iter_content` to reduce disk write overhead.
