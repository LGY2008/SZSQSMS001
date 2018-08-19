import os,sys
sys.path.append(os.getcwd())
from Page.page_setting import PageSetting
from Base.get_driver import get_driver
class TestSeting():
    def setup(self):
        # 获取driver
        self.driver=get_driver("com.android.settings",".Settings")
        # 实例化页面对象
        self.setting=PageSetting(self.driver)
    def teardown(self):
        self.driver.quit()
    # 测试函数
    def test_setting(self):
        # 点击搜索按钮
        self.setting.page_click_search_btn()
        # 输入搜索内容
        self.setting.page_input_text("wlan")
        # 点击返回按钮
        self.setting.page_click_back_btn()
    def test_sms(self):
        pass