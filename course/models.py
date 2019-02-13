# course/models.py

from datetime import datetime

from django.db import models



from users.models import UserProfile

class Course(models.Model):
# 1. 課程名稱 
# 2. 課程簡介
# 3. 課程預覽圖

    '''課程'''
    name = models.CharField("課程名稱",max_length=50)
    desc = models.CharField("課程簡介",max_length=300)
    image = models.ImageField("封面圖",upload_to="courses/%Y/%m",max_length=100)
    # is_banner = models.BooleanField('是否輪播',default=False)
    add_time = models.DateTimeField("添加時間",default=datetime.now,)
    likes = models.ManyToManyField(UserProfile)

    class Meta:
        verbose_name = "課程"
        verbose_name_plural = verbose_name

    def get_zj_nums(self):
        #獲取課程的章節數
        return self.lesson_set.all().count()
    get_zj_nums.short_description = '章節數'   #在後台顯示的名稱

    def go_to(self):
        from django.utils.safestring import mark_safe
        #mark_safe後就不會轉義
        return mark_safe("<a href='https://www.google.com.tw/'>跳轉</a>")
    go_to.short_description = "跳轉"

    def get_course_lesson(self):
        #獲取課程所有章節
        return self.lesson_set.all()

    def get_learn_users(self):
        #獲取這門課程的學習用戶
        return self.usercourse_set.all()[:5]

    def __str__(self):
        return self.name


# class BannerCourse(Course):
#     '''顯示輪播課程'''
#     class Meta:
#         verbose_name = '輪播課程'
#         verbose_name_plural = verbose_name
#         #這裡必須設置proxy=True，這樣就不會在生成一張表，而且具有Model的功能
#         proxy = True


class Lesson(models.Model):
# 1. 課程名稱 
# 2. 章節名稱
# 3. 添加時間
# 4. 章節內容

    '''課程章節'''
    course = models.ForeignKey(Course,verbose_name='課程名稱',on_delete=models.CASCADE)
    name = models.CharField("章節名稱",max_length=100)
    add_time = models.DateTimeField("添加時間",default=datetime.now)
    desc = models.TextField("章節內容")
    user = models.ForeignKey(UserProfile,verbose_name='上課學生',on_delete=models.CASCADE)
    # 記錄上課學生

    class Meta:
        verbose_name = "章節"
        verbose_name_plural = verbose_name

    # def get_lesson_vedio(self):
    #     #獲取章節所有影片
    #     return self.video_set.all()

    def __str__(self):
        return '《{0}》課程的章節 >> {1}'.format(self.course, self.name)


class Words(models.Model):
# 1. Lesson
# 1. 單字 
# 2. kk音標
# 3. 詞性
# 4. 中文
# 4. 解釋
# 5. 例句

    '''單字'''
    lesson = models.ForeignKey(Lesson,verbose_name='章節名稱',on_delete=models.CASCADE)
    words = models.CharField("單字",max_length=100)
    kk = models.CharField("kk音標",max_length=100,null=True)
    subject = models.CharField("詞性",max_length=100,null=True)
    chinese = models.CharField("中文",max_length=100,null=True)
    
    description = models.CharField("解釋",max_length=100,null=True)
    example = models.CharField("例句",max_length=100,null=True)

    # 記錄上課學生

    class Meta:
        verbose_name = "單字"
        verbose_name_plural = verbose_name

    # def get_lesson_vedio(self):
    #     #獲取章節所有影片
    #     return self.video_set.all()

    def __str__(self):
        return '《{0}》章節的單字 >> {1}'.format(self.lesson, self.words)


class quiz(models.Model):
    lesson = models.ForeignKey(Lesson,verbose_name='章節名稱',on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile,verbose_name='做題學生',on_delete=models.CASCADE)
    add_time = models.DateTimeField("添加時間",default=datetime.now)
    question = models.TextField("問題題目")
    stu_answer = models.TextField("學生回答")
    class Meta:
        verbose_name = "測驗"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '《{0}》章節的問題 >> {1}'.format(self.lesson, self.question)