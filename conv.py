
from tkinter import *

root = Tk()
root.geometry('400x400')
root.title('Converter')

def process():
	global value
	global summ
	global returnn

	value = inpBin.get()
	decVal = bin(value)

	Label(root,text='Binary {}=> {}'.format(value,decVal),font=('Arial',13)).pack()

def processdec():
	global decValue
	decimal, i , n = 0,0,0
	decValue = inpDec.get()

	while(decValue != 0):
		dec = decValue % 10
		decimal += dec * pow(2,i)
		decValue = decValue // 10
		i += 1
	ans = Label(root,text='Decimal {} => {}'.format(inpDec.get(),decimal),font=('Arial',13)).pack()

Label(root,text='Decimal to Binary',font=('Arial',15)).pack()

inpBin = IntVar()
Label(root,text='Decimal',font=('Arial',13)).pack()
binaryEnt = Entry(root,textvariable=inpBin,width=10).pack()
Button(root,text='Submit',width=10,command=lambda:process()).pack()

inpDec = IntVar()
Label(root,text='Binary',font=('Arial',13)).pack()
binaryEnt = Entry(root,textvariable=inpDec,width=10).pack()
Button(root,text='Submit',width=10,command=lambda:processdec()).pack()

root.mainloop()


