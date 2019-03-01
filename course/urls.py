from django.urls import path
from course import views


app_name = 'course'
urlpatterns = [
    path('', views.indexView, name='index'),
    path('course', views.course, name='course'),
    path('addcourse/', views.addcourse, name='addcourse'),
    path('courseRead/<int:courseId>/', views.courseRead, name='courseRead'),
    path('courseUpdate/<int:courseId>/', views.courseUpdate, name='courseUpdate'),
    path('courseDelete/<int:courseId>/', views.courseDelete, name='courseDelete'),
    path('courseSearch/', views.courseSearch, name='courseSearch'),


    path('wordUpdate/<int:WordsId>/', views.wordUpdate, name='wordUpdate'),



    path('courseLike/<int:courseId>/', views.courseLike, name='courseLike'),
    # path('dashboard', views.dashboardView, name='dashboard'),

]