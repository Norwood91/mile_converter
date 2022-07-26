import tkinter

window = tkinter.Tk()
window.title('Mile to Km Converter')
window.minsize(width=500, height=300)
window.maxsize(width=500, height=300)
window.config(padx=125, pady=100)

input = tkinter.Entry()
input.grid(column=1, row=0)


mile_label = tkinter.Label(text='Miles')
mile_label.grid(column=2, row=0)
mile_label.config(padx=10, pady=10)

equal_label = tkinter.Label(text='Is equal to: ')
equal_label.grid(column=0, row=1)
equal_label.config(pady=10)


number_label = tkinter.Label(text='0')
number_label.grid(column=1, row=1)
number_label.config(pady=10)

km_label = tkinter.Label(text='Km')
km_label.grid(column=2, row=1)
km_label.config(pady=10)

button = tkinter.Button(text='Calculate')
button.grid(column=1, row=2)
button.config(pady=10)


window.mainloop()