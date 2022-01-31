from tkinter import *

# create a tkinter window and set padding
window = Tk()
window.title("Miles to KM Converter")
window.config(padx=20, pady=20)

# create labels
km_label = Label(text="KM", font=("Arial", 24))
km_label.grid(column=2, row=1)
miles_label = Label(text="Miles", font=("Arial", 24))
miles_label.grid(column=2, row=0)
equals_label = Label(text="is equal to", font=("Arial", 24))
equals_label.grid(column=0, row=1)
answer_label = Label(text="0", font=("Arial", 24))
answer_label.grid(column=1, row=1)

# take user input
user_input = Entry(justify="center")
user_input.config(width=5, font=("Arial", 24))
user_input.grid(column=1, row=0)


# define function to convert miles to KM
def m_to_km():
    miles = int(user_input.get())
    km = miles * 1.609344
    answer_label.config(text=int(km))


# Create button and assign m_to_km command
button = Button(text="Calculate", command=m_to_km, font=("Arial", 24))
button.grid(column=1, row=2)

window.mainloop()
