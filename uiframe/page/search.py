

from uiframe.page.base_page import BasePage


class Search(BasePage):

    def search(self, name):
        self._params["name"] = name
        self.steps("./../yaml/search.yaml")
        # with open("./../yaml/search.yaml", encoding="utf-8") as f:
        #     steps = yaml.safe_load(f)
        # for step in steps:
        #     element = None
        #     if "by" in step.keys():
        #         element = self.find(step["by"], step["locator"])
        #     if "action" in step.keys():
        #         action = step["action"]
        #         if "click" == action:
        #             element.click()
        #         if "send" == action:
        #             element.send_keys(step["value"])

        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        # self.find(By.ID, 'com.xueqiu.android:id/search_input_text').send_keys("alibaba")
        # self.find(By.XPATH, '//*[@text="BABA"]').click()
        # # self.find(By.XPATH, '//*[contains(@resource-id, "ll_stock_item_container")]//*[@text="阿里巴巴"]')
        # self.find(By.XPATH,
        #           f'//*[contains(@resource-id, "ll_stock_item_container")]//*[@text="{name}"]/../..//*[@text="加自选"]').click()

    def is_choose(self, name):
        self._params["name"] = name
        return self.steps("./../yaml/search.yaml")

        # with open("./../yaml/is_choose.yaml", encoding="utf-8") as f:
        #     steps = yaml.safe_load(f)
        # for step in steps:
        #     element = None
        #     if "by" in step.keys():
        #         element = self.find(step["by"], step["locator"])
        #     if "action" in step.keys():
        #         action = step["action"]
        #         if "click" == action:
        #             element.click()
        #         if "send" == action:
        #             element.send_keys(step["value"])
        #         if "len > 0" == action:
        #             eles = self.finds(step["by"], step["locator"])
        #             return len(eles) > 0

        # ets = self.finds(By.XPATH,
        # f'//*[contains(@resource-id, "ll_stock_item_container")]//*[@text="{name}"]/../..//*[@text="已添加"]')
        # return len(ets) > 0




