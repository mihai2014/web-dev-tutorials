import os
import json

ALL = True
# ALL: list of directories and files
# not ALL: list only directories
# ul not included in li


def traverse0(dir):
    print('<ul>')
    for item in os.listdir(dir):
        if ALL:
            print('<li>%s</li>' % item)
        fullpath = os.path.join(dir, item)
        if os.path.isdir(fullpath):
            if not ALL:
                print('<li>%s</li>' % item)
            if os.listdir(fullpath) != []:
                traverse(fullpath)
    print('</ul>')

# traverse0('.')


html = ''


def traverse(dir):
    global html
    html += '<ul>'
    for item in os.listdir(dir):
        if ALL:
            html += f'<li>{item}</li>'
        fullpath = os.path.join(dir, item)
        if os.path.isdir(fullpath):
            if not ALL:
                html += '<li>{item}</li>'
            if os.listdir(fullpath) != []:
                traverse(fullpath)
    html += '</ul>'

# traverse('.')
# print(html)


class JsonTree:
    def __init__(self, path):
        self.treeObj = {"name":path, "contents":[]}
        self.path = path
        self.nr = -1
        self.scan(self.path, self.treeObj)

    def add(self, itemObj, name, contents):
        #itemObj['type'] = type
        itemObj['name'] = name
        itemObj['contents'] = contents
        return itemObj['contents']

    def scan(self, dir, itemObj):
        #self.nr += 1
        #if(self.nr == 4):
        #    sys.exit(0)

        for item in sorted(os.listdir(dir)):

            fullpath = os.path.join(dir, item)

            name = item
            if(os.path.isdir(fullpath)):
                typeItem = "directory"
                newitemObj = {"type":typeItem, "name": name , "contents": []}
            else:
                typeItem = "file"
                newitemObj = {"type":typeItem, "name": name}

            itemObj['contents'].append(newitemObj)

            #print(self.nr, typeItem, name)

            if os.path.isdir(fullpath):
                if os.listdir(fullpath) != []:
                    self.scan(fullpath, newitemObj)

#j = JsonTree('code')
#print(j.treeObj)

# stream = os.popen('tree -J .')
# output = stream.read()
# dict = json.loads(output)
# print(dict)

class Documents:
    def __init__(self, path, folderImg, fileImg):
        self.path = path
        self.tree = {}
        self.html = ''
        self.folderImg = folderImg
        self.fileImg = fileImg
        self.dirSections = []
        self.readTree()
        self.flag = False
        self.includedInTopic = False
        self.onlyTopics = True
        # self.scanTree(self.tree)

    def readTree(self):
        j = JsonTree(self.path)
        self.tree = j.treeObj
        
        #stream = os.popen('tree -J ' + self.path)
        #output = stream.read()
        #self.tree = json.loads(output)[0]

    # prototype
    def scanTree(self, item):
        # folders
        if ('contents' in item):
            print(f"D {item['name']}")
            for subitem in item['contents']:
                self.scanTree(subitem)
        # files
        else:
            print(f"F {item['name']}")

 

    def category(self, item):
        if 'contents' in item:
            for subitem in item['contents']:
                if((subitem['type'] == 'file') and (subitem['name'] == 'category.json')):
                    return True
        else:
            return False

    def topic(self, item):
        if 'contents' in item:
            for subitem in item['contents']:
                if((subitem['type'] == 'file') and (subitem['name'] == 'topic.json')):
                    return True
        else:
            return False

    def addFolder(self, item):

        dirClass = ''
        imgClass = ''
        href = "#"
        if(self.category(item)):
            #print("category"," ", end='')
            dirClass = 'text-green-600 underline'
        elif(self.topic(item)):
            #print("topic"," ", end='')
            dirClass = 'text-blue-500 hover:text-red-500 cursor-pointer'            
            href = "/".join(self.dirSections)
        elif(self.includedInTopic):
            #print("in-topic"," ", end='')
            if(self.onlyTopics):
                dirClass = 'invisible'    
                imgClass = 'invisible'
        else:
            #print("sub-category", " ", end='')
            pass

        # print("/".join(self.dirSections))    

        self.html += f'<img src="{self.folderImg}" alt="D-img" width="15" height="15" class="folder {imgClass}" >'
        self.html += f'<li class="{dirClass}">'
        # self.html += item['name']
        self.html += f'<a href={href}>{item["name"]}</a>'
        self.html += '</li>'        


    def addFile(self, item):
        
        self.html += f'<img src="{self.fileImg}" alt="F-img" width="15" height="15" class="file ">'
        self.html += f'<li>'
        self.html += item['name']
        self.html += '</li>'        
    
    # recursive
    def scanTree(self, item):
        # folders
        if ('contents' in item):

            # add new "dir section" (without 1st iteration that gives the entire root path)
            if (self.flag == False):
                self.flag = True
                self.dirSections.append('item')
            else:
                self.dirSections.append(item['name'])

            if(self.topic(item)): self.includedInTopic = True

            self.html += '<ul class="pl-4">'

            self.addFolder(item)

            for subitem in item['contents']:
                self.scanTree(subitem)

            self.dirSections.pop()    
            self.includedInTopic = False
            self.html += '</ul>'    

        # files
        else:
            if(not self.onlyTopics):
                self.addFile(item)

    def getTopics(self):
        self.html = ''
        self.scanTree(self.tree)
        # print(self.tree)

    def getTree(self):
        self.onlyTopics = False
        self.html = ''
        self.scanTree(self.tree)

# docs = Documents('.')
# print(docs.tree)
