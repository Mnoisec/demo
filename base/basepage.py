import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(15)
        self.driver.set_window_position(x=500, y=0)

    def visit(self,url):
        self.driver.get(url)

    def locator(self,loc):
        return self.driver.find_element(*loc)

    def input(self,loc,text):
        self.locator(loc).send_keys(text)

    def click(self,loc):
        self.locator(loc).click()

    def wait(self,time_):
        time.sleep(time_)

    def loc_text(self,loc):
        return self.locator(loc).text

    def loc_wait(self,loc,max=10,min=0.5):
        return WebDriverWait(self.driver, max, min).until((EC.presence_of_element_located(loc)))

    def quit(self):
        self.driver.quit()
