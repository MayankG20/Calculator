from tkinter import *
import tkinter.messagebox as msg
import parser
from time import sleep
import re

root=Tk()

root.title("Calculator")
#adding the input field
display=Entry(root)
display.grid(row=0,columnspan=10,sticky=W+E)

i=0
count1=0
def dis(n):
	global i
	global count1
	# print(i,count1)
	x=display.get()
	if x=="Error":
		dis1()
		count1=0
		dis(n)
	else:
		if count1==0:
			# print("no add kru")
			display.insert(i,n)
			i+=len(n)
		else:
			# print("result htau kya")
			x=re.search(r"[0-9]",n)
			if x:
				dis1()
				count1=0
				dis(n)
			else:
				count1=0
				dis(n)

def dis1():
	global i
	i=0
	display.delete(0,END)

def dis2():
	global i
	if i>0:
		display.delete(i-1,END)
		i-=1
	else:
		msg.showinfo("Warning","There is nothing to delete")

def dis4():
	ent_string=display.get()
	global count1
	global i
	count1=1
	try:
		a=parser.expr(ent_string).compile()
		result=eval(a)
		dis1()
		display.insert(0,result)
		i+=len(str(result))
	except Exception:
		dis1()
		display.insert(0,"Error")
		# sleep(5)
		# dis1()

Button(root,text="7",bg="Royalblue",command=lambda : dis("7")).grid(row=1,column=0,sticky=W+E,padx=2,pady=2)
Button(root,text="8",bg="Royalblue",command=lambda : dis("8")).grid(row=1,column=1,sticky=W+E,padx=2,pady=2)
Button(root,text="9",bg="Royalblue",command=lambda : dis("9")).grid(row=1,column=2,sticky=W+E,padx=2,pady=2)

Button(root,text="4",bg="Royalblue",command=lambda : dis("4")).grid(row=2,column=0,sticky=W+E,padx=2,pady=2)
Button(root,text="5",bg="Royalblue",command=lambda : dis("5")).grid(row=2,column=1,sticky=W+E,padx=2,pady=2)
Button(root,text="6",bg="Royalblue",command=lambda : dis("6")).grid(row=2,column=2,sticky=W+E,padx=2,pady=2)

Button(root,text="1",bg="Royalblue",command=lambda : dis("1")).grid(row=3,column=0,sticky=W+E,padx=2,pady=2)
Button(root,text="2",bg="Royalblue",command=lambda : dis("2")).grid(row=3,column=1,sticky=W+E,padx=2,pady=2)
Button(root,text="3",bg="Royalblue",command=lambda : dis("3")).grid(row=3,column=2,sticky=W+E,padx=2,pady=2)

Button(root,text="0",bg="Royalblue",command=lambda : dis("0")).grid(row=4,column=0,sticky=W+E,padx=2,pady=2)
Button(root,text=".",bg="lightgreen",command=lambda : dis(".")).grid(row=4,column=1,sticky=W+E,padx=2,pady=2)
Button(root,text="%",bg="lightgreen",command=lambda : dis("%")).grid(row=4,column=2,sticky=W+E,padx=2,pady=2)

Button(root,text="/",bg="lightgreen",command=lambda : dis("/")).grid(row=1,column=3,sticky=W+E,padx=2,pady=2)
Button(root,text="*",bg="lightgreen",command=lambda : dis("*")).grid(row=2,column=3,sticky=W+E,padx=2,pady=2)
Button(root,text="-",bg="lightgreen",command=lambda : dis("-")).grid(row=3,column=3,sticky=W+E,padx=2,pady=2)
Button(root,text="+",bg="lightgreen",command=lambda : dis("+")).grid(row=4,column=3,sticky=W+E,padx=2,pady=2)

Button(root,text="del",bg="White",command=lambda : dis2()).grid(row=1,column=4,sticky=W+E,padx=2,pady=2)
Button(root,text="(",bg="Magenta",command=lambda : dis("(")).grid(row=2,column=4,sticky=W+E,padx=2,pady=2)
Button(root,text="sq",bg="lightgreen",command=lambda : dis("**(2)")).grid(row=3,column=4,sticky=W+E,padx=2,pady=2)
b=Button(root,text="=",bg="Royalblue",command=lambda : dis4()).grid(row=4,column=4,columnspan=2,sticky=W+E,padx=2,pady=2)

Button(root,text="AC",bg="White",command=lambda : dis1()).grid(row=1,column=5,sticky=W+E,padx=2,pady=2)
Button(root,text=")",bg="Magenta",command=lambda : dis(")")).grid(row=2,column=5,sticky=W+E,padx=2,pady=2)
Button(root,text="sqrt",bg="lightgreen",command=lambda : dis("**(1/2)")).grid(row=3,column=5,sticky=W+E,padx=2,pady=2)
root.mainloop()