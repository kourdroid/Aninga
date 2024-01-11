import os
import time
import requests
from tqdm import tqdm
import customtkinter as ctk
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
    global destination
    global video_urls
    video_urls = []
    episode_number = []
    anime_link = anime_urlInput.get()
    anime_range = anime_rangeInput.get()
    destination = anime_destinationInput.get()
    selected_quality = quality
    driver = None
    
    extension_path = './adblock.crx'
    chrome_options = Options()
    chrome_options.add_extension(extension_path)
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    driver = webdriver.Chrome(options=chrome_options)

    

    try:      
        start_page, end_page = map(int, anime_range.split('-'))
        episode_num = start_page
        for episode_num in range(start_page, end_page + 1):
            episode_url = f"{anime_link}/{episode_num}"
            driver.get(episode_url)
            
            try:
                download_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.content-wrapper > section.play-section > div > div > div > div > div.video-info.col-xs-12 > div:nth-child(1) > div > button'))
                )

                download_button.click()

                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'panel-body'))
                )

                time.sleep(5)

                links = driver.find_elements(By.XPATH, f'//div[@class="panel-body"]//a[contains(@class, "btn-white") and contains(text(), "{selected_quality}")]')
                
                for link in links:
                    video_urls.append(link.get_attribute("href"))

            except Exception as e:
                print(f"An error occurred on page {episode_num}: {str(e)}")
            
            
            
            ## Downloading from video_urls list ##

        
        driver.quit()        
        print('='*20)         
        print(video_urls)

    except Exception as e:
        print(f"An error occurred on page {episode_num}: {str(e)}")

    finally:
        anime_name = anime_link.split('/')[-1]
        
        for episode_num in range(start_page, end_page +1):
            
            video_url = video_urls[episode_num - start_page]
            
            print(f'downloading...[{anime_name}] => [{video_url}]')
            try:
                response = requests.get(video_url, stream=True)
                file_size = int(response.headers.get('content-length', 0))
                filename = os.path.join(destination, f"{anime_name}_ep{episode_num}.mp4")
                with open(filename, 'wb') as file, tqdm(total=file_size, unit='B', unit_scale=True, desc=f"Downloading Episode {episode_num}", leave=False) as bar:
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            file.write(chunk)
                            bar.update(len(chunk))

                print(f"Episode {episode_num} downloaded successfully.")
            except Exception as e:
                print(f"An error occurred while downloading Episode {episode_num}: {str(e)}")
    

    
    
    
window = ctk.CTk()
window.title("Aninga")
ctk.set_appearance_mode('dark')
window.geometry('1280x720')
window.resizable(False, False)

## Variables:
heading1 = ('Open Sans', 64, 'bold')
heading2 = ('Open Sans', 32, 'bold')
heading3 = ('Open Sans', 24, 'bold')
p = ('Open Sans', 20)
primary = '#1573E2'
bgColor = '#03070B'
inputBgColor = '#1A1B25'

# my_image = ctk.CTkImage(bg_image, size=(1280, 720))
# # Create a label with the background image for the window
# image_label = ctk.CTkLabel(window, image=my_image, text="")
# image_label.pack()


logoFrame = ctk.CTkFrame(master=window, width=1280, height=120, fg_color=bgColor)
logoFrame.place(x=0,y=0)

logo = ctk.CTkLabel(logoFrame, text='Aninga', font=heading1, text_color=primary)
logo.place(x=524,y=10)

animeFrame = ctk.CTkFrame(master=window, width=640, height=600,fg_color=bgColor, bg_color=bgColor)
animeFrame.place(x=640, y=120)

mangaFrame = ctk.CTkFrame(master=window, width=640, height=600,fg_color=bgColor, bg_color=bgColor)
mangaFrame.place(x=0,y=120)

# ========================== Manga Section =========================

mangaTitle = ctk.CTkLabel(master=mangaFrame, text='Manga Downloader', font=heading2)
mangaTitle.place(x=168,y=58)

manga_urlInput = ctk.CTkEntry(mangaFrame,width=500,height=50,corner_radius=60,fg_color=inputBgColor ,font=p,border_width=0, placeholder_text='Manga Link without Page Number')
manga_urlInput.place(x=70,y=162)

manga_rangeInput = ctk.CTkEntry(mangaFrame,width=500,height=50,corner_radius=60,fg_color=inputBgColor,font=p,border_width=0, placeholder_text='Input The range of Episodes')
manga_rangeInput.place(x=70,y=240)

manga_destinationInput = ctk.CTkEntry(mangaFrame,width=500,height=50,corner_radius=60,fg_color=inputBgColor,font=p,border_width=0, placeholder_text='Enter the Destination')
manga_destinationInput.place(x=70,y=317)

manga_classInput = ctk.CTkEntry(mangaFrame,width=500,height=50,corner_radius=60,fg_color=inputBgColor,font=p,border_width=0, placeholder_text='Enter the Class of Image')
manga_classInput.place(x=70,y=394)

manga_downBtn = ctk.CTkButton(mangaFrame ,command=download_manga, corner_radius=64, width=260 , height=50,fg_color=primary, border_width=0, text='Download',font=heading3)
manga_downBtn.place(x=189,y=474)

# ========================== Anime Section =========================


animeTitle = ctk.CTkLabel(master=animeFrame, text='Anime Downloader', font=heading2)
animeTitle.place(x=168,y=58)

anime_urlInput = ctk.CTkEntry(animeFrame,width=500,height=50,corner_radius=60,fg_color=inputBgColor ,font=p,border_width=0, placeholder_text='Anime Link without Page Number')
anime_urlInput.place(x=70,y=162)

anime_rangeInput = ctk.CTkEntry(animeFrame,width=500,height=50,corner_radius=60,fg_color=inputBgColor,font=p,border_width=0, placeholder_text='Input The range of Episodes')
anime_rangeInput.place(x=70,y=240)

anime_destinationInput = ctk.CTkEntry(animeFrame,width=500,height=50,corner_radius=60,fg_color=inputBgColor,font=p,border_width=0, placeholder_text='Enter the Destination')
anime_destinationInput.place(x=70,y=317)

qFrame = ctk.CTkFrame(animeFrame,width=500,height=50,fg_color=bgColor, bg_color=bgColor)
qFrame.place(x=70, y=397)

quality_var = ctk.StringVar()

q1 = ctk.CTkRadioButton(qFrame, text='360p', font=heading3, fg_color=primary, variable=quality_var, value='360p')
q1.place(x=0, y=9)

q2 = ctk.CTkRadioButton(qFrame, text='480p', font=heading3, fg_color=primary, variable=quality_var, value='480p')
q2.place(x=135, y=9)

q3 = ctk.CTkRadioButton(qFrame, text='720p', font=heading3, fg_color=primary, variable=quality_var, value='720p')
q3.place(x=269, y=9)

q4 = ctk.CTkRadioButton(qFrame, text='1080p', font=heading3, fg_color=primary, variable=quality_var, value='1080p')
q4.place(x=402, y=9)

anime_downBtn = ctk.CTkButton(animeFrame,command=lambda: download_anime(quality_var.get(),), corner_radius=64, width=260 , height=50,fg_color=primary, border_width=0, text='Download',font=heading3)
anime_downBtn.place(x=189,y=474)

# ========================== End Section =========================


window.mainloop()
