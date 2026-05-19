import undetected_chromedriver as uc
from .stealth import simulate_human_behavior

def create_stealth_driver(headless: bool = True) -> uc.Chrome:
    """
    Spawns an undetected-chromedriver instance configured for maximum stealth.
    Designed exclusively to bypass Cloudflare and similar CAPTCHAs silently.
    """
    options = uc.ChromeOptions()
    if headless:
        options.add_argument('--headless')
    
    # Add robust stealth arguments
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    
    # Initialize undetected_chromedriver
    driver = uc.Chrome(options=options)
    
    # Further CDP overrides to ensure navigator.webdriver is completely scrubbed
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {
        "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        "platform": "Win32",
        "acceptLanguage": "en-US,en;q=0.9,ar;q=0.8"
    })
    
    return driver

def solve_challenge_silently(driver: uc.Chrome, url: str) -> str:
    """
    Visits a URL and handles the Javascript challenge/CAPTCHA if present.
    Returns the page source once cleared.
    """
    driver.get(url)
    simulate_human_behavior(driver)
    
    # Wait until title is no longer 'Just a moment...' 
    # or sufficient time has passed for the challenge to clear.
    import time
    max_wait = 15
    start_time = time.time()
    
    while time.time() - start_time < max_wait:
        title = driver.title.lower()
        if 'just a moment' not in title and 'attention required' not in title:
            break
        time.sleep(1)
        
    return driver.page_source
