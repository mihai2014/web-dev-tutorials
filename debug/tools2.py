from django.http import HttpResponse, Http404
import os

import numpy as np
from matplotlib import pyplot as plt


from time import sleep
import json


class regr_line:
    def __init__(self,data):
        self.data = data
        self.line1()
        self.graph()

    def line1(self):
        #transpose data
        x, y = self.data.T

        #population
        DDOF = 0

        #mean
        x_m = np.mean(x)
        y_m = np.mean(y)

        #std. dev. 
        s_x = np.std(x,ddof=DDOF)
        s_y = np.std(y,ddof=DDOF)

        #(2) (2')
        r = np.corrcoef(x,y)[0,1]
        #print("r =",r)

        #slope of regression line (3)
        m = r * s_y/s_x
        #print("m =",m)

        #y intercept
        b = y_m - m*x_m
        #print("y = % sx + %s" % (m,b))

        self.x = x
        self.y = y
        self.m = m
        self.b = b

    def line2(self):
        #transpose data
        x, y = self.data.T

        xy = np.multiply(x,y)
        xx = np.multiply(x,x)

        x_m = np.mean(x)
        y_m = np.mean(y)
        xy_m = np.mean(xy)
        xx_m = np.mean(xx)

        m = (xy_m - x_m * y_m )/(xx_m - x_m * x_m)
        b = y_m - m * x_m

        self.x = x
        self.y = y
        self.m = m
        self.b = b

#    def line2(self):
#        n = len(data)

        #sum of product of z-scores for (2) (2')
        #s = 0
        #for i,j in data:
        #    z_x = (i - x_m)/s_x
        #    z_y = (j - y_m)/s_y
        #    s = s + z_x*z_y

        #(1) (1')
        #r = (1/(n-DDOF)) * s   
        #print("r =",r)

        #xy_values = []
        #x_sq_values = []
        #for i,j in data:
        #    xy_values.append(i*j)
        #    x_sq_values.append(i*i)

        #xy_m = np.mean(xy_values)
        #x_sq_m = np.mean(x_sq_values)

        #slope (4)
        #m = (xy_m - x_m*y_m)/(x_sq_m - x_m*x_m)
        #print("m =",m)



    def graph(self):

        ret = plt.scatter(self.x,self.y)

        x_max = np.max(self.x)

        # Two points (x1, y1), (x2, y2) that define line y = mx + b
        (x1, y1), (x2, y2) = (0, self.b), (x_max, x_max*self.m + self.b)
        plt.plot([x1, x2], [y1, y2], 'r-')

        #plt.xlim(right=10)  # adjust the right leaving left unchanged
        #plt.xlim(left=0)  # adjust the left leaving right unchanged.
        #plt.ylim(top=50)
        #plt.ylim(0, 40)     # set the ylim to bottom, top

        #plt.show()

        PWD = os.getcwd()
        plt.savefig(PWD + "/blog/line.png")
        plt.close()


def regression(data):
    PWD = os.getcwd()
    #print(PWD)

    name = "x"
    v = []
    strValues = data.split(",")
    for strN in strValues:
        n = float(strN)

        if name=="x":
            x = n
            name="y"

        elif name=="y":
            y = n
            v.append([x,y])
            name="x"

    #data points
    values = np.array(v)

    #computeLine(values)
    my_line = regr_line(values)
    #print(id(my_line))

    image_data = open(PWD + "/blog/line.png", "rb").read()     #.decode('utf-8')
    return HttpResponse(image_data, content_type="image/png")
    #return HttpResponse(data)


def select(request, name, data):
    try:
        #return locals()[name]()
        return globals()[name](data)
    except KeyError:
        raise Http404("Resource does not exist(1)")



#----------------------------------------------------------------------------


def reply(request):
    req = request.read()
    if('timeout' in request.GET):
        timeout = int(request.GET['timeout'])
        sleep(timeout)
        return HttpResponse("here I am!")
    if('json' in request.POST):
        name = request.POST['name']
        #string
        jsonStr = request.POST['json']
        #dictionary
        jsonDict = json.loads(jsonStr)
        return HttpResponse("Your request was: " + req.decode('utf-8'))
    if request.FILES:
        comment = request.POST['comment']
        file = request.FILES['fileToUpload']
        #print file.size
        msg = "Your request was: comment=" + comment + "  file=" + file.name  #+ " file size=" + file.size
        return HttpResponse(msg)
    #catch all situations, just in case
    return HttpResponse("hello!")


def reply2(request):
    #req = request.read()
    #print req

    data = {}
    data['key1'] = "a"
    data['key2'] = 10
    data = json.dumps(data)
    return HttpResponse(data)


def test(request):

    if('arg' in request.GET):
        arg = request.GET['arg']
        if(arg == "1"):
            return HttpResponse("response nr 1")
        if(arg == "2"):
            return HttpResponse("response nr 2")

    return HttpResponse("hello!")


def answer_me(request):
    method = request.method

    if(method == "GET"):
        question = request.GET['question']
        return HttpResponse("Your question was: '" + question+"'")

    if(method == "POST"):
        pass
        question = request.POST['question']
        return HttpResponse("Your question was: '" + question+"'")

    return HttpResponse("hello!")


def select2(request):
    app = request.path.split("/")[2]
    try:
        #return locals()[name]()
        return globals()[app](request)
    except KeyError:
        raise Http404("Resource does not exist(2)")


ALL = False
#ALL: list of directories and files 
#not ALL: list only directories
#ul not included in li
def traverse(dir):
    print('<ul>')
    for item in os.listdir(dir):
        if ALL : print('<li>%s</li>' % item)
        fullpath = os.path.join(dir, item)
        if os.path.isdir(fullpath):
            if not ALL : print('<li>%s</li>' % item)
            if os.listdir(fullpath) != []:
                traverse(fullpath)
    print('</ul>')

