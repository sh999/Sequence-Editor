from Tkinter import *
class App:
	def __init__(self, master):
		self.a = 0
		frame = Frame(master) # a frame is a container for widgets
		frame.pack()

		self.but1 = Button(
			frame, text="1", command=self.but(1))
		self.but1.pack(side=TOP)

		self.but2 = Button(
			frame, text="2", command=self.f)
		self.but2.pack(side=TOP)



		self.display = Text(frame, height=5, width=20)

		self.display.pack()

	def but(self, a):
		self.display.delete(1.0, END)
		self.a = a;
		self.display.insert(END, self.a)
	def f(self):
		pass
	
root = Tk()
app = App(root)
root.mainloop()
