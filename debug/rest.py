   # def isMainFolder(self, item):
    #     # this is file
    #     if 'contents' not in item:
    #         return False
    #     # this is folder    
    #     for subitem in item['contents']:
    #         if((subitem['type'] == 'file') and (subitem['name'] == 'class.json')):
    #             return True
    #     return False

    # def isTopicFolder(self, item):
    #     # this is file
    #     if 'contents' not in item:
    #         return False
    #     # this is folder    
    #     for subitem in item['contents']:
    #         #print((subitem['type'] == 'file', subitem['name'] == 'class.json'))
    #         if((subitem['type'] == 'file') and (subitem['name'] == 'topic.json')):
    #             return True
    #     return False

    # def dirClass(self, item):
    #     dirClass = 'text-blue-500 '
    #     if (self.isMainFolder(item)):
    #         dirClass += 'hover:text-red-500 cursor-pointer'
    #     elif (self.isTopicFolder(item)):
    #         dirClass += 'text-indigo-600'
    #     else:
    #         # do NOT show folders that are not main or topics (eq. assets, img ...)
    #         # modify for showing the == entire tree ==
    #         # dirClass = 'invisible'
    #         pass
    #     return dirClass

    # def visible(self, item):
    #     imgClass = ' '
    #     if (self.isMainFolder(item)):
    #         imgClass = ' '
    #     elif (self.isTopicFolder(item)):
    #         # do NOT show images and files
    #         # imgClass = 'invisible'
    #         pass
    #     else:
    #         # do NOT show images and files
    #         # imgClass = 'invisible'
    #         pass
    #     return imgClass

    # def htmlTree2(self, item):
    #     # print(item['name'], self.dirSections)
    #     # folders
    #     if ('contents' in item):
    #         # add new "dir section" (without 1st iteration that gives the entire root path)
    #         if (self.flag == False):
    #             self.flag = True
    #             self.dirSections.append('item')
    #         else:
    #             self.dirSections.append(item['name'])

    #         self.html += '<ul class="pl-4">'

    #         self.html += f'<img src="{self.folderImg}" alt="folderImg" width="15" height="15" class="folder {self.visible(item)}" >'
    #         self.html += '<li style="clear:all">'

    #         if (self.isMainFolder(item)):
    #             self.html += f'<a class="{self.dirClass(item)}" href="{"/".join(self.dirSections)}">{item["name"]}</a>'
    #         else:
    #             self.html += f'<a class="{self.dirClass(item)}" href="#">{item["name"]}</a>'
    #             pass

    #         self.html += '</li>'

    #         for subitem in item['contents']:
    #             self.htmlTree(subitem)

    #         self.html += '</ul>'
    #         # remove last "dir section"
    #         self.dirSections.pop()

    #     # files
    #     else:
    #         pass
    #         # no files - do NOT delete
    #         self.html += f'<img src="{self.fileImg}" alt="folderImg" width="15" height="15" class="file {self.visible(item)}">'
    #         self.html += f'<li style="clear:all" class="{self.visible(item)}">'
    #         self.html += item['name']
    #         self.html += '</li>'

    # #def htmlTree(self, item, itemType):
    # #    self.html += "begin modif"
    # #    print(itemType ,item['name'])