      #本脚本存放元素定位的表达式

# 快速复制  ctrl + d   删除 ctrl + y
from selenium.webdriver.common.by import By

#启动应用的包名和启动名
sms_app_package = "com.android.mms"
sms_app_activity = ".ui.ConversationList"

#发送短信功能
sms_add_btn = By.ID,"com.android.mms:id/action_compose_new"
sms_edit_receive_number = By.ID,"com.android.mms:id/recipients_editor"
sms_edit_send_content = By.ID,"com.android.mms:id/embedded_text_editor"
sms_btn_send = By.ID,"com.android.mms:id/send_button_sms"

from selenium.webdriver.common.by import By

sms_app_package = "com.android.mms"
sms_app_activity = ".ui.ConversationList"

sms_app_activity = By.ID,"com.android.mms:id/action_compose_new"
sms_edit_receive_number = By.ID,"com.android.mms:id/recipients_editor"
sms_edit_send_content = By.ID,"com.android.mms:id/embedded_text_editor"
sms_btn_send = By.ID,"com.android .mms:"