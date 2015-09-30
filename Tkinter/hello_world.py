from Tkinter import *

def hello():
    print('hello darion.j.yaphet')

window = Tk()
window.title('hi~')
window.geometry('400x200')

button = Button(window, text='Click me', command=hello)
button.pack(expand=YES, fill=BOTH)

mainloop()
