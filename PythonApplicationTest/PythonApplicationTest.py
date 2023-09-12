from tkinter import *
from ctypes import CDLL, c_double


mydll = CDLL("..\\TestDLL\\x64\\Debug\\TestDLL.dll")

add_function = mydll.add
add_function.argtypes = [c_double, c_double]
add_function.restype = c_double


def clickListener():
    myText.set(str(add_function(float(e1.get()), float(e2.get()))))

mainWindow = Tk()
mainWindow.title("EarTechnic Task Demo")
mainWindow.geometry("300x300")
app = Frame(mainWindow)
app.grid(pady=20, padx=40)

myText = StringVar("")
Label(app,text="A").grid(row=0, pady=5, padx=5)
Label(app,text="B").grid(row=1)


e1 = Entry(app)
e2 = Entry(app)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(app, text="TOPLA", command=clickListener).grid(row=3, column=1, sticky=W, pady=5, padx=30)

Label(app, text="Toplam").grid(row=4,padx=4)
Label(app, textvariable=myText).grid(row=4, column=1, sticky=W, pady=4,padx=4)

mainWindow.mainloop()





