import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def samsung(ip_adress):
    '''
    Get Data from Samsung printers by selenium.
    '''
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    WebDriver = webdriver.Chrome(options=options)  #options=options
    WebDriver.get("http://%s/sws/index.html" %ip_adress)
    time.sleep(5)
    WebDriver.find_element(By.ID, "Tab_Information").click()
    time.sleep(5)
    WebDriver.find_element(By.XPATH,
        '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]/div/div/div/'
        'ul/div/li/ul/li[3]').click()
    time.sleep(2)
    html = WebDriver.page_source
    x = html.replace("x-grid3-cell-inner x-grid3-col-5", "xxx", 2).find("x-grid3-cell-inner x-grid3-col-5")
    y = html[x:].find("</div>")
    WebDriver.close()
    count = html[x:x + y].split('">')[2]
    return count
if __name__ == "__main__":
    print(samsung('10.1.2.200'))