## 2024-05-18 - Small Chunk Size Anti-Pattern in Large Video Downloads
**Learning:** Using a small chunk size (e.g., 1KB / 1024 bytes) with `response.iter_content` when downloading large video files, combined with a progress bar like `tqdm`, causes massive CPU overhead and disk I/O thrashing because `tqdm` updates progress and writes to disk for every tiny chunk downloaded.
**Action:** When downloading large files, use a larger chunk size (e.g., 1MB / `1024*1024`) to significantly reduce the frequency of progress bar updates and disk write operations, improving performance.
## 2024-06-21 - Missing Connection Pooling in Loops
**Learning:** Using `requests.get()` inside loops without a session causes Python's `requests` library to open and close a new TCP/SSL connection for every single request. This is a huge performance bottleneck when downloading dozens of images/files from the same host, adding unnecessary overhead per file.
**Action:** Always instantiate and use `requests.Session()` within a `with` context manager when making multiple sequential requests (e.g., image downloading in loops) to enable connection pooling and eliminate repetitive TCP/SSL handshake overhead.
