import tkinter as tk
from tkinter import messagebox

class RestrauntOrderManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Order Management app")
   
        self.menu_items = {
            "Fries MEAL ":2,
            "LUNCH ":2,
            "BURGER MEAL ":3,
            "PIZZA MEAL ":4,
            "CHEESE BURGER MEAL ":2.5,
            "DRINKS ":1,
        }
        self.exchange_rate = 82
        self.setup_background(root)
        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor = tk.CENTER)

        ttk.label(
            frame,
            text=" Restaurant Order Management ",
            font =("Italic", 20, "bold"),
        ).grid(row=0, columnspan=3, padx=10, pady=10)

        self.menu_labels = {}
        self.menu_quantities = {} 

        for i, (item,price) in enumerate(self.menu_items.items(), start=1):
            label = ttk.Label(frame, text=f"{item} - ${price}", font=("Italic", 12))
            label.grid(row=i, column=0, padx=10, pady=5)
            self.menu_labels[item] = label

            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] = quantity_entry

        self.currency_var = tk.StringVar()
        ttk.label(
            frame,
            text="Currency:",
            font=("Italic", 12)
        ).grid(row=len(self.menu_items)+1, column=0, padx=10, pady=5)
        