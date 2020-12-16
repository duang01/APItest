"""一些公用的方法封装"""
import inspect
import json
import logging

import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver


from uiframe.page.wrapper import handle_black


class BasePage:
    _params = {}  # 用来存字典一些变量

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def screenshot(self, name):
        self._driver.save_screenshot(name)

    def finds(self, locator, value: str = None):
        elements: list
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)
        return elements

    @handle_black
    def find(self, locator, value: str = None):    # 封装定位元素方法
        logging.info(locator)
        logging.info(value)
        element: WebElement
        if isinstance(locator, tuple):     # 判断传入的参数是否为一个元组
            element = self._driver.find_element(*locator)    # *locator 代表解元组
        else:
            element = self._driver.find_element(locator, value)
        return element

    @handle_black
    def find_and_get_text(self, locator, value: str = None):    # 处理定位元素后去点击等操作跳出来的弹窗
        element: WebElement
        if isinstance(locator, tuple):     # 判断传入的参数是否为一个元组
            element_text = self._driver.find_element(*locator).text    # *locator 代表解元组
        else:
            element_text = self._driver.find_element(locator, value).text
        return element_text

    def steps(self, path):
        with open(path, encoding="utf-8") as f:
            name = inspect.stack()[1].function   # inspect 查看谁调用的
            steps = yaml.safe_load(f)[name]
            # 利用序列化与反序列化进行变量替换
        raw = json.dumps(steps)
        for key, value in self._params.items():
            raw = raw.replace(f'${{{key}}}', value)
        steps = json.loads(raw)

        for step in steps:
            if "action" in step.keys():
                action = step["action"]
                if "click" == action:
                    self.find(step["by"], step["locator"]).click()
                if "send" == action:
                    self.find(step["by"], step["locator"]).send_keys(step["value"])
                if "len > 0" == action:
                    eles = self.finds(step["by"], step["locator"])
                    return len(eles) > 0




