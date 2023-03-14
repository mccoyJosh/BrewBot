import tkinter as tk

# Create a window
window = tk.Tk()
window.title("Coffee Order")


# Define function to handle button click
def handle_click(selection):
    print("You ordered a", selection)

# Create Espresso button
espresso_btn = tk.Button(window, text="Espresso", command=lambda: handle_click("Espresso"))
espresso_btn.pack()

# Create Normal Coffee button
normal_coffee_btn = tk.Button(window, text="Normal Coffee", command=lambda: handle_click("Normal Coffee"))
normal_coffee_btn.pack()

# Create Super Deluxe Coffee button
super_deluxe_btn = tk.Button(window, text="Super Deluxe Coffee", command=lambda: handle_click("Super Deluxe Coffee"))
super_deluxe_btn.pack()

# Run the window
window.mainloop()
