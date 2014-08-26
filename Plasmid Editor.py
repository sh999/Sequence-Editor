'''
Plasmid Editor
8/18/14
'''
from Tkinter import *
from tkFileDialog import *
from tkMessageBox import *

def openFile():
	filename = askopenfilename(parent=root)
	f = open(filename)
	a = f.readlines()
	a = ''.join(a)
	a = a.replace('\n','')
	text.delete(1.0, END)
	
	text.insert(INSERT, a)
	seq.setSeq(a)
	fileModified = True
	text.insert(0.1, "fileModified="+str(fileModified)+"\n")

def revComp():
	ref = list(seq.getSeq()[::-1]) # Converted to list b/c string is immutable
	rcSeq = list('x'*len(ref))
	for i in range(0, len(ref)):
		if ref[i] == 'A':
			rcSeq[i] = 'T'
		if ref[i] == 'C':
			rcSeq[i] = 'G'
		if ref[i] == 'T':
			rcSeq[i] = 'A'
		if ref[i] == 'G':
			rcSeq[i] = 'C'
	rcSeq = ''.join(rcSeq)
	seq.setSeq(rcSeq)
	text.delete(1.0, END)
	text.insert(INSERT, rcSeq)

def save():
	filename = asksaveasfile(mode='w', defaultextension=".txt")

def exiting():
	text.insert(0.1, "fileModified="+str(fileModified)+"\n")

	if fileModified == True:
		text.insert(INSERT, "file modified?  Exit?")
	else:
		text.insert(INSERT, "file not modified")

class Sequence:
	def __init__(self):
		self.s = ''
	def getSeq(self):
		return self.s 
	def setSeq(self,s):
		self.s = s


root = Tk()
seq = Sequence()
root.title("Plasmid Editor")
fileModified = False
opn = Button(root, text="Open", command=openFile)
exit = Button(root, text="Exit", command=exiting)
revComp = Button(root, text="Reverse Complement", command=revComp)
save = Button(root, text="Save", command=save)


text = Text(root)
debugText = Text(root)
debugText.insert(INSERT, "hey")
text.grid(row=0,column=1, rowspan=5)
opn.grid(row=0, column=0, )
revComp.grid(row=1, column=0)
save.grid(row=2, column=0)
exit.grid(row=3, column=0)
# debugText.grid(row=4, column=0)

root.rowconfigure(4, weight=1)
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)

root.geometry("400x300+500+200")

opnIcon = PhotoImage(file="openFolder.gif")
revcompIcon = PhotoImage(file="revcomp.gif")
saveIcon = PhotoImage(file="save.gif")

opn.config(image=opnIcon,width="44", height="44")
revComp.config(image=revcompIcon, width="44", height="44")
save.config(image=saveIcon)

root.mainloop()