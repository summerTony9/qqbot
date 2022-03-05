import json

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


async def get_song_id(song: str):
    driver = webdriver.Chrome()

    url = "https://music.163.com/#/search/m/?s={}".format(song)
    driver.get(url)
    driver.delete_all_cookies()

    with open('/Users/luyueti/Desktop/code/qqbot/awesome/plugins/music/cookies.txt', 'r') as cookief:
        cookieslist = json.load(cookief)
        for cookie in cookieslist:
            driver.add_cookie(cookie)
    driver.refresh()

    driver.switch_to.frame(driver.find_element(by=By.ID, value="g_iframe"))
    time.sleep(3)

    song_id = driver.find_element(by=By.CLASS_NAME, value="text").find_element(By.XPATH, './*')
    href = song_id.get_attribute('href')
    song_id = href.split('id=')[1]
    driver.close()
    return song_id
