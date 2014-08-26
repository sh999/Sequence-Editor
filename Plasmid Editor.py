'''
Plasmid Editor
8/18/14
'''
from Tkinter import *
from tkFileDialog import askopenfilename

def openFile():
	filename = askopenfilename(parent=root)
	f = open(filename)
	a = f.readlines()
	a = ''.join(a)
	a = a.replace('\n','')
	text.delete(1.0, END)
	text.insert(INSERT, a)
	seq.setSeq(a)

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
	filename = asksaveasfile(parent=root)

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
opn = Button(root, text="Open", command=openFile)
exit = Button(root, text="Exit", command=exit)
revComp = Button(root, text="Reverse Complement", command=revComp)
save = Button(root, text="Save", command=save)
test = Label(root, text="test")

text = Text(root)
text.insert(INSERT, 'lol')
text.grid(row=0,column=1, rowspan=6)
opn.grid(row=0, column=0, )
revComp.grid(row=1, column=0, sticky=N)
exit.grid(row=2, column=0, sticky=N)
save.grid(row=3, column=0)
test.grid(row=4, column=0, sticky=N)

root.rowconfigure(4, weight=1)
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)
root.geometry("400x400+500+200")

opnIcon = PhotoImage(file="openFolder.gif")
revcompIcon = PhotoImage(file="revcomp.gif")
opn.config(image=opnIcon,width="44", height="44")
revComp.config(image=revcompIcon, width="44", height="44")

root.mainloop()