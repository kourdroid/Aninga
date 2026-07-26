## 2024-05-18 - Small Chunk Size Anti-Pattern in Large Video Downloads
**Learning:** Using a small chunk size (e.g., 1KB / 1024 bytes) with `response.iter_content` when downloading large video files, combined with a progress bar like `tqdm`, causes massive CPU overhead and disk I/O thrashing because `tqdm` updates progress and writes to disk for every tiny chunk downloaded.
**Action:** When downloading large files, use a larger chunk size (e.g., 1MB / `1024*1024`) to significantly reduce the frequency of progress bar updates and disk write operations, improving performance.
## 2024-05-19 - Connection Pooling in Bulk Downloads
**Learning:** Multiple iterative HTTP requests to the same host using `requests.get()` inside loops cause redundant TCP and SSL handshakes for every downloaded image or episode, leading to high network overhead and latency.
**Action:** Always wrap loops that make iterative requests to the same host in a `with requests.Session() as session:` context manager and use `session.get()` to reuse connections and reduce network overhead.
