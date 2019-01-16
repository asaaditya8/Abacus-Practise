import tkinter as tk
import random
import time

window = tk.Tk()
window.title("Practice APP")
window.geometry("630x400")

entries = []
act_anss = []

class entry_gen():
	def __init__(self, w):
		self.w = w
		self.dayValue = tk.StringVar() 

	def limitSizeDay(self, *args):
	    value = self.dayValue.get()
	    if len(value) > self.w: self.dayValue.set(value[:self.w])

	def place(self, x, y):
		self.dayValue.trace('w', self.limitSizeDay)
		day_entry1= tk.Entry(width=self.w, textvariable=self.dayValue)
		day_entry1.grid(column=x, row=y)
		entries.append(day_entry1)

def label_gen(text, x, y):
	label1 = tk.Label(text=text, font=('arial', 10), justify='right')
	label1.grid(column=x, row=y)

def rand_int():
	neg = False
	p = random.randint(1,100)
	if p < 30:
		neg = True
	a = 0
	if neg:
		while a==0:
			a = random.randint(-9,-1)
	else:
		while a==0:
			a = random.randint(1,9)
	return a

def prob_gen(rows, x, y):
	nums = []
	indices = list(range(rows))
	for i in indices:
		nums.append(rand_int())

	act_ans = sum(nums)
	text = '\n'.join([str(i) for i in nums])
	label_gen(text, x, y)

	entry1 = entry_gen(2)
	entry1.place(x,rows+1)
	act_anss.append(act_ans)

def prob_row_gen(rows, func):
	for i in range(25):
		func(rows, i, 1)

class timer():
	def __init__(self):
		self.text1 = tk.Label(text='00:00', font=('arial', 12))
		self.text1.grid(column=25, row=0)
	
	def put(self, text):
		self.text1.config(text=text)

class score_labels():
	def __init__(self, x, y):
		self.label1 = tk.Label(text='', font=('arial', 12))
		self.label1.grid(column=x, row=y)
		self.label2 = tk.Label(text='', font=('arial', 12))
		self.label2.grid(column=x, row=y+1)
	
	def evaluate(self):
		self.score = 0
		for e, a in zip(entries, act_anss):
			val = e.get()
			if val == '':
				val = 0
			if a == int(val):
				self.score += 1
		self.acc = self.score * 100 / len(entries)

	def update(self):
		self.evaluate()
		self.label1.config(text=str(self.score) + '/25')
		self.label2.config(text=str(self.acc) + '%')
		et = time.time()
		t = int(et - st)
		s = str(t//60) + ':' + str(t%60)
		clock.put(s)

def submit_button(x, y, func):
	button1 = tk.Button(text='Submit', command=func)
	button1.grid(column=x, row=y)

clock = timer()
prob_row_gen(10, prob_gen)
s = score_labels(25, 13)
submit_button(25, 12, s.update)
st = time.time()

window.mainloop()