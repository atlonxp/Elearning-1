# # operation/adminx.py

# import xadmin

# from .models import UserAsk, UserCourse, UserMessage, CourseComments, UserFavorite


# class UserAskAdmin(object):
#     '''用戶表單我要學習'''

#     list_display = ['name', 'mobile', 'course_name', 'add_time']
#     search_fields = ['name', 'mobile', 'course_name']
#     list_filter = ['name', 'mobile', 'course_name', 'add_time']


# #
# class UserCourseAdmin(object):
#     '''用戶課程學習'''

#     list_display = ['user', 'course', 'add_time']
#     search_fields = ['user', 'course']
#     list_filter = ['user', 'course', 'add_time']



# class UserMessageAdmin(object):
#     '''用戶消息後台'''

#     list_display = ['user', 'message', 'has_read', 'add_time']
#     search_fields = ['user', 'message', 'has_read']
#     list_filter = ['user', 'message', 'has_read', 'add_time']



# class CourseCommentsAdmin(object):
#     '''用戶評論後台'''

#     list_display = ['user', 'course', 'comments', 'add_time']
#     search_fields = ['user', 'course', 'comments']
#     list_filter = ['user', 'course', 'comments', 'add_time']



# class UserFavoriteAdmin(object):
#     '''用戶收藏後台'''

#     list_display = ['user', 'fav_id', 'fav_type', 'add_time']
#     search_fields = ['user', 'fav_id', 'fav_type']
#     list_filter = ['user', 'fav_id', 'fav_type', 'add_time']


# # 將後台管理器與models進行關聯註冊。
# xadmin.site.register(UserAsk, UserAskAdmin)
# xadmin.site.register(UserCourse, UserCourseAdmin)
# xadmin.site.register(UserMessage, UserMessageAdmin)
# xadmin.site.register(CourseComments, CourseCommentsAdmin)
# xadmin.site.register(UserFavorite, UserFavoriteAdmin)