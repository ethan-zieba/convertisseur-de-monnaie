import tkinter as tk
import customtkinter as ctk
from forex_python.converter import CurrencyRates as cRates

rates = cRates()
ratesEUR = rates.get_rates('EUR')


def update_result(*args):
    try:
        result.delete(0, ctk.END)
        result.insert(0, float(entry1.get())/first_currency*second_currency)
    except ValueError:
        result.delete(0, ctk.END)
        result.insert(0, "0")


first_curr_status = 1
first_currency = 1
second_currency = ratesEUR["USD"]


def change_currency(curr):
    try:
        global first_curr_status
        global first_currency
        global second_currency
        if curr == "EUR":
            label_text = "EUR" + " 1"
        else:
            label_text = str(curr) + " " + str(ratesEUR[curr])
        if first_curr_status == -1:
            entry1label.configure(text=label_text)
            if curr == "EUR":
                first_currency = 1
            else:
                first_currency = ratesEUR[curr]
            first_curr_status = 1
        elif first_curr_status == 1:
            if curr == "EUR":
                second_currency = 1
            else:
                second_currency = ratesEUR[curr]
            resultlabel.configure(text=label_text)
            first_curr_status = -1
    except KeyError:
        custom_currency_entry.delete(0, ctk.END)
        custom_currency_entry.insert(0, "Non valid curr.")


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
root.title("Currency Converter")
root.geometry("345x265")

entry1label = ctk.CTkLabel(root, width=10, text="EUR " + str(first_currency))
resultlabel = ctk.CTkLabel(root, width=10, text="USD " + str(second_currency))
entry1 = ctk.CTkEntry(root, width=80)
result = ctk.CTkEntry(root, width=80)
converted_label = ctk.CTkLabel(root, width=50, text=" Converted:")
converted_label.grid(row=1, column=0, columnspan=2)
entry1label.grid(row=0, column=0)
entry1.grid(row=1, column=0, padx=5, pady=5)
result.grid(row=1, column=1, padx=5, pady=5)
resultlabel.grid(row=0, column=1)

entry1.bind("<KeyRelease>", update_result)

currencies = ["EUR", "USD", "GBP", "JPY", "CAD", "CHF"]
row_num = 2
col_num = 0
for currency in currencies:
    button = ctk.CTkButton(root, text=currency, command=lambda curr=currency: change_currency(curr))
    button.grid(row=row_num, column=col_num, padx=5, pady=5)
    col_num += 1
    if col_num > 1:
        col_num = 0
        row_num += 1

custom_currency_label = ctk.CTkLabel(root, text="Other currencies:\n(BGN CZK DKK HUF PLN RON \nSEK ISK NOK TRY AUD BRL \nCNY HKD IDR INR KRW MXN \nMYR NZD PHP SGD THB ZAR)")
custom_currency_label.grid(row=row_num, column=0, padx=4, pady=4, rowspan=2)

custom_currency_entry = ctk.CTkEntry(root, width=100)
custom_currency_entry.grid(row=row_num, column=1, padx=1, pady=1)

apply_button = ctk.CTkButton(root, text="Apply", command=lambda: change_currency(custom_currency_entry.get()))
apply_button.grid(row=row_num+1, column=1, padx=5, pady=5)

root.mainloop()
