## 2024-05-18 - Small Chunk Size Anti-Pattern in Large Video Downloads
**Learning:** Using a small chunk size (e.g., 1KB / 1024 bytes) with `response.iter_content` when downloading large video files, combined with a progress bar like `tqdm`, causes massive CPU overhead and disk I/O thrashing because `tqdm` updates progress and writes to disk for every tiny chunk downloaded.
**Action:** When downloading large files, use a larger chunk size (e.g., 1MB / `1024*1024`) to significantly reduce the frequency of progress bar updates and disk write operations, improving performance.
## 2024-05-24 - Requests Connection Pooling Optimization
**Learning:** Making multiple iterative HTTP requests to the same host using `requests.get()` inside a loop causes redundant TCP and SSL handshakes for every request, acting as a severe performance bottleneck for downloading many small files (like manga images).
**Action:** Always wrap iterative requests in a `with requests.Session() as session:` context manager and use `session.get()` to enable connection pooling.
