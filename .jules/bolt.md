## 2024-05-18 - Small Chunk Size Anti-Pattern in Large Video Downloads
**Learning:** Using a small chunk size (e.g., 1KB / 1024 bytes) with `response.iter_content` when downloading large video files, combined with a progress bar like `tqdm`, causes massive CPU overhead and disk I/O thrashing because `tqdm` updates progress and writes to disk for every tiny chunk downloaded.
**Action:** When downloading large files, use a larger chunk size (e.g., 1MB / `1024*1024`) to significantly reduce the frequency of progress bar updates and disk write operations, improving performance.
## 2026-06-04 - Connection Pooling for Independent Requests
**Learning:** Python's requests library does not use connection pooling for independent get() calls, resulting in repetitive TCP/SSL handshake overhead when making multiple requests to the same host.
**Action:** Always instantiate and use requests.Session() with a with context manager when making multiple requests to the same host to enable connection pooling and improve performance.
