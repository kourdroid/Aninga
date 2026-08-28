## 2024-05-18 - Small Chunk Size Anti-Pattern in Large Video Downloads
**Learning:** Using a small chunk size (e.g., 1KB / 1024 bytes) with `response.iter_content` when downloading large video files, combined with a progress bar like `tqdm`, causes massive CPU overhead and disk I/O thrashing because `tqdm` updates progress and writes to disk for every tiny chunk downloaded.
**Action:** When downloading large files, use a larger chunk size (e.g., 1MB / `1024*1024`) to significantly reduce the frequency of progress bar updates and disk write operations, improving performance.
## 2024-05-23 - Requests Connection Pooling
**Learning:** Python's `requests.get()` doesn't pool connections. In loops, wrapping the requests with `with requests.Session() as session:` and using `session.get()` reduces TCP and TLS overhead for each downloaded image or chunk, significantly boosting performance.
**Action:** Use `requests.Session()` for repetitive requests to the same server.
