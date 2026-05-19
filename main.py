import os
import time
import requests
from PIL import Image
from tqdm import tqdm
import customtkinter as ctk
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

icon = Image.open('logo.ico')
extension_path = './adblock.crx'

def download_manga():
    manga_link = manga_urlInput.get()
    manga_range = manga_rangeInput.get()
    destination = manga_destinationInput.get()
    img_class = manga_classInput.get()
    driver = None
    try:
        # Create the destination directory if it doesn't exist
        if not os.path.exists(destination):
            os.makedirs(destination)
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(manga_link)

        # Extract the base URL and manga ID from the given link
        base_url = "/".join(manga_link.split("/")[:-1])

        # Loop through the specified range of pages and download images
        start_page, end_page = map(int, manga_range.split('-'))

        for page_num in range(start_page, end_page + 1):
            url = f"{base_url}/{page_num}"
            print(f"Downloading images from: {url}")

            driver.get(url)
            time.sleep(2)  # Allow time for dynamic content to load, adjust as needed

            soup = BeautifulSoup(driver.page_source, "html.parser")
            img_tags = soup.find_all('img', {'class': img_class})

            for idx, img_tag in enumerate(img_tags):
                img_url = img_tag.get('src')
                img_response = requests.get(img_url, stream=True)
                img_name = f"page_{page_num}_img_{idx + 1}.png"
                img_path = os.path.join(destination, img_name)

                with open(img_path, 'wb') as img_file:
                    for chunk in img_response.iter_content(chunk_size=8192):
                        img_file.write(chunk)

                print(f"Downloaded: {img_path}")

    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        if driver:
            driver.quit()
    
def download_anime(quality):
    import threading
    import asyncio
    
    def _run_async():
        asyncio.run(download_anime_async(quality))
        
    # Start thread to avoid freezing customtkinter UI
    threading.Thread(target=_run_async, daemon=True).start()

async def download_anime_async(quality):
    from core.manager import PluginManager
    from core.downloader import AsyncDownloader
    from core.browser import create_stealth_driver
    from urllib.parse import urlparse
    import time
    from tqdm import tqdm

    anime_link = anime_urlInput.get()
    anime_range = anime_rangeInput.get()
    destination = anime_destinationInput.get()
    
    print("Loading plugins...")
    manager = PluginManager()
    manager.load_plugins()
    
    domain = urlparse(anime_link).netloc.replace('www.', '')
    
    target_plugin = None
    for p in manager.get_all_plugins():
        if p.domain in domain:
            target_plugin = p
            break
            
    if not target_plugin:
        print(f"[Error] No plugin found for domain: {domain}")
        return
        
    print(f"Using plugin: {target_plugin.name}")
    
    # Initialize the Stealth Driver conditionally based on known protections
    driver = None
    if "blkom" in domain or "topcinemaa" in domain:
        print("Engaging Stealth CAPTCHA Browser...")
        driver = create_stealth_driver()
        
    start_page, end_page = map(int, anime_range.split('-'))
    downloader = AsyncDownloader(destination)
    anime_name = anime_link.strip('/').split('/')[-1]
    
    try:
        for episode_num in range(start_page, end_page + 1):
            episode_url = f"{anime_link}/{episode_num}"
            print(f"Resolving Episode {episode_num}...")
            
            # Use plugin to resolve the direct MP4 links
            video_urls = target_plugin.resolve_download_links(episode_url, driver)
            
            if not video_urls:
                print(f"[Warning] No video links found for Episode {episode_num}")
                continue
                
            # For this simple integration, just take the first link
            target_url = video_urls[0]
            
            print(f"Downloading... [{anime_name}] => [{target_url}]")
            
            # Progress bar closure
            pbar = None
            def progress(downloaded, total):
                nonlocal pbar
                if pbar is None:
                    pbar = tqdm(total=total, unit='B', unit_scale=True, desc=f"Ep {episode_num}", leave=False)
                # Update purely the delta
                pbar.update(downloaded - pbar.n)
                
            try:
                filename = f"{anime_name}_ep{episode_num}.mp4"
                await downloader.download_file(target_url, filename, progress)
                if pbar: 
                    pbar.close()
                print(f"\nEpisode {episode_num} downloaded successfully.")
                print('='*50)
            except Exception as e:
                if pbar: pbar.close()
                print(f"\nError downloading Episode {episode_num}: {e}")
                
    finally:
        if driver:
            driver.quit()
        print("Download Sequence Completed.")
        
window = ctk.CTk()
window.title("Aninga")
ctk.set_appearance_mode('dark')
window.geometry('1280x720')
window.resizable(False, False)
window.iconbitmap('logo.ico'
                  )


## Variables:

heading1 = ('Open Sans', 64, 'bold')
heading2 = ('Open Sans', 32, 'bold')
heading3 = ('Open Sans', 24, 'bold')
p = ('Open Sans', 20)
primary = '#c03238'
hover_primary = '#d10b0b'
bgColor = '#03070B'
inputBgColor = '#1A1B25'

## End of Variables


bg_image = ctk.CTkImage(Image.open('background.png'), size=(1280,120))

logoFrame = ctk.CTkFrame(master=window, width=1280, height=120, fg_color=bgColor)
logoFrame.place(x=0,y=0)

image_label = ctk.CTkLabel(logoFrame, image=bg_image, text="")
image_label.pack()


animeFrame = ctk.CTkFrame(master=window, width=640, height=600,fg_color=bgColor, bg_color=bgColor)
animeFrame.place(x=640, y=120)

mangaFrame = ctk.CTkFrame(master=window, width=640, height=600,fg_color=bgColor, bg_color=bgColor)
mangaFrame.place(x=0,y=120)

# ========================== Manga Section =========================

mangaTitle = ctk.CTkLabel(master=mangaFrame, text='Manga Downloader', font=heading2,text_color=primary)
mangaTitle.place(x=168,y=58)

manga_urlInput = ctk.CTkEntry(mangaFrame,width=500,height=50,corner_radius=60,fg_color=inputBgColor ,font=p,border_width=0, placeholder_text='Manga Link (e.g. without page number)')
manga_urlInput.place(x=70,y=162)

manga_rangeInput = ctk.CTkEntry(mangaFrame,width=500,height=50,corner_radius=60,fg_color=inputBgColor,font=p,border_width=0, placeholder_text='Page Range (e.g. 1-10)')
manga_rangeInput.place(x=70,y=240)

manga_destinationInput = ctk.CTkEntry(mangaFrame,width=500,height=50,corner_radius=60,fg_color=inputBgColor,font=p,border_width=0, placeholder_text='Enter the Destination')
manga_destinationInput.place(x=70,y=317)

manga_classInput = ctk.CTkEntry(mangaFrame,width=500,height=50,corner_radius=60,fg_color=inputBgColor,font=p,border_width=0, placeholder_text='Enter the Class of Image')
manga_classInput.place(x=70,y=394)

manga_downBtn = ctk.CTkButton(mangaFrame ,command=download_manga, corner_radius=64, width=260 , height=50,fg_color=primary, border_width=0, text='Download',font=heading3, hover_color=hover_primary, cursor='hand2')
manga_downBtn.place(x=189,y=474)

# ========================== Anime Section =========================


animeTitle = ctk.CTkLabel(master=animeFrame, text='Anime Downloader', font=heading2,text_color=primary)
animeTitle.place(x=168,y=58)

anime_urlInput = ctk.CTkEntry(animeFrame,width=500,height=50,corner_radius=60,fg_color=inputBgColor ,font=p,border_width=0, placeholder_text='Anime Link (e.g. without episode number)')
anime_urlInput.place(x=70,y=162)

anime_rangeInput = ctk.CTkEntry(animeFrame,width=500,height=50,corner_radius=60,fg_color=inputBgColor,font=p,border_width=0, placeholder_text='Episode Range (e.g. 1-25)')
anime_rangeInput.place(x=70,y=240)

anime_destinationInput = ctk.CTkEntry(animeFrame,width=500,height=50,corner_radius=60,fg_color=inputBgColor,font=p,border_width=0, placeholder_text='Enter the Destination')
anime_destinationInput.place(x=70,y=317)

qFrame = ctk.CTkFrame(animeFrame,width=500,height=50,fg_color=bgColor, bg_color=bgColor)
qFrame.place(x=70, y=397)

quality_var = ctk.StringVar(value='720p')

q1 = ctk.CTkRadioButton(qFrame, text='360p', font=heading3, fg_color=primary,hover_color=hover_primary, variable=quality_var, value='360p', cursor='hand2')
q1.place(x=0, y=9)

q2 = ctk.CTkRadioButton(qFrame, text='480p', font=heading3, fg_color=primary,hover_color=hover_primary, variable=quality_var, value='480p', cursor='hand2')
q2.place(x=135, y=9)

q3 = ctk.CTkRadioButton(qFrame, text='720p', font=heading3, fg_color=primary,hover_color=hover_primary, variable=quality_var, value='720p', cursor='hand2')
q3.place(x=269, y=9)

q4 = ctk.CTkRadioButton(qFrame, text='1080p', font=heading3, fg_color=primary,hover_color=hover_primary, variable=quality_var, value='1080p', cursor='hand2')
q4.place(x=402, y=9)

anime_downBtn = ctk.CTkButton(animeFrame,command=lambda: download_anime(quality_var.get(),), corner_radius=64, width=260 , height=50,fg_color=primary, border_width=0, text='Download',font=heading3,hover_color=hover_primary, cursor='hand2')
anime_downBtn.place(x=189,y=474)

# ========================== End Section =========================


window.mainloop()
