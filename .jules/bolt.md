## 2024-05-18 - Small Chunk Size Anti-Pattern in Large Video Downloads
**Learning:** Using a small chunk size (e.g., 1KB / 1024 bytes) with `response.iter_content` when downloading large video files, combined with a progress bar like `tqdm`, causes massive CPU overhead and disk I/O thrashing because `tqdm` updates progress and writes to disk for every tiny chunk downloaded.
**Action:** When downloading large files, use a larger chunk size (e.g., 1MB / `1024*1024`) to significantly reduce the frequency of progress bar updates and disk write operations, improving performance.
## 2024-06-22 - Connection Pooling for Repeated API Calls
**Learning:** Python's `requests.get()` function does not use connection pooling. Every independent call to `requests.get()` creates a new socket and performs a full TCP/SSL handshake, which causes significant overhead when downloading multiple files (like manga images) from the same host.
**Action:** Always wrap repeated HTTP requests to the same host in a `requests.Session()` context manager (`with requests.Session() as session:`) to reuse underlying TCP connections, drastically reducing latency and handshake overhead.
