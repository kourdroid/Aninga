## 2024-05-18 - Small Chunk Size Anti-Pattern in Large Video Downloads
**Learning:** Using a small chunk size (e.g., 1KB / 1024 bytes) with `response.iter_content` when downloading large video files, combined with a progress bar like `tqdm`, causes massive CPU overhead and disk I/O thrashing because `tqdm` updates progress and writes to disk for every tiny chunk downloaded.
**Action:** When downloading large files, use a larger chunk size (e.g., 1MB / `1024*1024`) to significantly reduce the frequency of progress bar updates and disk write operations, improving performance.

## 2024-05-18 - Missing Connection Pooling
**Learning:** Calling `requests.get()` in a loop without a session creates a new TCP connection and performs an SSL handshake for every single request, leading to massive overhead when downloading many files from the same host.
**Action:** Wrap iterative HTTP requests in a `with requests.Session() as session:` context manager to reuse the underlying TCP connections, drastically reducing latency.
