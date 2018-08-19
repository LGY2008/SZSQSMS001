from Page.page_sms import PageSMS
from Page.page_setting import PageSetting
# 声明统一入口类
class PageExit():
    def __init__(self,driver):
        self.driver=driver
    # 获取setting页面对象
    def page_get_setting_object(self):
        return PageSetting(self.driver)
    # 获取sms页面对象
    def page_get_sms_object(self):
        return PageSMS(self.driver)