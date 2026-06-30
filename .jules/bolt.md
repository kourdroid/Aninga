## 2024-05-18 - Small Chunk Size Anti-Pattern in Large Video Downloads
**Learning:** Using a small chunk size (e.g., 1KB / 1024 bytes) with `response.iter_content` when downloading large video files, combined with a progress bar like `tqdm`, causes massive CPU overhead and disk I/O thrashing because `tqdm` updates progress and writes to disk for every tiny chunk downloaded.
**Action:** When downloading large files, use a larger chunk size (e.g., 1MB / `1024*1024`) to significantly reduce the frequency of progress bar updates and disk write operations, improving performance.
## 2024-05-24 - Connection Pooling in Requests
**Learning:** Python's `requests.get` lacks connection pooling for sequential independent requests to the same host, which causes significant TCP/SSL handshake overhead in tight loops when downloading many images or videos.
**Action:** Use `with requests.Session() as session:` to pool connections for sequential downloads from the same host to reduce network latency and prevent ResourceWarnings.
