"""针对App的一些基本操作的封装"""
from appium import webdriver

from uiframe.page.base_page import BasePage
from uiframe.page.main import Main


class App(BasePage):

    def start(self):
        # appium_server 启动参数设置
        if self._driver == None:
            caps = {}
            caps['platformName'] = 'Android'
            caps['platformVersion'] = '9'
            caps['deviceName'] = '79d70e23'

            # app信息
            caps['appPackage'] = 'com.xueqiu.android'  # 包名
            caps['appActivity'] = '.view.WelcomeActivityAlias'  # 启动名

            # 输入法
            caps['unicodeKeyboard'] = 'true'  # 支持中文输入，而且不会乱跳
            caps['resetKeyboard'] = 'true'  # 运行结束后删除appium键盘
            caps['noReset'] = 'true'  # 不做应用清除.
            caps['skipServerInstallation'] = True    # 跳过appium server监听包的安装
            caps['skipDeviceInitialization'] = True  # 跳过设备的初始化，不是初次运行

            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self._driver.launch_app()

        self._driver.implicitly_wait(10)

        return self

    def restart(self):

        pass

    def stop(self):

        pass

    def main(self) -> Main:

        return Main(self._driver)
