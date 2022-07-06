import os
import pytest
from page.test_refresh import Refresh

class Test_Refresh():

    def test_refresh01(self,driver):
        self.re = Refresh(driver=driver)
        msg = self.re.click_refresh()
        assert "We've queued" in msg

    def teardown(self):
        self.re.quit()

if __name__ == '__main__':
    pytest.main([])
    os.system("allure generate ./temps/ -o ./report/ --clean")