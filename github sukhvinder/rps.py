
from tkinter import *
import random

root = Tk()
root.geometry("400x400")
root.title("RPS Game")
 

computer_value = { "0":"Rock" , "1":"Paper" , "2":"Scissor" }
score=0

def reset_game():
    global score
    score=0
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l0.config(text="score")
    l1.config(text = "Player              ")
    l3.config(text = "Computer")
    l4.config(text = "")
    

def isrock():
    global score
    #score+=1
    c_v = computer_value[str(random.randint(0,2))]
    if c_v == "Rock":
        match_result = "Match Draw"
    elif c_v=="Scissor":
        match_result = "Player Win"
        score+=1
    else:
        match_result = "Computer Win"
        score-=1
    l4.config(text = match_result)
    l1.config(text = "Rock            ")
    l3.config(text = c_v)
    l0.config(text = score)
    
 

def ispaper():
    global score
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Paper":
        match_result = "Match Draw"
    elif c_v=="Scissor":
        match_result = "Computer Win"
        score-=1
    else:
        match_result = "Player Win"
        score+=1
    l4.config(text = match_result)
    l1.config(text = "Paper           ")
    l3.config(text = c_v)
    l0.config(text = score)
    

 

def isscissor():
    global score
    c_v = computer_value[str(random.randint(0,2))]
    if c_v == "Rock":
        match_result = "Computer Win"
        score-=1
    elif c_v == "Scissor":
        match_result = "Match Draw"
    else:
        match_result = "Player Win"
        score+=1
    l4.config(text = match_result)
    l1.config(text = "Scissor         ")
    l3.config(text = c_v)
    l0.config(text = score)

 

Label(root,
      text = "Rock Paper Scissor",
      font = "normal 20 bold",
      fg = "blue").pack(pady = 20)

 
frame = Frame(root)
frame.pack()
 
l1 = Label(frame,
           text = "Player              ",
           font = 10)
 
l2 = Label(frame,text = "VS             ",font = "normal 10 bold")
 
l3 = Label(frame, text = "Computer", font = 10)
l0 = Label(frame, text = "Score :", font = 10)

l0.pack(side = LEFT) 
l1.pack(side = LEFT)
l2.pack(side = LEFT)
l3.pack()
 
l4 = Label(root,
           text = "",
           font = "normal 20 bold",
           bg = "white",
           width = 15 ,
           borderwidth = 2,
           relief = "solid")
l4.pack(pady = 20)
 
frame1 = Frame(root)
frame1.pack()
 
b1 = Button(frame1, text = "Rock",
            font = 10, width = 7,
            command = isrock)
 
b2 = Button(frame1, text = "Paper ",
            font = 10, width = 7,
            command = ispaper)
 
b3 = Button(frame1, text = "Scissor",
            font = 10, width = 7,
            command = isscissor)
 
b1.pack(side = LEFT, padx = 10)
b2.pack(side = LEFT,padx = 10)
b3.pack(padx = 10)
 
Button(root, text = "Reset Game",
       font = 10, fg = "red",
       bg = "black", command = reset_game).pack(pady = 20)
 

root.mainloop()