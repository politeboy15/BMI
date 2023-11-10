from tkinter import *
from tkinter import messagebox
 
def calculate_bmi():
   kg = int(weight_tf.get())
   m = int(height_tf.get())/100
   bmi = kg/(m*m)
   bmi = round(bmi, 1)
 
   if bmi < 18.5:
       messagebox.showinfo('Answer', f'ИМТ = {bmi} соответствует недостаточному весу')
   elif (bmi > 18.5) and (bmi < 24.9):
       messagebox.showinfo('Answer', f'ИМТ = {bmi} соответствует нормальному весу')
   elif (bmi > 24.9) and (bmi < 29.9):
       messagebox.showinfo('Answer', f'ИМТ = {bmi} соответствует избыточному весу')
   else:
       messagebox.showinfo('Answer', f'ИМТ = {bmi} соответствует ожирению')  
 
window = Tk()
window.title('BMI v 0.0.1')
window.geometry('400x300')
window.configure(background='aqua')
 
frame = Frame(
   window,
   padx=10,
   pady=10,
   background='aqua'
)
frame.pack(expand=True)
 
 
height_lb = Label(
   frame,
   text="Your height  ",
   font='Arial 18',
   background='aqua'
)
height_lb.grid(row=3, column=1)
 
weight_lb = Label(
   frame,
   text="Your mass  ",
   font='Arial 18',
   background='aqua'
)
weight_lb.grid(row=4, column=1)
 
height_tf = Entry(
   frame,
)
height_tf.grid(row=3, column=2, pady=5)
 
weight_tf = Entry(
   frame,
)
weight_tf.grid(row=4, column=2, pady=5)
 
cal_btn = Button(
   frame,
   text='Calculate',
   command=calculate_bmi,
   background='cadetblue1',
   font = 'Arial 25'
)
cal_btn.grid(row=5, column=2)
 
window.mainloop()