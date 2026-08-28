## 2024-05-18 - Small Chunk Size Anti-Pattern in Large Video Downloads
**Learning:** Using a small chunk size (e.g., 1KB / 1024 bytes) with `response.iter_content` when downloading large video files, combined with a progress bar like `tqdm`, causes massive CPU overhead and disk I/O thrashing because `tqdm` updates progress and writes to disk for every tiny chunk downloaded.
**Action:** When downloading large files, use a larger chunk size (e.g., 1MB / `1024*1024`) to significantly reduce the frequency of progress bar updates and disk write operations, improving performance.

## 2024-05-18 - Missing Connection Pooling in Loops
**Learning:** The application historically uses standalone `requests.get()` calls inside loops for bulk media downloads. This causes significant overhead because a new TCP/SSL handshake is negotiated for every single image or video chunk.
**Action:** Always instantiate and use `requests.Session()` within a `with` context manager when making multiple requests to the same host or during bulk download loops to eliminate repetitive handshake overhead.
