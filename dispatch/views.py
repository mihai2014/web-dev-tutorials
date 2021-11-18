from django.shortcuts import render
from django.contrib.staticfiles.views import serve
from django.template import Template, Context
from django.conf import settings
from django.templatetags.static import static
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.html import escape
from dispatch.tree import Documents
import json
import os
from django.urls import reverse

fileImg = static('/dispatch/img/file.jpg')
folderImg = static('/dispatch/img/folder.png')
# folderCode = static('/code/')
# folderCode  = "static"
# str(settings.BASE_DIR)
docs = Documents(str(settings.BASE_DIR) + '/../code/',folderImg, fileImg)
docs.getTopics()
print("tree loaded")

def favicon(request):
    # print('favicon')
    # return HttpResponse("<h1>favicon!</h1>")
    return serve(request, 'dispatch/favicon.ico')

#def index(request):
#    # print('>>', request.GET)
#    # return HttpResponse("<h1>Hello!</h1>")
#    data = '''
#    <h1>Home</h1>    
#    '''    
#    return render(request, 'dispatch/common.html', {"data": data, "name": "Home"})

def test(request):

    baseDir = str(settings.BASE_DIR)
    
    #compose = (baseDir, '/../code/', file_path)
    compose = (baseDir, '/dispatch/templates/dispatch/test-tabs.html')
    filePath = "".join(compose)

    with open(filePath) as f:
        content = f.read()
    #print(content)    

    #return HttpResponse(baseDir)
    return render(request, 'dispatch/common.html', {"data": content,  "name": "Test"})

def home(request):
    data = '''
    <h1>Home</h1>    
    '''
    return render(request, 'dispatch/common.html', {"data": "", "name": "Home"})


def about(request):
    data = "About"
    return render(request, 'dispatch/common.html', {"data": "", "name": "About" })
    #return render(request, 'dispatch/about.html', {"data": data, "name": "About" })


def topics(request):
    global docs

    html = '''
    <h1 class="font-bold">Topics</h1>
    <br>
    '''
    html += docs.html

    return render(request, 'dispatch/common.html', {"data":html, "name": "Topics"})

itemTopicHtml = ""

# tab buttons
def tabs(filesList):

    firstTime = True

    selected = '''text-gray-600 py-4 px-10 block hover:text-blue-500
    focus:outline-none text-blue-500 border-b-2 font-medium border-blue-500    
    '''
    notSelected = '''text-gray-600 py-4 px-10 block hover:text-blue-500
    focus:outline-none'''

    htmlTabs = '<div class="bg-white overflow-auto"><div class="flex flex-col sm:flex-row">'

    for fileName in filesList:
        if firstTime: 
            cls = selected 
            active = "true"
            firstTime = False
        else: 
            cls = notSelected
            active = "false"

        htmlTabs += f'<button id="button-{fileName}" active="{active}" class="{cls}">{fileName}</button>'
    
    htmlTabs += '</div></div>'  

    # htmlTabs += jsScript

    return htmlTabs

# html string with all topic files
def showFile(fileName, filePath, fileContent):
    global itemTopicHtml

    # initial, all tabs are invisible, will be made wisible by js from the tabs menu (see tabs.js)
    # for debug situations make class="visible" just below
    itemTopicHtml += f'<div class="invisible" id="file-{fileName}">'

    itemTopicHtml += f'<div>{fileName}</div>'

    #itemTopicHtml += f'<p><a href="{filePath}">{filePath}</a></p><br>'
    itemTopicHtml += fileContent

    itemTopicHtml += f'</div>'


def fileExtension(name):
    return name.split(".")[1]

def itemCategory(request, href):

    # index.html path
    baseDir = str(settings.BASE_DIR)
    compose = (baseDir, '/../code/', href)
    indexFilePath = "".join(compose)

    # category.json path (by removing ending "index.html" from the path)
    parts = indexFilePath.split("/")
    parts.pop()
    jsonFilePath = "/".join(parts)+"/category.json"

    try:
        with open(jsonFilePath) as f:
            content = f.read()
            content = json.loads(content)
            try: 
                title = content['name'] 
            except: 
                title = "Dj/Vue-tutorial" 
            try: 
                tags = content['tags'] 
            except: 
                tags = ["Django","Vue","tutorial"]
            tagsStr = ", ".join(tags)
    except:
        print("no topic.json!") 

    try:
        with open(indexFilePath) as f:
            content = f.read()
    except:
        print("no file")
        #return HttpResponseRedirect(reverse('topics'))
        #return HttpResponse("Category: "+ href)
        content = "Dj/Vue-tutorial"

    return render(request, 'dispatch/common.html', 
                    {"data":content , 
                    "tags": tags, 
                    "category":"", 
                    "tagsStr": tagsStr, 
                    "name": "Category", 
                    "title": title, 
                    "tabs": []})    

def itemTopic(request, file_path):
    global itemTopicHtml

    # reset
    itemTopicHtml = ""

    baseDir = str(settings.BASE_DIR)
    compose = (baseDir, '/../code/', file_path)
    dirPath = "".join(compose)

    tabFiles = []

    # try:
    files = os.listdir(dirPath)
    # except:
    # return render(request, 'dispatch/common.html', 
    #                 {"data":itemTopicHtml , 
    #                 "tags": tags, 
    #                 "category":"", 
    #                 "tagsStr": tagsStr, 
    #                 "name": "Topics", 
    #                 "title": title, 
    #                 "tabs": htmlTabs})

    topicFiles = []

    try:
        file = "introduction.html"
        filePath =  "/".join((dirPath,file))
        with open(filePath) as f:
            content = f.read()
            topicFiles += [file]
            showFile(file, filePath, f"{content}")
    except:
        pass        

    try:
        filePath =  "/".join((dirPath,"topic.json"))
        with open(filePath) as f:
            content = f.read()
            content = json.loads(content)
            title = content['title'] 
            tags = content['tags'] 
            topicFiles += content['files']
            htmlTabs = tabs(topicFiles)
            tagsStr = ", ".join(tags)
    except:
        print("no topic.json!")    

    for file in topicFiles:
        filePath =  "/".join((dirPath,file))  
        if not os.path.isdir(filePath):
            # bypass
            if file == "topic.json" or file == "introduction.html":
                continue

            if fileExtension(file) == "js": language = "language-javascript"
            if fileExtension(file) == "html": language = "language-html"
            if fileExtension(file) == "json": language = "language-json"
            if fileExtension(file) == "py": language = "language-python"
            
            with open(filePath) as f:
                content = f.read()
                showFile(file, filePath, f'<pre><code class="{language}">{escape(content)}</code></pre>')

    return render(request, 'dispatch/common.html', 
                    {"data":itemTopicHtml , 
                    "tags": tags, 
                    "category":"", 
                    "tagsStr": tagsStr, 
                    "name": "Topics", 
                    "title": title, 
                    "tabs": htmlTabs})    


# def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('polls/index.html')
#    context = {
#        'latest_question_list': latest_question_list,
#    }
#    return HttpResponse(template.render(context, request))



#    html = "<h1>Topics - this is html unescaped!!</h1>"
#    html += docs.html

#    # c = Context(dict(data = html))
#    c = Context({"data": html})
#    t = Template('''
#    {% extends "dispatch/base.html" %}
#    {% block content %}
#    {% autoescape off %}{{ data }}{% endautoescape %}
#    {% endblock %}
#    ''').render(c)
#    # print(t)
#    #return HttpResponse(t)
