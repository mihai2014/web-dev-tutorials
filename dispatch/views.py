from django.shortcuts import render
from django.contrib.staticfiles.views import serve
from django.template import Template, Context
from django.conf import settings
from django.templatetags.static import static
from django.http import HttpResponse
from django.utils.html import escape
from dispatch.tree import Documents
import json
import os

fileImg = static('/dispatch/img/file.jpg')
folderImg = static('/dispatch/img/folder.png')
# folderCode = static('/code/')
# folderCode  = "static"
# str(settings.BASE_DIR)
docs = Documents(str(settings.BASE_DIR) + '/code/',folderImg, fileImg)
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
    <h1>Vue Topics</h1>
    '''
    html += docs.html

    return render(request, 'dispatch/common.html', {"data":html, "name": "Topics"})

def fileExtension(name):
    return name.split(".")[1]

def itemTopic(request, file_path):
    baseDir = str(settings.BASE_DIR)
    compose = (baseDir, '/code/', file_path)
    dirPath = "".join(compose)

    html = '''
    <i>Folder: ''' + dirPath + '''</i>
    <br><br>
    '''

    files = os.listdir(dirPath)
    #print(files)

    for file in files:
        filePath =  "/".join((dirPath,file))  
        if not os.path.isdir(filePath):
            # intercept topic.json
            if file == "topic.json":
                with open(filePath) as f:
                    content = f.read()
                    # print(content)
                    content = json.loads(content)
                    title = content['title'] 
                    tags = content['tags'] 
                    files = content['files']
                tagsStr = ", ".join(tags)
                print(tagsStr)

            # intercept introduction.html
            if file == "introduction.html":                    
                with open(filePath) as f:
                    content = f.read()
                    html += content                    
                           


    for file in files:
        filePath =  "/".join((dirPath,file))  
        if not os.path.isdir(filePath):
            # bypass
            if file == "topic.json" or file == "introduction.html":
                continue

            # print(file,filePath)
            if fileExtension(file) == "js": language = "language-javascript"
            if fileExtension(file) == "html": language = "language-html"
            if fileExtension(file) == "json": language = "language-json"
            if fileExtension(file) == "py": language = "language-python"
            
            with open(filePath) as f:

                html += "<p>"+file+"</p>"

                html += '<pre><code class="'+language+'" >'

                content = f.read()
                html += escape(content)

                html += '</code></pre>'
                
                # print(content)
                # print("------------------------------------")
                html += "<br>"


    return render(request, 'dispatch/common.html', {"data":html , "tags": tags, "category":"", "tagsStr": tagsStr, "name": "Topics", "title": title})


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
