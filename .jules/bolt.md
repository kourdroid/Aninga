## 2024-07-21 - Connection pooling with requests.Session()
**Learning:** Making multiple iterative HTTP requests to the same host using `requests.get()` creates a new TCP and SSL connection for every image/episode downloaded. This introduces significant network overhead.
**Action:** Always wrap loop-based iterative requests in a `with requests.Session() as session:` block to reuse connections, which can dramatically speed up scraping and downloading processes.

## 2024-07-21 - Connection pooling with requests.Session()
**Learning:** Making multiple iterative HTTP requests to the same host using `requests.get()` creates a new TCP and SSL connection for every image/episode downloaded. This introduces significant network overhead.
**Action:** Always wrap loop-based iterative requests in a `with requests.Session() as session:` block to reuse connections, which can dramatically speed up scraping and downloading processes.
