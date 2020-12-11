'''
from tkinter import *

class App:
    def __init__(self):
        window = Tk()
        helloA = Button(window, text="클릭하세요",command=self.hello)
        helloA.pack()
        
        window.mainloop()
    
    def hello(self):
        print("안녕하세요")
        print("안녕하세요")
        print("안녕하세요")

App()
'''
'''
from tkinter import *

def cos1():
    temperature = float(e1.get())
    mytemp=(temperature-32)*5/9
    e2.insert(0,str(mytemp))

def fos1():
    temperature = float(e1.get())
    mytemp=(temperature-32)*5/9
    e2.insert(0,str(mytemp))
window = Tk()
Label(window, text="화씨").grid(row=0)
Label(window, text="섭씨").grid(row=1)

e1=Entry(window)
e2=Entry(window)

e1.grid(row=0, column=1)
e2.grid(row=1,column=1)
cos = Button(window, text="화씨->섭씨",command=cos1).grid(row=3,column=0)       
fos = Button(window, text="섭씨->화씨",command=fos1).grid(row=3,column=1)
       
window.mainloop()
'''

class Rectangle:

    def __init__(self,side=0):

        self.side = side

    def getArea(self):

        return self.side*self.side

def printAreas(r,n):

    while n>=1:

        print(r.side,"\t",r.getArea())

        r.side = r.side + 1

        n=n-1

myRect=Rectangle()

count = 5

printAreas(myRect,count)

print("사각형의 변=",myRect.side)

print("반복횟수=",count)