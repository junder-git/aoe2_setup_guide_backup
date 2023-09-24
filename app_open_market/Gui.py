import tkinter as tk

class Gui:
    def __init__(self):
        # Create the first main window
        window1 = tk.Tk()
        window1.title("Window 1 - Item Trading")
        # Create buttons for the first window
        self.create_buttons(window1)
        # Create the second main window
        window2 = tk.Tk()
        window2.title("Window 2 - Item Trading")
        # Create buttons for the second window
        self.create_buttons(window2)
        # Start the GUI main loop for both windows
        window1.mainloop()
        window2.mainloop()
    def buy_item(self, item):
        print(f"Buying {item}")
    def sell_item(self, item):
        print(f"Selling {item}")
    # Function to create Buy and Sell buttons
    def create_buttons(self, window):
        # Buy buttons
        buy_food_button = tk.Button(window, text="Buy Food", command=lambda: self.buy_item("Food"))
        buy_wood_button = tk.Button(window, text="Buy Wood", command=lambda: self.buy_item("Wood"))
        buy_gold_button = tk.Button(window, text="Buy Gold", command=lambda: self.buy_item("Gold"))
        buy_stone_button = tk.Button(window, text="Buy Stone", command=lambda: self.buy_item("Stone"))

        # Sell buttons
        sell_food_button = tk.Button(window, text="Sell Food", command=lambda: self.sell_item("Food"))
        sell_wood_button = tk.Button(window, text="Sell Wood", command=lambda: self.sell_item("Wood"))
        sell_gold_button = tk.Button(window, text="Sell Gold", command=lambda: self.sell_item("Gold"))
        sell_stone_button = tk.Button(window, text="Sell Stone", command=lambda: self.sell_item("Stone"))

        # Place Buy buttons on the left side
        buy_food_button.grid(row=0, column=0, padx=10, pady=5)
        buy_wood_button.grid(row=1, column=0, padx=10, pady=5)
        buy_gold_button.grid(row=2, column=0, padx=10, pady=5)
        buy_stone_button.grid(row=3, column=0, padx=10, pady=5)

        # Place Sell buttons on the right side
        sell_food_button.grid(row=0, column=1, padx=10, pady=5)
        sell_wood_button.grid(row=1, column=1, padx=10, pady=5)
        sell_gold_button.grid(row=2, column=1, padx=10, pady=5)
        sell_stone_button.grid(row=3, column=1, padx=10, pady=5)

