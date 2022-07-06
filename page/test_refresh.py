from base.basepage import BasePage
from selenium.webdriver.common.by import By

class Refresh(BasePage):
    url = "https://opensea.io/assets/ethereum/0x495f947276749ce646f68ac8c248420045cb7b5e/60577518981592662729936491994831767198268555683308385638080151811416695767041"
    refresh_button = (By.XPATH,'//div[@class="item--collection-toolbar-wrapper"]/div[@class="sc-1xf18x6-0 sc-1twd32i-0 sc-1skvztv-1 haVRLx kKpYwv kgqWIT"]/button[1]')
    msg = (By.XPATH,'//div[@class="sc-1xf18x6-0 sc-1twd32i-0 eAciso kKpYwv"]/parent::div')

    def click_refresh(self):
        self.visit(self.url)
        self.click(self.refresh_button)
        self.wait(2)
        self.loc_wait(self.msg)
        return self.loc_text(self.msg)


