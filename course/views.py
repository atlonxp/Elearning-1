from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.

from course.models import Course,Lesson

from course.forms import CourseForm

from django.contrib import messages

from django.db.models.query_utils import Q

from django.views.generic.base import View


class indexView(View):
    '''
    顯示首頁
    '''
    def get(self,request):
        # return render(request, 'login.html')
        courses = {}
        for course in Course.objects.all():
            courses.update({course:Lesson.objects.filter(course=course)})

        # articles = {}
        # for article in Article.objects.all():
        #     articles.update({article:Comment.objects.filter(article=article)})

        context = {'courses':courses}
        # print(context)
        return render(request, 'course/index.html', context)

class dashboardView(View):
    '''
    顯示dashboard
    '''
    def get(self,request):
        # return render(request, 'login.html')
        courses = {}
        for course in Course.objects.all():
            courses.update({course:Lesson.objects.filter(course=course)})

        # articles = {}
        # for article in Article.objects.all():
        #     articles.update({article:Comment.objects.filter(article=article)})

        context = {'courses':courses}
        # print(context)
        return render(request, 'course/sbadmin2.html', context)


def course(request):
    '''
    Render the course page
    '''
    # courses = Course.objects.all()

    courses = {}
    for course in Course.objects.all():
        courses.update({course:Lesson.objects.filter(course=course)})

    # articles = {}
    # for article in Article.objects.all():
    #     articles.update({article:Comment.objects.filter(article=article)})

    context = {'courses':courses}
    # print(context)
    return render(request, 'course/course.html', context)

def addcourse(request):
    '''
    Create a new article instance
        1. If method is GET, render an empty form
        2. If method is POST, perform form validation and display error messages if the form is invalid
        3. Save the form to the model and redirect the user to the article page
    '''
    # TODO: finish the code
    # return render(request, 'course/course.html')
    template = 'course/addcourse.html'
    # template = 'courses/coursesUpdate.html'
    if request.method == 'GET':
        return render(request, template, {'courseForm':CourseForm()})
        
    # POST
    courseForm = CourseForm(request.POST)
    if not courseForm.is_valid():
        return render(request, template, {'courseForm':courseForm})

    courseForm.save()
    # return course(request)
    messages.success(request, '課程已新增')
    return redirect('course:course')

def courseRead(request, courseId):
    '''
    Read an article
        1. Get the "article" instance using "articleId"; redirect to the 404 page if not found
        2. Render the articleRead template with the article instance and its
           associated comments
    '''
    course = get_object_or_404(Course, id=courseId)
    context = {
        'course': course,
        'lessons': Lesson.objects.filter(course=course)
    }
    return render(request, 'course/courseRead.html', context)


def courseUpdate(request, courseId):
    '''
    Update the article instance:
        1. Get the article to update; redirect to 404 if not found
        2. Render a bound form if the method is GET
        3. If the form is valid, save it to the model, otherwise render a
           bound form with error messages
    '''
    course = get_object_or_404(Course, id=courseId)
    template = 'course/courseUpdate.html'
    if request.method == 'GET':
        courseForm = CourseForm(instance=course)
        return render(request, template, {'courseForm':courseForm})

    # POST
    courseForm = CourseForm(request.POST, instance=course)
    if not courseForm.is_valid():
        return render(request, template, {'courseForm':courseForm})

    courseForm.save()
    messages.success(request, '課程已修改') 
    return redirect('course:courseRead', courseId=courseId)


def courseDelete(request, courseId):
    '''
    Delete the article instance:
        1. Render the article page if the method is GET
        2. Get the article to delete; redirect to 404 if not found
    '''

    if request.method == 'GET':
        return redirect('course:course')

    # POST
    course = get_object_or_404(Course, id=courseId)
    course.delete()
    messages.success(request, '文章已刪除')  
    return redirect('course:course')


def courseSearch(request):
    '''
    Search for articles:
        1. Get the "searchTerm" from the HTML page
        2. Use "searchTerm" for filtering
    '''
    searchTerm = request.GET.get('searchTerm')
    courses = Course.objects.filter(Q(name__icontains=searchTerm) |
                                      Q(desc__icontains=searchTerm))
    context = {'courses':courses, 'searchTerm':searchTerm} 
    return render(request, 'course/courseSearch.html', context)


def courseLike(request, courseId):
    '''
    Add the user to the 'likes' field:
        1. Get the article; redirect to 404 if not found
        2. If the user does not exist in the "likes" field, add him/her
        3. Finally, call articleRead() function to render the article
    '''
    
    course = get_object_or_404(Course, id=courseId)
    print(course.likes.all())
    print(request.user.course_set.all() )
    if request.user not in course.likes.all():
        course.likes.add(request.user)
    return courseRead(request, courseId)


def courseRead_new(request, courseId):
    '''
    Read an article
        1. Get the "article" instance using "articleId"; redirect to the 404 page if not found
        2. Render the articleRead template with the article instance and its
           associated comments
    '''
    course = get_object_or_404(Course, id=courseId)
    context = {
        'course': course,
        'lessons': Lesson.objects.filter(course=course)
    }
    return render(request, 'course/courseRead(new).html', context)