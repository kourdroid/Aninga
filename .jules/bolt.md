## 2024-05-18 - Small Chunk Size Anti-Pattern in Large Video Downloads
**Learning:** Using a small chunk size (e.g., 1KB / 1024 bytes) with `response.iter_content` when downloading large video files, combined with a progress bar like `tqdm`, causes massive CPU overhead and disk I/O thrashing because `tqdm` updates progress and writes to disk for every tiny chunk downloaded.
**Action:** When downloading large files, use a larger chunk size (e.g., 1MB / `1024*1024`) to significantly reduce the frequency of progress bar updates and disk write operations, improving performance.
## 2024-10-24 - Requests Connection Pooling
**Learning:** Python's `requests` library does not automatically pool connections across independent `requests.get()` calls. This means repetitive loops downloading resources from the same host suffer significant TCP and SSL handshake overhead for every single file.
**Action:** Always wrap repetitive `requests` operations to the same host in a `with requests.Session() as session:` context manager to reuse underlying socket connections and eliminate handshake latency.
