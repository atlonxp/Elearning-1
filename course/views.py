from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.

from course.models import Course,Lesson,Words

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

# class dashboardView(View):
#     '''
#     顯示dashboard
#     '''
#     def get(self,request):
#         # return render(request, 'login.html')
#         courses = {}
#         for course in Course.objects.all():
#             courses.update({course:Lesson.objects.filter(course=course)})

#         # articles = {}
#         # for article in Article.objects.all():
#         #     articles.update({article:Comment.objects.filter(article=article)})

#         context = {'courses':courses}
#         # print(context)
#         return render(request, 'course/sbadmin2.html', context)


def dashboardView(request):
    '''
    顯示dashboard
    '''
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
    # print(course.likes.all())
    # print(request.user.course_set.all() )
    if request.user not in course.likes.all():
        course.likes.add(request.user)
    return courseRead(request, courseId)


def courseRead_new(request,courseId):
    '''
    顯示courseRead_new
    '''
    # course = get_object_or_404(Course, id=courseId)
    # context = {
    #     'course': course,
    #     'lessons': Lesson.objects.filter(course=course)
    # }
    course = get_object_or_404(Course, id=courseId)
    lessons = {}
    for lesson in Lesson.objects.all():
        lessons.update({lesson:Words.objects.filter(lesson=lesson)})

    context = {
        'course':course,
        'lessons':lessons
        }
    # print(context)
    
    return render(request, 'course/courseRead(new).html', context)

def Sentence(request,courseId):
    '''
    顯示courseRead_new
    '''
    # course = get_object_or_404(Course, id=courseId)
    # context = {
    #     'course': course,
    #     'lessons': Lesson.objects.filter(course=course)
    # }


    course = get_object_or_404(Course, id=courseId)
    lessons = {}
    example = []
    for lesson in Lesson.objects.all():
        # print(Words.objects.filter(lesson=lesson))
        a = Words.objects.filter(lesson=lesson)
        for e in a:
            # print(e.example)
            example.append(e.example)
        lessons.update({lesson:Words.objects.filter(lesson=lesson)})
    print(example)
    # ['One of the best known of Aesop\'s fables is "The Lion and the Mouse."', 'The moral of "The Lion and the Mouse" is: Little friends may prove to be great friends.']
    
    

    '''
        判斷詞性部分
    '''
    from textblob import TextBlob

    text = example[0]

    '''
        google翻譯
    '''
    from py_translator import TEXTLIB
    s = TEXTLIB().translator(is_html=False, text= example[0] , lang_to='zh-TW', proxy=False)
    print(s)
    example_tw = s


    blob = TextBlob(text)
    # print(blob.tags)           # [('The', 'DT'), ('titular', 'JJ'),
                        #  ('threat', 'NN'), ('of', 'IN'), ...]
    words_tag_2_tw={

        'CC':'並列連詞',
        'CD':'純數,基數',
        'DT':'限定詞(置於名詞前起限定作用,如 the、some、my 等)',
        'EX':'存在句,存現句',
        'FW':'外來語',
        'IN':'介詞/從屬連詞,主從連詞,從屬連接詞',
        'JJ':'形容詞',
        'JJR':'（形容詞或副詞的）比較級形式',
        'JJS':'（形容詞或副詞的）最高級',
        'LS':'listmarker',
        'MD':'形態的，形式的 , 語氣的；情態的',
        'NN':'名詞單數形式',
        'NNS':'名詞複數形式',
        'NNP':'專有名詞',
        'NNPS':'專有名詞複數形式',
        'PDT':"前位限定詞",
        'POS':'屬有詞,結束語',
        'PRP':'人稱代詞',
        'PRP$':'物主代詞',
        'RB':'副詞',
        'RBR':'（形容詞或副詞的）比較級形式',
        'RBS':'（形容詞或副詞的）最高級',
        'RP':'小品詞(與動詞構成短語動詞的副詞或介詞)',
        'TO':'to',
        'UH':'感嘆詞；感嘆語',
        'VB':'動詞',
        'VBD':'動詞,過去時,過去式',
        'VBG':'動詞 ,動名詞/現在分詞',
        'VBN':'動詞,過去分詞',
        'VBP':'動詞,現在',
        'VBZ':'動詞,第三人稱',
        'WDT':'限定詞（置於名詞前起限定作用，如 the、some、my 等）',
        'WP':'代詞（代替名詞或名詞詞組的單詞）',
        'WP$':'所有格；屬有詞',
        'WRB':'副詞'
    }

    # all_tag='''
    #     <option value="名詞">名詞</option>
    #     <option value="CC">並列連詞</option>
    #     <option value="CD">純數,基數</option>
    #     <option value="DT">限定詞(置於名詞前起限定作用)</option>
    #     <option value="EX">存在句,存現句</option>
    #     <option value="FW">外來語</option>
    #     <option value="IN">介詞/從屬連詞,主從連詞,從屬連接詞</option>
    #     <option value="JJ">形容詞</option>
    #     <option value="JJR">（形容詞或副詞的）比較級形式</option>
    #     <option value="JJS">（形容詞或副詞的）最高級</option>
    #     <option value="LS">listmarker</option>
    #     <option value="MD">形態的，形式的,語氣的；情態的</option>
    #     <option value="NN">名詞單數形式</option>
    #     <option value="NNS">名詞複數形式</option>
    #     <option value="NNP">專有名詞</option>
    #     <option value="NNPS">專有名詞複數形式</option>
    #     <option value="PDT">前位限定詞</option>
    #     <option value="POS">屬有詞,結束語</option>
    #     <option value="PRP">人稱代詞</option>
    #     <option value="PRP$">物主代詞</option>
    #     <option value="RB">副詞</option>
    #     <option value="RBR">（形容詞或副詞的）比較級形式</option>
    #     <option value="RBS">（形容詞或副詞的）最高級</option>
    #     <option value="RP">小品詞(與動詞構成短語動詞的副詞或介詞)</option>
    #     <option value="TO">to</option>
    #     <option value="UH">感嘆詞；感嘆語</option>
    #     <option value="VB">動詞</option>
    #     <option value="VBD">動詞,過去時,過去式</option>
    #     <option value="VBG">動詞 ,動名詞/現在分詞</option>
    #     <option value="VBN">動詞,過去分詞</option>
    #     <option value="VBP">動詞,現在</option>
    #     <option value="VBZ">動詞,第三人稱</option>
    #     <option value="WDT">限定詞（置於名詞前起限定作用，如 the、some、my 等）</option>
    #     <option value="WP">代詞（代替名詞或名詞詞組的單詞）</option>
    #     <option value="WP$">所有格；屬有詞</option>
    #     <option value="WRB">副詞'</option>
    # '''


# CC     coordinating conjunction 並列連詞
# CD     cardinaldigit  純數  基數
# DT     determiner  限定詞（置於名詞前起限定作用，如 the、some、my 等）
# EX     existentialthere (like:"there is"... think of it like "thereexists")   存在句；存現句
# FW     foreignword  外來語；外來詞；外文原詞
# IN     preposition/subordinating conjunction介詞/從屬連詞；主從連詞；從屬連接詞
# JJ     adjective    'big'  形容詞
# JJR    adjective, comparative 'bigger' （形容詞或副詞的）比較級形式
# JJS    adjective, superlative 'biggest'  （形容詞或副詞的）最高級
# LS     listmarker  1)
# MD     modal (could, will) 形態的，形式的 , 語氣的；情態的
# NN     noun, singular 'desk' 名詞單數形式
# NNS    nounplural  'desks'  名詞複數形式
# NNP    propernoun, singular     'Harrison' 專有名詞
# NNPS  proper noun, plural 'Americans'  專有名詞複數形式
# PDT    predeterminer      'all the kids'  前位限定詞
# POS    possessiveending  parent's   屬有詞  結束語
# PRP    personalpronoun   I, he, she  人稱代詞
# PRP$  possessive pronoun my, his, hers  物主代詞
# RB     adverb very, silently, 副詞    非常  靜靜地
# RBR    adverb,comparative better   （形容詞或副詞的）比較級形式
# RBS    adverb,superlative best    （形容詞或副詞的）最高級
# RP     particle     give up 小品詞(與動詞構成短語動詞的副詞或介詞)
# TO     to    go 'to' the store.
# UH     interjection errrrrrrrm  感嘆詞；感嘆語
# VB     verb, baseform    take   動詞
# VBD    verb, pasttense   took   動詞   過去時；過去式
# VBG    verb,gerund/present participle taking 動詞  動名詞/現在分詞
# VBN    verb, pastparticiple     taken 動詞  過去分詞
# VBP    verb,sing. present, non-3d     take 動詞  現在
# VBZ    verb, 3rdperson sing. present  takes   動詞  第三人稱
# WDT    wh-determiner      which 限定詞（置於名詞前起限定作用，如 the、some、my 等）
# WP     wh-pronoun   who, what 代詞（代替名詞或名詞詞組的單詞）
# WP$    possessivewh-pronoun     whose  所有格；屬有詞
# WRB    wh-abverb    where, when 副詞




    sentence = ''
    
    # for word,tag in  blob.tags:
    #     sentence += '''
    #     <form>
    #         <div class="form-row align-items-center">
    #         <div class="col-auto my-1">
    #             <label class="mr-sm-2" for="inlineFormCustomSelect">
    #     '''
    #     sentence += word

    #     sentence += '''
    #             </label>
    #             <select class="custom-select mr-sm-2" id="inlineFormCustomSelect">
    #     '''
    #     sentence += '<option selected value="'+tag+'" >'+tag+'</option>'

    #     sentence += '''
    #             <option value="名詞">名詞</option>
    #             <option value="動詞">動詞</option>
    #             </select>
    #         </div>
            
    #         <div class="col-auto my-1">
    #             <button type="submit" class="btn btn-primary">Submit</button>
    #         </div>
    #         </div>
    #     </form>
    #     '''
        # print(word,tag)

    # sentence += '''
    #     <form>
    #         <div class="row">    
    # '''
  
    # for word,tag in  blob.tags:   
    #     sentence += '''
    #             <div class="form-row align-items-center">
    #                 <div class="col-2"> 
    #     '''
    #     sentence += '<label class="mr-sm-2" for="inlineFormCustomSelect">'+word+'</label>'
    #     sentence += '''
    #             <select id="select_words" name="town" style="font-size:6px;">
    #     '''
    #     sentence += '<option value="'+tag+'">'+words_tag_2_tw[tag]+'</option>'
    #     sentence += all_tag
    #     sentence += '''
    #             </select>
    #             </div>
    #         </div>
    #     '''
    # sentence += '''    
    #         </div>
    #     </form>
    # '''
    
    # '''html
    # <form>
    #     <div class="form-row align-items-center">
    #         <div class="col-4">
    #             <label class="mr-sm-2" for="inlineFormCustomSelect">words</label>
    #             <select id="select_words" name="town" style="font-size:12px;">
    #                 <option value="名詞">名詞</option>
    #                 <option value="動詞">動詞</option>
    #             </select>
    #         </div>
    #     </div>
    # </form>
    # '''

    sentence += '''
        <div class="row"> 
    '''
  
    for word,tag in  blob.tags:
        if word == "'s":
            sentence += '<em data-toggle="tooltip" data-html="true" title="'+words_tag_2_tw[tag]+'">'+word+'</em>'
        else:
            sentence += '<em data-toggle="tooltip" data-html="true" title="'+words_tag_2_tw[tag]+'">&nbsp;'+word+'</em>'

    sentence += '''   
        </div>
        <div class="row"> 
            <em>'''+example_tw+'''</em>
        </div>
    '''
    
    # '''html
    # <div class="row">
    #     <label class="mr-sm-2" for="inlineFormCustomSelect" data-toggle="tooltip" data-html="true" title="12312313">words</label>
    #     <label class="mr-sm-2" for="inlineFormCustomSelect" data-toggle="tooltip" data-html="true" title="12312313">words</label>
    #     <label class="mr-sm-2" for="inlineFormCustomSelect" data-toggle="tooltip" data-html="true" title="12312313">words</label>
    #     <label class="mr-sm-2" for="inlineFormCustomSelect" data-toggle="tooltip" data-html="true" title="12312313">words</label>
    # </div>
    # '''






    # sentence += '''
    #     <form>
    #         <div class="form-row align-items-center">
    #             <div class="col-4">
    #                 <label class="mr-sm-2" for="inlineFormCustomSelect">123</label>
    #                 <select class="custom-select mr-sm-0" id="inlineFormCustomSelect" style="font-size:7px;">
    #                     <option selected value="名詞" style="font-size:7px;">Choose...</option>
    #                     <option value="名詞" style="font-size:7px;">名詞</option>
    #                     <option value="動詞" style="font-size:7px;">動詞</option>
    #                 </select>

    #                 <select id="select_words" name="town" style="font-size:12px;">
    #                     <option value="名詞">名詞</option>
    #                     <option value="動詞">動詞</option>
    #                 </select>
    #             </div>
            
     
    #         </div>
    #     </form>
    # '''


    context = {
        'course':course,
        'lessons':lessons,
        'Sentence':sentence
        }
    # print(context)
    
    return render(request, 'course/Sentence.html', context)
