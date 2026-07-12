## 2024-05-18 - Small Chunk Size Anti-Pattern in Large Video Downloads
**Learning:** Using a small chunk size (e.g., 1KB / 1024 bytes) with `response.iter_content` when downloading large video files, combined with a progress bar like `tqdm`, causes massive CPU overhead and disk I/O thrashing because `tqdm` updates progress and writes to disk for every tiny chunk downloaded.
**Action:** When downloading large files, use a larger chunk size (e.g., 1MB / `1024*1024`) to significantly reduce the frequency of progress bar updates and disk write operations, improving performance.

## 2024-07-12 - Missing Connection Pooling in Iterative Downloads
**Learning:** Iteratively downloading many small files (like manga images) using individual `requests.get` calls creates a significant bottleneck because it forces the application to negotiate a new TCP and SSL connection for every single file.
**Action:** Always wrap loops that make iterative requests to the same host in a `with requests.Session() as session:` block and use `session.get()` to enable connection pooling and avoid redundant handshakes.
