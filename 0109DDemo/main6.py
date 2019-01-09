from selenium.webdriver import Chrome
import time
from pytube import Playlist
import os

driver = Chrome("./chromedriver")
#打開網址
driver.get("https://www.youtube.com/view_all_playlists")
driver.find_element_by_id("identifierId").send_keys("drbrhbym@gmail.com")
driver.find_element_by_id("identifierNext").click()
time.sleep(1)
driver.find_element_by_class_name("whsOnd").send_keys("Kk123456")
driver.find_element_by_id("passwordNext").click()
time.sleep(5)
for p in driver.find_elements_by_class_name("vm-video-title-text"):
    url = p.get_attribute("href")
    print(p.text, url)
    pl = Playlist(url, suppress_exception=True)
    dirname = 'youtube/' + p.text
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    pl.download_all(dirname)

time.sleep(3)
driver.close()