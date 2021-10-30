import os
import json
import sys


def scanTree(self, item):

    # folders
    if ('contents' in item):
        self.html += '<ul>'
        self.addFolder(item)

        for subitem in item['contents']:
            self.scanTree(subitem)

        self.html += '</ul>'

    # files
    else:
        if(not self.onlyTopics):
            self.addFile(item)


class JsonTree:
    def __init__(self, path):
        self.treeObj = {"name":path, "contents":[]}
        self.path = path
        self.nr = -1
        self.scan(self.path, self.treeObj)
        self.start()

    def add(self, itemObj, name, contents):
        #itemObj['type'] = type
        itemObj['name'] = name
        itemObj['contents'] = contents
        return itemObj['contents']

    def scan(self, dir, itemObj):
        #self.nr += 1
        #if(self.nr == 4):
        #    sys.exit(0)

        for item in os.listdir(dir):

            fullpath = os.path.join(dir, item)

            name = item
            if(os.path.isdir(fullpath)):
                typeItem = "directory"
                newitemObj = {"type":typeItem, "name": name , "contents": []}
            else:
                typeItem = "file"
                newitemObj = {"type":typeItem, "name": name}

            itemObj['contents'].append(newitemObj)

            print(self.nr, type, name)

            if os.path.isdir(fullpath):
                if os.listdir(fullpath) != []:
                    self.scan(fullpath, newitemObj)


j = JsonTree('code')
print(j.treeObj)
