## 2024-05-18 - Small Chunk Size Anti-Pattern in Large Video Downloads
**Learning:** Using a small chunk size (e.g., 1KB / 1024 bytes) with `response.iter_content` when downloading large video files, combined with a progress bar like `tqdm`, causes massive CPU overhead and disk I/O thrashing because `tqdm` updates progress and writes to disk for every tiny chunk downloaded.
**Action:** When downloading large files, use a larger chunk size (e.g., 1MB / `1024*1024`) to significantly reduce the frequency of progress bar updates and disk write operations, improving performance.

## 2026-06-13 - Missing Connection Pooling in Loops
**Learning:** The codebase repeatedly uses `requests.get()` inside loops (e.g., iterating over images or episodes), which creates a new TCP/SSL connection for each request and adds significant handshake overhead.
**Action:** Always wrap sequential HTTP requests to the same host in a `requests.Session()` context manager to enable connection pooling and reduce latency.
