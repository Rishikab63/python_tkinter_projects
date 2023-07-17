
#USING TKINTER

from tkinter import *
import math
import tkinter.messagebox as tmsg

import string
import random

def generate():
    s1 = string.ascii_lowercase #lowercase- lowercase letters dega   
        #print(s1)               
    s2 = string.ascii_uppercase    #uppercase dega
        #print(s2) 
    s3 = string.digits    #uppercase dega
        #print(s3) 
    s4 = string.punctuation
        #print(s4)
        
      

    #blank list and then sb s ko concatenate kr de rhe and then printing
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))    #s1->string hai and esko list bnna kai s mai dal rhe
    s.extend(list(s3))
    s.extend(list(s4))
    #print(s)   #stores all the character used to make strong password

    random.shuffle(s)   #s shuffle ho jaiga

    #8print(s)

    #ab shuffled s mai sai plen ka character nikalenge 

    l=int(e1.get())

    sf="".join(s[0:l])
    Label(root, text="Your Password is- %s"%(sf),padx=10, pady=5,font=("Arial", 25, "bold") ).grid(padx=30,pady=40)
    tmsg.showinfo("Password","Password Generated")
    




root = Tk()

root.title("Password Geneator")
root.geometry("600x300")
root.config(bg="powderblue")

#creating class
Label(root, text="Enter the length: ", bg="#ff9999", padx=5, pady=5, width=20, font=("Arial", 25, "bold") ).grid(column=0,row=0,padx=30,pady=50)

e1=Entry(root, bg="black",fg="white",  width=20,font=("Arial", 25))
e1.grid(column=0,row=1,padx=50,pady=20)

b1=Button(root,text="GENERATE", command=generate, bg="black",fg="white",width=10, font=("Arial", 15, "bold"))
b1.grid(padx=100,pady=20)
        



mainloop()


#label


#mainmenu=Menu(root)

'''#commands-
add_commands(label="Help",command=help)
mainmenu.add_cascade(label="Help",menu=m3)'''




