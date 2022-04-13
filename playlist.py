from selenium import webdriver
import time
from datetime import timedelta

url = input("Playlist URL'i: ")
duration = input("Playlist suresi: ")
browser = webdriver.Chrome()

counter = 1
firsTime = True

while True:
    print("Liste "+str(counter)+". Kez Oynatılıyor...")
    browser.get(url)
    if firsTime:
        browser.find_element_by_css_selector('.ytp-play-button.ytp-button').click()
        firsTime = False
        browser.find_element_by_css_selector('.ytp-mute-button.ytp-button').click()
    print("Playlist icin "+str(duration)+" sn beklenecek...")
    time.sleep(int(duration))
    totalTime = int(duration) * (counter)
    print("Toplam izlenme suresi: "+str(timedelta(seconds=totalTime)))
    counter+=1



    


