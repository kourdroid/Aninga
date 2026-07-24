## 2024-05-18 - Small Chunk Size Anti-Pattern in Large Video Downloads
**Learning:** Using a small chunk size (e.g., 1KB / 1024 bytes) with `response.iter_content` when downloading large video files, combined with a progress bar like `tqdm`, causes massive CPU overhead and disk I/O thrashing because `tqdm` updates progress and writes to disk for every tiny chunk downloaded.
**Action:** When downloading large files, use a larger chunk size (e.g., 1MB / `1024*1024`) to significantly reduce the frequency of progress bar updates and disk write operations, improving performance.

## 2024-07-24 - Missing Connection Pooling for Bulk Image Downloads
**Learning:** Iterating `requests.get()` without a session in the `download_manga` loop creates a new TCP/SSL handshake for every single manga page image. In this codebase's architecture, which downloads hundreds of small images sequentially, this anti-pattern forms a massive bottleneck.
**Action:** Wrap iterative requests to the same host in a `with requests.Session() as session:` context manager and use `session.get()` to enable connection pooling, drastically reducing download overhead.
