from Base.base import Base
import Page
class PageSetting(Base):
    # 点击搜索按钮
    def page_click_search_btn(self):
        self.base_click_btn(Page.search_btn)
    # 输入内容
    def page_input_text(self,value):
        self.base_input_text(Page.input_text,value)
    # 点击返回按钮
    def page_click_back_btn(self):
        self.base_click_btn(Page.back_btn)