import tkinter as tk

window = tk.Tk()
window.title('First GUI program')
window.minsize(width= 500, height=300)
window.config(padx=200, pady=100)

#label
my_lable = tk.Label(text='i am a label', font=('Ariel', 24,'bold'))
my_lable.config(text='new text')
my_lable.grid(column=0, row=0)
my_lable.config(padx=20, pady=30)
#button
def button_clicked():
    print('click')

button = tk.Button(text='click me',command=button_clicked)
button.grid(column=1,row=1)


button2 = tk.Button(text='click 2', command=button_clicked)
button2.grid(column=2,row=0)

#Entry
input= tk.Entry(width=10)
print(input.get())
input.grid(column=5,row=5)




window.mainloop()