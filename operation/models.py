# # operation/models.py

# from datetime import datetime

# from django.db import models

# from course.models import Course
# from users.models import UserProfile


# class UserAsk(models.Model):
#     '''用戶諮詢'''
#     name = models.CharField('姓名',max_length=20)
#     mobile = models.CharField('手機',max_length=11)
#     course_name = models.CharField('課程名',max_length=50)
#     add_time = models.DateTimeField('添加時間',default=datetime.now)

#     class Meta:
#         verbose_name = '用戶諮詢'
#         verbose_name_plural = verbose_name

#     def __str__(self):
#         return self.name


# class CourseComments(models.Model):
#     '''課程評論'''
#     user = models.ForeignKey(UserProfile,verbose_name='用戶',on_delete=models.CASCADE)
#     course = models.ForeignKey(Course,verbose_name='課程',on_delete=models.CASCADE)
#     comments = models.CharField('評論',max_length=200)
#     add_time = models.DateTimeField('添加時間', default=datetime.now)

#     class Meta:
#         verbose_name = '課程評論'
#         verbose_name_plural = verbose_name


# class UserFavorite(models.Model):
#     '''用戶收藏'''
#     FAV_TYPE = (
#         (1,'課程'),
#         (2,'課程機構'),
#         (3,'講師')
#     )

#     user = models.ForeignKey(UserProfile,verbose_name='用戶',on_delete=models.CASCADE)
#     fav_id = models.IntegerField('數據id',default=0)
#     fav_type = models.IntegerField(verbose_name='收藏類型',choices=FAV_TYPE,default=1)
#     add_time = models.DateTimeField('添加時間', default=datetime.now)

#     class Meta:
#         verbose_name = '用戶收藏'
#         verbose_name_plural = verbose_name


# class UserMessage(models.Model):
#     user = models.IntegerField('接受用戶',default=0)
#     message = models.CharField('消息內容',max_length=500)
#     has_read = models.BooleanField('是否已讀',default=False)
#     add_time = models.DateTimeField('添加時間', default=datetime.now)

#     class Meta:
#         verbose_name = '用戶消息'
#         verbose_name_plural = verbose_name


# class UserCourse(models.Model):
#     '''用戶課程'''
#     user = models.ForeignKey(UserProfile,verbose_name='用戶',on_delete=models.CASCADE)
#     course = models.ForeignKey(Course,verbose_name='課程',on_delete=models.CASCADE)
#     add_time = models.DateTimeField('添加時間', default=datetime.now)

#     class Meta:
#         verbose_name = '用戶課程'
#         verbose_name_plural = verbose_name