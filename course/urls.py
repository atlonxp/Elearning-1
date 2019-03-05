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
    # path('add/', views.addd, name='add'),
    path('ajax_list/', views.ajax_list, name='ajax_list'),
    path('ajax_dict/', views.ajax_dict, name='ajax_dict'),
    path('ajax_jquery/', views.ajax_jquery, name='ajax_jquery'),
    path('ajax_jquery_POST/', views.ajax_jquery_POST, name='ajax_jquery_POST'),
    path('ajax_jquery_sample/', views.ajax_jquery_sample, name='ajax_jquery_sample'),


    path('translator_Example/', views.translator_Example, name='translator_Example'),
    path('synonyms/', views.synonyms, name='synonyms'),
    path('synonymsave/', views.synonymsave, name='synonymsave'),
    path('synonymsMK/', views.synonymsMK, name='synonymsMK'),




    path('courseLike/<int:courseId>/', views.courseLike, name='courseLike'),
    # path('dashboard', views.dashboardView, name='dashboard'),

]