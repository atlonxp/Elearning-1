from __future__ import absolute_import
import xadmin
from .models import UserSettings, Log
from xadmin.layout import *

from django.utils.translation import ugettext_lazy as _, ugettext

# from xadmin import views


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

from xadmin import views
 
@xadmin.sites.register(views.BaseAdminView)
class BaseSetting(object):
    # 開啟主題功能
    enable_themes = True
    use_bootswatch = True

class GlobalSetting(object):
    # 设置base_site.html的Title
    site_title = 'NUTC_Elearning'
    # 设置base_site.html的Footer
    site_footer  = 'andy112247@gmail.com'
    # menu_style = 'accordion'
xadmin.site.register(views.CommAdminView, GlobalSetting)



class UserSettingsAdmin(object):
    model_icon = 'fa fa-cog'
    hidden_menu = True

xadmin.site.register(UserSettings, UserSettingsAdmin)

class LogAdmin(object):

    def link(self, instance):
        if instance.content_type and instance.object_id and instance.action_flag != 'delete':
            admin_url = self.get_admin_url('%s_%s_change' % (instance.content_type.app_label, instance.content_type.model), 
                instance.object_id)
            return "<a href='%s'>%s</a>" % (admin_url, _('Admin Object'))
        else:
            return ''
    link.short_description = ""
    link.allow_tags = True
    link.is_column = False

    list_display = ('action_time', 'user', 'ip_addr', '__str__', 'link')
    list_filter = ['user', 'action_time']
    search_fields = ['ip_addr', 'message']
    model_icon = 'fa fa-cog'

xadmin.site.register(Log, LogAdmin)
