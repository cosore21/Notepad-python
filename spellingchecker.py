import tkinter 
from tkinter import*
from textblob import TextBlob




root=Tk()
root.title("Spelling Checker")
root.geometry("900x500+400+90")

root.config(bg="green")

def check_spelling():
    word=enter_text.get()
    a=TextBlob(word)
    right=str(a.correct())

    cs=Label(root,text="Correct text is :", font=("romans",18),bg="green",fg="white")
    cs.place(x=100,y=250)
    spell.config(text=right)


heading= Label(root,text="Spelling Checker",font="Roman 24 bold", bg="green",fg="white")
heading.pack(pady=(50,0))

enter_text=Entry(root,justify="center",width=30,font=("poppins",24),bg='white',border=2)
enter_text.pack(pady=10)
enter_text.focus()

button=Button(root,text="check",font=("roman" ,8 ,"bold"),fg="white",bg="red",command=check_spelling)
button.pack()

spell=Label(root,font=("poppins",18),bg="green",fg="white")
spell.place(x=350,y=250)



root.mainloop()