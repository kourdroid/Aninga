## 2024-05-18 - Small Chunk Size Anti-Pattern in Large Video Downloads
**Learning:** Using a small chunk size (e.g., 1KB / 1024 bytes) with `response.iter_content` when downloading large video files, combined with a progress bar like `tqdm`, causes massive CPU overhead and disk I/O thrashing because `tqdm` updates progress and writes to disk for every tiny chunk downloaded.
**Action:** When downloading large files, use a larger chunk size (e.g., 1MB / `1024*1024`) to significantly reduce the frequency of progress bar updates and disk write operations, improving performance.
## 2024-05-18 - Connection Pooling with requests.Session
**Learning:** Iteratively calling `requests.get()` inside a loop to download multiple files from the same server establishes a new TCP connection (and performs TLS handshakes) for every single request, leading to massive network latency overheads.
**Action:** When making multiple requests to the same domain (e.g., downloading manga pages or video episodes), wrap the operations in a `with requests.Session() as session:` context manager and use `session.get()` to enable HTTP Keep-Alive, significantly speeding up batch downloads.
