import tkinter

def convert():
    converted_num = round(float(input.get()) * 1.6)
    number_label['text'] = converted_num
    return converted_num

def clear_input():
    input.delete(0, tkinter.END)


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

convert_button = tkinter.Button(text='Convert', command=convert, bg='light blue')
convert_button.grid(column=1, row=2)

clear_button = tkinter.Button(text='Clear', command=clear_input, bg='light pink')
clear_button.grid(column=2, row=2)
window.mainloop()