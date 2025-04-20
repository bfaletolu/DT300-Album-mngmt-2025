##
# album_mngmt_system.py
# program that manages albums and their information in one system using GUI
# Brooklyn Faletolu
# 15/04/2025

from tkinter import *

class Album:
    """Supporting class for GUI"""

    def __init__(self, album_name, artist, amount_of_copies):
        """Setting up parameters for information for the albums & initialise album object with provided details"""
        self.album_name = album_name
        self.artist = artist
        self.amount_of_copies = int(amount_of_copies)
        

    def get_info(self):
        """Return a formatted string of the stocks details"""

        return f"{self.album_name} by {self.artist} -- {self.amount_of_copies} copies."


# Dictionary of stock and associated info mapped by album name
stock = {
    "Thriller": Album("Thriller", "Micheal Jackson", 15),
    "Rumours": Album("Rumours", "Fleetwood Mac", 20),
    "Born To Run": Album("Born To Run", "Bruce Springsteen", 10)
    }


class AlbumGUI:        
    """Setting up GUI structure to manage stock records"""

    def __init__(self, root):
        """Initialise GUI components & layout with parameters"""

        self.root = root
        self.root.title("Album Management")
        self.root.geometry("600x600")

        # Entry input & label
        self.entry_label = Label(root, text="Input:")
        self.entry_label.pack()
        self.entry_box = Entry(root)
        self.entry_box.pack()

        # Output display area
        self.output_text = Text(root, height=30, width=45)
        self.output_text.pack()

        # Buttons
        self.btn1 = Button(root, text="Checkout Item", command=self.checkout_item)
        self.btn1.pack()
        self.btn2 = Button(root, text="Restock Item", command=self.restock_item)
        self.btn2.pack()

    def get_entry(self):
        """Get user intput from entry box"""

        return self.entry_box.get().strip()
    
    def show_total_stock(self):
        """Display and update total stock"""

    def show_total_sold(self):
        """Display total amount sold"""
        
    def checkout_item(self):
        """Allows user to choose and checkout an item"""

    def restock_item(self):
        """Allows user to choose and restock an item"""
        
if __name__ == "__main__":
    root = Tk()
    gui = AlbumGUI(root)
    root.mainloop()
