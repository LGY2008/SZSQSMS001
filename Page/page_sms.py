from selenium.webdriver.common.by import By

from Base.base import Base
import Page
class PageSMS(Base):
    """
    一、短信操作步骤
	1. 点击添加短信
	2. 收入手机号
	3. 输入短信内容
	4. 点击发送按钮
	5. 长按短信内容-->删除
	6. 确认删除

    """
    # 点击添加短信按钮操作和输入手机号码
    def page_add_sms_and_phone(self,phone):
        self.base_click_btn(Page.sms_add_sms)
        self.base_input_text(Page.sms_res_phone,phone)
    # 输入短信内容
    def page_input_sms_text(self,value):
        self.base_input_text(Page.sms_input_sms,value)
    # 点击发送按钮
    def page_send_sms_btn(self):
        self.base_click_btn(Page.sms_send_sms_btn)
    # 删除短信
    def page_delete_sms_list(self):
        # 获取所有短信列表
        sms_list=self.base_get_sms_list(Page.sms_get_sms_list)
        print("列表长度为：",len(sms_list))
        for i in range(len(sms_list)):
            # 备用-杀手锏
            # sms_list = self.base_get_sms_list( Page.sms_get_sms_list )
            # 获取要删除短信的内容  存储在text---》判断text在不在现在所有列表中
            self.text=self.base_get_text2(sms_list[0])
            print("获取要准备删除的短信内容为：",self.text)
            # 长按
            self.base_long_press_element( sms_list[0] )
            # 点击删除短信
            self.base_xpath_click("删除")
            # 点击确定删除短信按钮
            self.base_click_btn( Page.sms_delete_sms_btn )
            print("删除【%s】内容成功"%self.text)
            if self.get_result_list():
                # 断言
                assert self.text not in self.get_result_list()
                print("断言成功：%s短信列表没有%s内容啦！"%(self.text,self.get_result_list()))
    # 断言 获取结果  封装
    def get_result_list(self):
        try:
            sms_list=self.base_get_sms_list(Page.sms_get_sms_list)
            return [i.text for i in sms_list]
        except:
            return False

    # 断言 结果列表是否成功
    def if_sms_list(self):
        try:
            self.base_find_elements(Page.sms_get_sms_list)
            return False
        except:
            return True

