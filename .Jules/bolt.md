## 2024-07-20 - Use requests.Session for connection pooling
**Learning:** When making multiple iterative HTTP requests to the same host using Python's `requests` library, performance degrades due to redundant TCP/SSL handshakes on every request.
**Action:** Always wrap the calls in a `with requests.Session() as session:` context manager and use `session.get()` to enable connection pooling.
