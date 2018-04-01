# -*- coding: utf-8 -*-
from tkinter import *

import aiml
import os
kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")

window = Tk()
window.title("Chatbot")
window.height =12000
window.width = 12000
label_1 = Label(text= "conversation").grid(row=0)

messages = Text(window)
messages.grid(row=1)

label_2 = Label(text="Right Answer:").grid(row=2,sticky=W)
input_u = StringVar()
input_f = Entry(window, text=input_u)
input_f.grid(row=2,ipady=5, ipadx=100)

label_2 = Label(text="You Question:").grid(row=3,sticky=W)
input_user = StringVar()
input_field = Entry(window, text=input_user)
input_field.grid(row=3,ipady=5, ipadx=100)

prev = ''

def Enter_pressed(event):
    global prev

    input_get = input_field.get()
    input_r = input_f.get()

    if len(input_get) != 0:
        prev = input_get[:]
        print(prev)
        messages.insert(INSERT,'you: %s\n' % input_get)
        input_user.set('')
        messages.see(END)
        output = kernel.respond(input_get)
        messages.insert(INSERT,'Bot: %s\n' % output)
        print(output)
    elif len(input_r) != 0:
        with open('output.txt', 'a',encoding='utf-8') as f:
            f.write(prev + '->' + input_r + "\n")
        messages.insert(INSERT,'right ans: %s\n' % input_r)
        input_u.set('')
        messages.see(END)
        print(prev+'->'+input_r)
    else:
        messages.insert(INSERT,'Bot: no \n')
    # label.pack()
    return "break"

#frame = Frame(window)  # , width=300, height=300)
input_field.bind("<Return>", Enter_pressed)
input_f.bind("<Return>", Enter_pressed)
#frame.pack()


window.mainloop()
