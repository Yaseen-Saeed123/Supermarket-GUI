from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

# Make a dict holding the menu of the shop
shop = {
    "Rice" : 34,
    "Milk" : 18,
    "Bozo" : 10,
    "Salsa" : 15, 
    "Meat" : 500,
}

def submit():
    text = ""
    new_lines = []
    total = 0
    try:
        # Loop through items to support multiple selections
        if rice_value.get() == 1:
            quantity = int(rice_quantity.get())
            price = shop['Rice']
            new_lines.append(f"Rice = {quantity} x {price} = {quantity * price} pounds")
            total += quantity * price

        if milk_value.get() == 1:
            quantity = int(milk_quantity.get())
            price = shop['Milk']
            new_lines.append(f"Milk = {quantity} x {price} = {quantity * price} pounds")
            total += quantity * price

        if bozo_value.get() == 1:
            quantity = int(bozo_quantity.get())
            price = shop['Bozo']
            new_lines.append(f"Bozo = {quantity} x {price} = {quantity * price} pounds")
            total += quantity * price

        if salsa_value.get() == 1:
            quantity = int(salsa_quantity.get())
            price = shop['Salsa']
            new_lines.append(f"Salsa = {quantity} x {price} = {quantity * price} pounds")
            total += quantity * price

        if meat_value.get() == 1:
            quantity = int(meat_quantity.get())
            price = shop['Meat']
            new_lines.append(f"Meat = {quantity} x {price} = {quantity * price} pounds")
            total += quantity * price

        if total == 0:
            messagebox.showwarning(title="No order made", message="No items selected")
            name.focus_set()
            return

        new_lines.append("----------------------------------------------")
        new_lines.append(f"Total price (No tax added): {total} pounds")
        new_lines.append(f"Total price (Tax added 14%): {round(total * 1.14, 2)} pounds")
        new_lines.append("----------------------------------------------")
        new_lines.append(f"Customer name: {name.get()}")
        new_lines.append("=================================\n")

        text = "\n".join(new_lines)
        with open("Bills.txt", 'w', newline='') as file:
            file.write(text)

        messagebox.showinfo(title="Bill", message=text[:-1])
        clear()
        
    except ValueError:
        messagebox.showwarning(title="Invalid input", message="Please enter valid quantities")
        name.focus_set()
        return


# Make a clear function
def clear():
    name.delete(0, "end")
    rice_value.set(0)
    milk_value.set(0)
    bozo_value.set(0)
    salsa_value.set(0)
    meat_value.set(0)
    rice_quantity.delete(0, "end")
    milk_quantity.delete(0, "end")
    bozo_quantity.delete(0, "end")
    salsa_quantity.delete(0, "end")
    meat_quantity.delete(0, "end")
    name.focus_set()

# Start
root = Tk()
root.title("Senson and boz shop")
root.geometry("370x350")
root.resizable(False, False)
# Label
welcome = Label(root, text="Welcome to Hyper market", font="Arial 20 bold")
welcome.grid(row=0, column=0, columnspan=4, sticky="we", pady=10, padx=10)

# Customer name
name_label = Label(root, text="Customer name")
name = ttk.Entry(root, width = 20)

name_label.grid(row=1, column=0, sticky="we")
name.grid(row=1, column=1)
name.focus_set()

# Order id
id = str(random.randint(1, 100000))

# Shopping items
rice_value=IntVar(value=0)
rice =ttk.Checkbutton(root, text="Rice", variable=rice_value)
rice_quantity = ttk.Entry(root, width=5)

rice.grid(row=2, column=0, pady=10)
rice_quantity.grid(row=2, column=1, padx=3, pady=10)

milk_value=IntVar(value=0)
milk =ttk.Checkbutton(root, text="Milk", variable=milk_value)
milk_quantity = ttk.Entry(root, width=5)

milk.grid(row=3, column=0, pady=10)
milk_quantity.grid(row=3, column=1, padx=3, pady=10)

bozo_value = IntVar(value=0)
bozo =ttk.Checkbutton(root, text="Bozo", variable=bozo_value)
bozo_quantity = ttk.Entry(root, width=5)

bozo.grid(row=4, column=0, pady=10)
bozo_quantity.grid(row=4, column=1, padx=3, pady=10)

salsa_value = IntVar(value=0)
salsa =ttk.Checkbutton(root, text="Salsa", variable=salsa_value)
salsa_quantity = ttk.Entry(root, width=5)

salsa.grid(row=5, column=0, pady=10)
salsa_quantity.grid(row=5, column=1, padx=3, pady=10)

meat_value = IntVar(value=0)
meat =ttk.Checkbutton(root, text="Meat", variable=meat_value)
meat_quantity = ttk.Entry(root, width=5)

meat.grid(row=6, column=0, pady=10)
meat_quantity.grid(row=6, column=1, padx=3, pady=10)

# Buttons
submit_button = ttk.Button(root, text="Submit Order", command=submit)
submit_button.grid(row=7, column=0, padx=10, pady=3, columnspan=2)

clear_button = ttk.Button(root, text="Clear Order", command=clear)
clear_button.grid(row=7, column=1, padx=3, pady=10, columnspan=2)

# Update
root.mainloop()