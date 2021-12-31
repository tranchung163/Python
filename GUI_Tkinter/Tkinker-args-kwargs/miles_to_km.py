import tkinter as tk
from typing import Text

window = tk.Tk()
window.title('Mile to Km Converter')
window.minsize(width=250, height=150)


#Kilometer
km_label = tk.Label(text='Km', font=('Ariel',14,'bold'))
km_label.grid(column=0, row=1)
km_output = tk.Label(text=0)
km_output.grid(column=0,row=3)

#Mile
mile_label = tk.Label(text='Mile', font=('Ariel',14,'bold'))
mile_label.grid(column=0, row=0)
mile_input = tk.Entry(width=7)
mile_input.grid(column=0,row=1)

#Button
def miles_to_km():
    miles = float(mile_input.get())
    kilo = float(miles * 1.609)
    km_output.config(text=f'{kilo}')
    print(kilo)
button = tk.Button(text='Calculate', command=miles_to_km)
button.grid(column=1,row=2)

window.mainloop()