import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from pyautogui import click, locateCenterOnScreen, ImageNotFoundException
load_dotenv()

#Path to save music to(replace with the path you want your music saved to)
path = r"C:\Users\Jonathan King\Documents\Spotify Songs"
extension_path = r"C:\Users\Jonathan King\Documents\Self Teaching\Python\Projects\Spoofy-Auto-Download\Extensions\AddBlocker.crx"

#checks to see if path exists if it doesn't it creates the folder to save the files in
if not os.path.exists(path):
    os.makedirs(path)     
    
#download automation    
scope = "user-library-read"
chrome_options = Options()
installed = False
try:
    chrome_options.add_extension(extension_path)
    installed = True
except OSError:
    pass
driver = webdriver.Chrome(options=chrome_options)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
delim=0
results = sp.current_user_saved_tracks(50, delim)

#loop to continue the innner loop after every 50 songs
while results['items']:
    #loop to get song id from api and append to standard spotify share song link
    for idx, item in enumerate(results['items']):
        params = {"behavior": "allow", "downloadPath": path}
        driver.execute_cdp_cmd('Page.setDownloadBehavior', params)
        driver.get("https://spotifymate.com/")
        track = item['track']
        trackID = track['id']
        baseURL = "https://open.spotify.com/track/"
        songURL = baseURL + trackID
        element = driver.find_element(By.ID, "url")
        submitbutton = driver.find_element(By.ID, "send")
        sleep(1)
        element.clear()
        element.send_keys(songURL)
        submitbutton.click()
        sleep(5)
        downloadbutton = driver.find_element(By.XPATH, "//span[text()='Download Mp3']")
        downloadbutton.click()
     
       
    delim += 50
    results = sp.current_user_saved_tracks(50, delim)
        
driver.close()   