## 2024-05-18 - Small Chunk Size Anti-Pattern in Large Video Downloads
**Learning:** Using a small chunk size (e.g., 1KB / 1024 bytes) with `response.iter_content` when downloading large video files, combined with a progress bar like `tqdm`, causes massive CPU overhead and disk I/O thrashing because `tqdm` updates progress and writes to disk for every tiny chunk downloaded.
**Action:** When downloading large files, use a larger chunk size (e.g., 1MB / `1024*1024`) to significantly reduce the frequency of progress bar updates and disk write operations, improving performance.

## 2024-06-09 - Missing Connection Pooling Anti-Pattern in Bulk Downloads
**Learning:** Using independent `requests.get()` calls in a loop for downloading multiple images or episodes from the same host causes significant repetitive TCP/SSL handshake overhead.
**Action:** Always instantiate and use a `requests.Session()` block (with a context manager) when making multiple requests to the same host to eliminate repetitive handshake overhead and utilize connection pooling.
