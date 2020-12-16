
from uiframe.page.base_page import BasePage
from uiframe.page.search import Search


class Market(BasePage):
    def goto_search(self):

        # self.find(By.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']").click()

        return Search(self._driver)