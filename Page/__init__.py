from selenium.webdriver.common.by import By
"""
设置页面数据：
"""
search_btn=By.ID,"com.android.settings:id/search"
input_text=By.ID,"android:id/search_src_text"
back_btn=By.CLASS_NAME,"android.widget.ImageButton"

"""
短信页面数据：
"""
#添加短信
sms_add_sms=By.ID,"com.android.mms:id/action_compose_new"
#接受者电话
sms_res_phone=By.ID,"com.android.mms:id/recipients_editor"
# 输入短信内容
sms_input_sms=By.ID,"com.android.mms:id/embedded_text_editor"
#发信送短信按钮
sms_send_sms_btn=By.ID,"com.android.mms:id/send_button_sms"
# 获取短信内容列表
sms_get_sms_list=By.ID,"com.android.mms:id/text_view"
# 确定删除短信
sms_delete_sms_btn=By.ID,"android:id/button1"
"""
更多页面数据
"""