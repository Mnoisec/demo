from base.basepage import BasePage
from selenium.webdriver.common.by import By

class Refresh(BasePage):
    url = "https://opensea.io/assets/matic/0xecc82095b2e23605cd95552d90216faa87606c40/3305"
    refresh_button = (By.XPATH,'//div[@class="item--collection-toolbar-wrapper"]/div[@class="sc-1xf18x6-0 sc-1twd32i-0 sc-1skvztv-1 haVRLx kKpYwv kgqWIT"]/button[1]')
    msg = (By.XPATH,'//div[@class="sc-1xf18x6-0 sc-1twd32i-0 eAciso kKpYwv"]/parent::div')

    def click_refresh(self):
        self.visit(self.url)
        self.click(self.refresh_button)
        self.wait(2)
        self.loc_wait(self.msg)
        return self.loc_text(self.msg)


