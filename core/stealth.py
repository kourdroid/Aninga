import time
import random

def get_random_delay(min_sec: float = 1.0, max_sec: float = 3.5) -> float:
    """Return a randomized delay to simulate human jitter"""
    return random.uniform(min_sec, max_sec)

def simulate_human_behavior(driver):
    """
    Perform random scroll and mouse movements to build trust
    before doing targeted actions on a website protected by Cloudflare/DDoS-Guard.
    """
    time.sleep(get_random_delay(0.5, 1.5))
    
    # Inject smooth scrolling javascript
    scroll_script = """
    window.scrollBy({
        top: Math.floor(Math.random() * 600) + 200, 
        left: 0, 
        behavior: 'smooth'
    });
    """
    try:
        driver.execute_script(scroll_script)
    except Exception:
        pass
        
    time.sleep(get_random_delay(1.0, 2.5))
