from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import chromedriver_autoinstaller # pip install chromedriver-autoinstaller

chromedriver_autoinstaller.install() # To update your chromedriver automatically


# Get free proxies for rotating
def get_free_proxies(driver):
    driver.get('https://sslproxies.org')# https://www.us-proxy.org

    table = driver.find_element(By.TAG_NAME, 'table')
    thead = table.find_element(By.TAG_NAME, 'thead').find_elements(By.TAG_NAME, 'th')
    tbody = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')

    headers = []
    for th in thead:
        headers.append(th.text.strip())

    proxies = []
    for tr in tbody:
        proxy_data = {}
        tds = tr.find_elements(By.TAG_NAME, 'td')
        for i in range(len(headers)):
            proxy_data[headers[i]] = tds[i].text.strip()
        proxies.append(proxy_data)
    driver.close()
    for proxy in proxies:
        if  proxy["Code"] == "FR":
            print(proxy["IP Address"] + ":"+ proxy["Port"])
            return proxy["IP Address"] + ":"+ proxy["Port"]
#driver = webdriver.Chrome()
#free_proxy = get_free_proxies(driver)

def Calc(element):
    try:
        minute = element.split(":")[0]
        second = element.split(":")[1]
        duration = int(minute)*60 + int(second)
        return duration
    except:
        time.sleep(2)
        return Calc(element)
videoCount = int(input("Video Sayısı: "))
urlList = []
for i in range(videoCount):
    urlList.append(input(str(i+1)+". Video URL'i: "))
counter = 1

PROXY_STR = "194.233.69.90:443"
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=%s' % PROXY_STR)
browser = webdriver.Chrome()#(options=options)

firsTime = True
while True:
    print("Liste "+str(counter)+". Kez Oynatılıyor...")
    for i in range(videoCount): 
        browser.get(urlList[i])
        if firsTime:
            browser.find_element_by_css_selector('.ytp-play-button.ytp-button').click()
            firsTime = False
            browser.find_element_by_css_selector('.ytp-mute-button.ytp-button').click()
        element = browser.find_element_by_css_selector(".ytp-time-duration").text
        duration = Calc(element)
        print(str(i+1)+". video icin "+str(duration)+" sn beklenecek...")
        time.sleep(int(duration))
    counter+=1



    


