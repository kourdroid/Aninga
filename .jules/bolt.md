## 2024-05-18 - Small Chunk Size Anti-Pattern in Large Video Downloads
**Learning:** Using a small chunk size (e.g., 1KB / 1024 bytes) with `response.iter_content` when downloading large video files, combined with a progress bar like `tqdm`, causes massive CPU overhead and disk I/O thrashing because `tqdm` updates progress and writes to disk for every tiny chunk downloaded.
**Action:** When downloading large files, use a larger chunk size (e.g., 1MB / `1024*1024`) to significantly reduce the frequency of progress bar updates and disk write operations, improving performance.
## 2024-06-01 - Missing Connection Pooling in Loops
**Learning:** The codebase repeatedly calls `requests.get()` inside loops when downloading images or multiple files, which creates significant TCP/SSL handshake overhead for each independent request.
**Action:** Wrap iterative download loops with `with requests.Session() as session:` and use `session.get()` to pool connections and reuse sockets, reducing latency and resource usage.
