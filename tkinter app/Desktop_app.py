import tkinter as tk
import random

''' tkinter grid contains columns and rows 3*3
and you spiecify the place for the items in grid  
tkinter some window attruibtes
'''

window = tk.Tk()
window.title("Hello___")
window.geometry("500x700")

#------------some functions-----

def p_G():
	ph = [' hallo', ' hello', ' marhba', ' azycko', ' salmoalyckom']
	name = str(en1.get())
	return ph[random.randint(0,6)] + name



def p_D():
		Ge = p_G()

		p_D = tk.Text(master=window, height=10, width=30)
		p_D.grid(column=0, row=3)
		p_D.insert(tk.END, Ge)	
#some componts like buttons labels etc..

#----------labels for texts-----
title = tk.Label(text="hello all")
title.grid(column=0, row=0)

title2 = tk.Label(text="what is your name bitch?? ")
title2.grid(column=0, row=1)



#--------inputs ===== enteries---------
en1=tk.Entry()
en1.grid(column=1, row=1)



#-----------buttons-------
bu1=tk.Button(text='click it', command=p_D)
bu1.grid(column=0, row=2, )


window.mainloop()
