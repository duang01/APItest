
from uiframe.page.base_page import BasePage
from uiframe.page.market import Market


class Main(BasePage):
    def goto_market(self):

        # self.find(By.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']").click()
        # with open("./../yaml/main.yaml", encoding="utf-8") as f:
        #     steps = yaml.safe_load(f)
        # for step in steps:
        #     element = None
        #     if "by" in step.keys():
        #
        #         element = self.find(step["by"], step["locator"])
        #     if "action" in step.keys():
        #         action = step["action"]
        #     if "click" == action:
        #         element.click()
        #     if "send" == action:
        #         value = step["value"]
        #         print(f"send({value})")
        self.steps("./../yaml/main.yaml")
        return Market(self._driver)