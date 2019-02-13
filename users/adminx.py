# users/adminx.py

import xadmin

# from .models import Banner


from xadmin import views


# # 創建xadmin的最基本管理器配置，並與view綁定
# class BaseSetting(object):
#     # 開啟主題功能
#     enable_themes = True
#     use_bootswatch = True

# # 全局修改，固定寫法
# class GlobalSettings(object):
#     # 修改title
#     site_title = 'NUTC_elearning'
#     # 修改footer
#     site_footer = 'andy112247@gmail.com'
#     # 收起菜單
#     menu_style = 'accordion'


# #xadmin中這裡是繼承object，不再是繼承admin
# class EmailVerifyRecordAdmin(object):
#     # 顯示的列
#     list_display = ['code', 'email', 'send_type', 'send_time']
#     # 搜索的欄位
#     search_fields = ['code', 'email', 'send_type']
#     # 過濾
#     list_filter = ['code', 'email', 'send_type', 'send_time']


# class BannerAdmin(object):
#     list_display = ['title', 'image', 'url','index', 'add_time']
#     search_fields = ['title', 'image', 'url','index']
#     list_filter = ['title', 'image', 'url','index', 'add_time']


# xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
# xadmin.site.register(Banner,BannerAdmin)

# 將基本配置管理與view綁定
# xadmin.site.register(views.BaseAdminView,BaseSetting)

# 將title和footer訊息進行註冊
# xadmin.site.register(views.CommAdminView,GlobalSettings)