#WELCOME TO MY RENT CALCULATOR 
import tkinter as tk
from tkinter import messagebox

def calculateRent():
                    room_rent = int(entry_rent.get())
                    food_spent = int(entry_food.get())
                    electric_unit_charge = float(entry_electric_charge.get())
                    unit_consumed = float(entry_units.get())
                    roommates = int(entry_roommates.get())

                    if room_rent < 0 or food_spent < 0 or electric_unit_charge < 0 or unit_consumed < 0 or roommates < 0:
                                                                        messagebox.showerror("Input Error", "Values cannot be negative.")
                                                                        return

                    totalElectricBill = electric_unit_charge * unit_consumed
                    total_cost = (room_rent + food_spent + totalElectricBill)

                    if roommates >= 0:
                              if roommates == 0:
                                  per_person_cost = total_cost
                              else:
                                  per_person_cost = total_cost//roommates

                              
                             
                    else:
                              per_person_cost = total_cost

                    result_text.set(f"Total Bill: R{total_cost:.2f}\nEach Pays: R{per_person_cost:.2f}" if roommates > 0 else f"Total Bill: R{total_cost:.2f}")

                   

# Creating the GUI Window
root = tk.Tk()
root.title("Room Rent & Expenses Calculator")
root.geometry("400x350")
root.resizable(False, False)

# Labels and Entry Fields
tk.Label(root, text="Enter Rent Amount (R):").pack()
entry_rent = tk.Entry(root)
entry_rent.pack()

tk.Label(root, text="Enter Food Spending (R):").pack()
entry_food = tk.Entry(root)
entry_food.pack()

tk.Label(root, text="Electricity Unit Charge (R):").pack()
entry_electric_charge = tk.Entry(root)
entry_electric_charge.pack()

tk.Label(root, text="Units Consumed:").pack()
entry_units = tk.Entry(root)
entry_units.pack()

tk.Label(root, text="Number of Roommates:").pack()
entry_roommates = tk.Entry(root)
entry_roommates.pack()

# Button to Calculate
tk.Button(root, text="Calculate", command=calculateRent).pack(pady=10)

# Display Result
result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, font=("Arial", 12, "bold"), fg="blue").pack()

# Run the GUI
root.mainloop()
