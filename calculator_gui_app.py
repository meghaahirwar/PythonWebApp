#Calculator by using Tkinter
from tkinter import *
   
root = Tk()   #root is an instance/object for TK() class
root.geometry("465x450")  #height x width
# root.minsize(200,100)
# root.maxsize(1000,1000)
root.title("My Calculator")

#for Icon
root.wm_iconbitmap("download.ico")

def click(event):    #Tkinter internally passes a parameter as event in the function. so when event will trigger then function will call
    # print("Hello")
    # pass
    global screenValue
    text = event.widget.cget("text")   #These widgets are the functional units on any Tkinter GUI application. Tkinter Widgets There are various controls, such as buttons, labels, scrollbars, radio buttons, and text boxes
    print(text)
    
    if text == "=":
        if screenValue.get().isdigit():
            value = int(screenValue.get())
        else:
            value=eval(entryBox.get())
        
        screenValue.set(value)
        entryBox.update()     
    elif text == "CLEAR":
        screenValue.set("")
        entryBox.update()
        
    elif text == "BACK":
        text_len = len(screenValue.get())
        screenValue.set(text_len)
        entryBox.update()
        
    else:
        screenValue.set(screenValue.get() + text)
        entryBox.update()

screenValue = StringVar()
screenValue.set("")
entryBox = Entry( textvar = screenValue, font = "lucida 20 bold", width=20, borderwidth=10, border=5, justify=RIGHT)
# screen.pack(fill= BOTH, ipadx=5, pady= 10, padx=8)
entryBox.pack(expand =YES, fill =BOTH, ipadx=5, pady= 10, padx=8)

frame1 = Frame(root, bg="grey")
btn = Button(frame1, text="CLEAR", font="lucida 15 bold", padx=220, pady=12, bg="dark red", fg="white")
# btn.pack(side=LEFT, padx=2, pady=2, expand =YES)
btn.pack(expand =YES, fill =BOTH, padx=2, pady=2)
btn.bind("<Button-1>", click)

frame1.pack(expand =YES, fill =BOTH)

frame1 = Frame(root, bg="grey")
btn = Button(frame1, text="9", font="lucida 15 bold", padx=50, pady=10, bg="Dark grey")
btn.pack(side=LEFT, padx=2, pady=2, expand =YES)
# btn.pack(expand =YES, fill =BOTH, padx=2, pady=2)
btn.bind("<Button-1>", click)

btn = Button(frame1, text="8", font="lucida 15 bold", padx=50, pady=10, bg="Dark grey")
btn.pack(side=LEFT, padx=2, pady=2, expand =YES)
# btn.pack(expand =YES, fill =BOTH, padx=2, pady=2)
btn.bind("<Button-1>", click)

btn = Button(frame1, text="7", font="lucida 15 bold", padx=50, pady=10, bg="Dark grey")
btn.pack(side=LEFT, padx=2, pady=2, expand =YES)
# btn.pack(expand =YES, fill =BOTH, padx=2, pady=2)
btn.bind("<Button-1>", click)

btn = Button(frame1, text="+", font="lucida 15 bold", padx=28, pady=10, bg="black" , fg="white")
btn.pack(side=LEFT, padx=2, pady=2, expand =YES)
# btn.pack(expand =YES, fill =BOTH, padx=2, pady=2)
btn.bind("<Button-1>", click)

frame1.pack(expand =YES, fill =BOTH)

frame1 = Frame(root, bg="grey")
btn = Button(frame1, text="6", font="lucida 15 bold", padx=50, pady=10, bg="Dark grey")
btn.pack(side=LEFT, padx=2, pady=2, expand =YES)
# btn.pack(expand =YES, fill =BOTH, padx=2, pady=2)
btn.bind("<Button-1>", click)

btn = Button(frame1, text="5", font="lucida 15 bold", padx=50, pady=10, bg="Dark grey")
btn.pack(side=LEFT, padx=2, pady=2, expand =YES)
# btn.pack(expand =YES, fill =BOTH, padx=2, pady=2)
btn.bind("<Button-1>", click)

btn = Button(frame1, text="4", font="lucida 15 bold", padx=50, pady=10, bg="Dark grey")
btn.pack(side=LEFT, padx=2, pady=2, expand =YES)
#btn.pack(expand =YES, fill =BOTH, padx=2, pady=2)
btn.bind("<Button-1>", click)

btn = Button(frame1, text="-", font="lucida 15 bold", padx=30, pady=10, bg="black" , fg="white")
btn.pack(side=LEFT, padx=2, pady=2, expand =YES)
# btn.pack(expand =YES, fill =BOTH, padx=2, pady=2)
btn.bind("<Button-1>", click)

frame1.pack(expand =YES, fill =BOTH)

frame1 = Frame(root, bg="grey")
btn = Button(frame1, text="3", font="lucida 15 bold", padx=50, pady=10, bg="Dark grey")
btn.pack(side=LEFT, padx=2, pady=2, expand =YES)
# btn.pack(expand =YES, fill =BOTH, padx=2, pady=2)
btn.bind("<Button-1>", click)

btn = Button(frame1, text="2", font="lucida 15 bold", padx=50, pady=10, bg="Dark grey")
btn.pack(side=LEFT, padx=2, pady=2, expand =YES)
# btn.pack(expand =YES, fill =BOTH, padx=2, pady=2)
btn.bind("<Button-1>", click)

btn = Button(frame1, text="1", font="lucida 15 bold", padx=50, pady=10, bg="Dark grey")
btn.pack(side=LEFT, padx=2, pady=2, expand =YES)
# btn.pack(expand =YES, fill =BOTH, padx=2, pady=2)
btn.bind("<Button-1>", click)

btn = Button(frame1, text= "*", font="lucida 15 bold", padx=30, pady=10, bg="black" , fg="white")
btn.pack(side=LEFT, padx=2, pady=2, expand =YES)
# btn.pack(expand =YES, fill =BOTH, padx=2, pady=2)
btn.bind("<Button-1>", click)

# btn = Button(frame1, text="=", font="lucida 35 bold", padx=32, pady=28)
# btn.pack(side=LEFT, padx=10, pady=10)
# btn.bind("<Button-1>", click)
frame1.pack(expand =YES, fill =BOTH)

frame1 = Frame(root, bg="grey")
btn = Button(frame1, text="0", font="lucida 15 bold", padx=50, pady=10, bg="Dark grey")
btn.pack(side=LEFT, padx=2, pady=2, expand =YES)
# btn.pack(expand =YES, fill =BOTH, padx=2, pady=2)
btn.bind("<Button-1>", click)

btn = Button(frame1, text=".", font="lucida 15 bold", padx=51, pady=10, bg="dark cyan")
btn.pack(side=LEFT, padx=2, pady=2, expand =YES)
# btn.pack(expand =YES, fill =BOTH, padx=2, pady=2)
btn.bind("<Button-1>", click)

btn = Button(frame1, text="=", font="lucida 15 bold", padx=50, pady=10, bg="Dark grey")
btn.pack(side=LEFT, padx=2, pady=2, expand =YES)
# btn.pack(expand =YES, fill =BOTH, padx=2, pady=2)
btn.bind("<Button-1>", click)

btn = Button(frame1, text="/", font="lucida 15 bold", padx=30, pady=10, bg="black" , fg="white")
btn.pack(side=LEFT, padx=2, pady=2, expand =YES)
# btn.pack(expand =YES, fill =BOTH, padx=2, pady=2)
btn.bind("<Button-1>", click)

frame1.pack(expand =YES, fill =BOTH)

# frame1 = Frame(root, bg="grey")
# btn = Button(frame1, text="=", font="lucida 20 bold", padx=220, pady=12, bg="black" , fg="white")
# btn.pack(side=LEFT, padx=2, pady=2, expand =YES)
# # btn.pack(expand =YES, fill =BOTH, padx=2, pady=2)
# btn.bind("<Button-1>", click)

# frame1.pack(expand =YES, fill =BOTH)
root.mainloop()