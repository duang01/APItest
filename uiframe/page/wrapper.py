"""装饰器模块"""
import logging

import allure
from selenium.webdriver.common.by import By


def handle_black(func):    # 弹窗异常处理
    logging.basicConfig(level=logging.INFO)

    def wrapper(*args, **kwargs):
        from uiframe.page.base_page import BasePage
        _black_list = [
            (By.XPATH, "//*[@text='确认']"),
            (By.XPATH, "//*[@text='取消']"),
            (By.XPATH, "//*[@text='下次再说']")
        ]
        _max_num = 3  # 一次元素定位最多的异常次数
        _error_num = 0  # 定位元素的异常次数
        instance: BasePage = args[0]
        try:
            logging.info("run "+func.__name__ +"\n args: \n"+ repr(args[1:])+"\n"+repr(kwargs))
            element = func(*args, **kwargs)
            _error_num = 0  # 找到元素，异常次数归零
            instance._driver.implicitly_wait(10)
            return element

        except Exception as e:  # 异常处理逻辑：遍历异常黑名单若发现有，则处理
            # 添加截图到alluer报告中
            instance.screenshot("./../picture/err1.png")
            with open("./../picture/err.png", "rb") as f:
                content = f.read()
            allure.attach(content, attachment_type=allure.attachment_type.PNG)

            logging.error("element not found, handle black_list")
            instance._driver.implicitly_wait(1)
            if _error_num > _max_num:
                raise e
            _error_num += 1
            for ele in _black_list:
                elelist = instance.finds(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    return wrapper(*args, **kwargs)
            raise e
    return wrapper


