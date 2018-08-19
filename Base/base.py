from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
class Base():
    def __init__(self,driver):
        self.driver=driver
    # 定位单个元素 封装
    def base_find_element(self,loc,timeout=2,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(*loc))
    # 定位一组元素 封装
    def base_find_elements(self,loc,timeout=2,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_elements(*loc))
    # 点击元素 封装
    def base_click_btn(self,loc):
        self.base_find_element(loc).click()
    # 输入元素 封装
    def base_input_text(self,loc,value):
        self.base_find_element(loc).send_keys(value)
    # 获取元素 文本值封装
    def base_get_text(self,loc):
        return self.base_find_element(loc).text
    # 获取元素 文本值封装
    def base_get_text2(self,el):
        return el.text
    # 获取一组元素
    def base_get_sms_list(self,loc):
        return self.base_find_elements(loc)
    # 长按方法 封装
    def base_long_press_element(self,el):
        TouchAction(self.driver).long_press(el,duration=2000).release().perform()
    # 单独封装个Xpath语句
    def base_xpath_click(self,text):
        self.base_click_btn((By.XPATH,"//*[contains(@text,'"+text+"')]"))
