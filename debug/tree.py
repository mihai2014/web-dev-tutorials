import os, json

ALL = True
#ALL: list of directories and files 
#not ALL: list only directories
#ul not included in li
def traverse0(dir):
    print('<ul>')
    for item in os.listdir(dir):
        if ALL : print('<li>%s</li>' % item)
        fullpath = os.path.join(dir, item)
        if os.path.isdir(fullpath):
            if not ALL : print('<li>%s</li>' % item)
            if os.listdir(fullpath) != []:
                traverse(fullpath)
    print('</ul>')

#traverse0('.')

html = ''
def traverse(dir):
    global html
    html += '<ul>'
    for item in os.listdir(dir):
        if ALL : html += f'<li>{item}</li>'
        fullpath = os.path.join(dir, item)
        if os.path.isdir(fullpath):
            if not ALL : html += '<li>{item}</li>'
            if os.listdir(fullpath) != []:
                traverse(fullpath)
    html += '</ul>'

# traverse('.')
# print(html)


# stream = os.popen('tree -J .')
# output = stream.read()
# dict = json.loads(output)
# print(dict)

class Documents:
    def __init__(self, path):
        self.path = path
        self.tree = {}
        self.html = ''
        self.readTree()
        self.scanTree(self.tree)

    def readTree(self):
        stream = os.popen('tree -J ' + self.path)
        output = stream.read()
        self.tree = json.loads(output)[0]

    def scanTree(self,item):    
        # folders
        if ('contents' in item):
            print(f"D {item['name']}")
            for subitem in item['contents']:
                self.scanTree(subitem)
        # files        
        else:    
            print(f"F {item['name']}")    

    def htmlTree(self):
        # folders
        if ('contents' in item):
            self.html += '<ul>'

            self.html += '<li>'
            self.html += item.name
            self.html += '</li>'

            for subitem in item['contents']:
                self.htmlTree(subitem)
            self.html += '</ul>'    

        # files        
        else:    
            self.html += '<li>'
            self.html += item.name
            self.html += '</li>'
            

    def htmlTopics(self):
        # folders
        if ('contents' in item):
            pass
            for subitem in item['contents']:
                self.htmlTopics(subitem)
        # files        
        else:    
            pass

    def getTree(self):
        self.html = ''
        self.htmlTree()

    def getTopics(self):
        self.html = ''
        self.htmlTopics()

docs = Documents('.')
# print(docs.tree)     

