import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
def brother(ip_adress):
    '''
    Get Data from Brother printers by using 'urllib.request'. If site have Authorization, will call function to get Data with Authorization.
    '''
    my_request = urllib.request.urlopen("http://%s/general/information.html?kind=item" % ip_adress)
    my_HTML = my_request.read().decode()
    if 'Counter' not in my_HTML:
        return get_html_brother_pass(ip_adress)
    else:
        x = my_HTML.find("Counter")
        y = my_HTML[x:].find("</dd>")
        count = my_HTML[x:x + y].split('</dt><dd>')[1]
        return count


def get_html_brother_pass(ip_adress):
    '''
    Function to get Data with Authorization.
    '''
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    WebDriver = webdriver.Chrome(options=options)      #options=options
    WebDriver.get("http://%s/general/status.html" %ip_adress)
    WebDriver.find_element(By.ID,"LogBox").send_keys("initpass")
    WebDriver.find_element(By.ID, "LogBox").send_keys(Keys.RETURN)
    WebDriver.get("http://%s/general/information.html?kind=item" %ip_adress)
    my_HTML = WebDriver.page_source
    WebDriver.close()
    x = my_HTML.find("Counter")
    y = my_HTML[x:].find("</dd>")
    count = my_HTML[x:x + y].split('</dt><dd>')[1]
    return count
if __name__ == "__main__":
    print(brother('10.1.2.99'))
    #print(brother('10.1.2.101'))