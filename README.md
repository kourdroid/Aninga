## Aninga - A Manga and Anime Downloader

**Download your favorite anime and manga with ease!**

Aninga is a Python GUI application designed to simplify downloading anime and manga content from the web. It boasts a user-friendly interface, support for popular websites, and options for selecting quality and destination folders.

**ScreenShots**
[]!()

**Features:**

* Download anime episodes in various qualities (360p, 480p, 720p, 1080p)
* Download manga chapters as images
* User-friendly GUI with a dark theme
* Support for custom image classes for manga downloads
* Integrates with an adblocker extension for uninterrupted downloads

**Getting Started:**

1. Clone or download this repository.
2. Install required libraries:

```bash
pip install -r requirements.txt
```
3. Run the main application file:
```
python main.py
```
**Usage:**

**Manga Download:**

1. Enter the manga link (without page number).
2. Specify the chapter range to download (e.g., 1-10).
3. Enter the destination folder.
4. Provide the CSS class of the image element containing manga pages.
5. Click the "Download" button.

**Anime Download:**

1. Enter the anime link (without episode number).
2. Specify the episode range to download (e.g., 1-25).
3. Enter the destination folder.
4. Select the desired video quality.
5. Click the "Download" button.

**Notice**
- the manga download is working just with this site: https://3asq.org/
- the anime download is working just with www.blkom.com
  
**Troubleshooting:**

* **Website Incompatibility:** If issues arise with a specific website, adjust the CSS class or selectors in the code.
* **Download Errors:** Check your internet connection and website accessibility.

**Contributing:**

We welcome contributions! Submit issues or pull requests to improve Aninga.

**License:**

This project is licensed under the MIT License.

**Enjoy downloading your favorite anime and manga with Aninga!**
