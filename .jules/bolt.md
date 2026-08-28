## 2024-05-18 - Small Chunk Size Anti-Pattern in Large Video Downloads
**Learning:** Using a small chunk size (e.g., 1KB / 1024 bytes) with `response.iter_content` when downloading large video files, combined with a progress bar like `tqdm`, causes massive CPU overhead and disk I/O thrashing because `tqdm` updates progress and writes to disk for every tiny chunk downloaded.
**Action:** When downloading large files, use a larger chunk size (e.g., 1MB / `1024*1024`) to significantly reduce the frequency of progress bar updates and disk write operations, improving performance.
## 2026-05-27 - Connection Pooling Overhead in Bulk Downloads
**Learning:** Independent `requests.get()` calls do not use connection pooling. This causes repetitive TCP/SSL handshakes overhead when downloading multiple images or videos from the same host, severely impacting performance during bulk downloads.
**Action:** Use `requests.Session()` within a `with` context manager when making multiple requests (like downloading pages of manga or episodes of anime) to eliminate overhead and ensure proper socket cleanup.
