##
# album_mngmt_system.py
# program that manages albums and their information in one system using GUI
# Brooklyn Faletolu
# 15/04/2025

from tkinter import *

class Album:
    """Supporting class for GUI"""

    def __init__(self, album_name, artist, amount_of_copies, sold):
        """Setting up parameters for information for the albums & initialise album object with provided details"""
        self.album_name = album_name
        self.artist = artist
        self.amount_of_copies = int(amount_of_copies)
        self.sold = sold

    def get_total_sold(self):
        """Track total amount checkecd out for an album"""
        
        return self.sold
    

    def get_total_stock(self):
        """Track total amount of stock left for an album"""

        return self.amount_of_copies


    def get_info(self):
        """Return a formatted string of the stocks details"""

        return f"{self.album_name} by {self.artist} -- {self.amount_of_copies} copies."


# Dictionary of stock and associated info mapped by album name
stock = {
    "Thriller": Album("Thriller", "Micheal Jackson", 15, 0),
    "Rumours": Album("Rumours", "Fleetwood Mac", 20, 0),
    "Born To Run": Album("Born To Run", "Bruce Springsteen", 10, 0)
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

        # Checkout & restock buttons
        self.btn1 = Button(root, text="Checkout Item", command=self.checkout_item)
        self.btn1.pack()
        self.btn2 = Button(root, text="Restock Item", command=self.restock_item)
        self.btn2.pack()

        # Total stock label
        self.total_stock_label = Label(root, text="")
        self.total_stock_label.pack()
        
        # Total sold label
        self.total_sold_label = Label(root, text="")
        self.total_sold_label.pack()

        # Show totals at start
        self.show_total_stock()
        self.show_total_sold()
        
    def get_entry(self):
        """Get user input from entry box"""

        return self.entry_box.get().strip()


    def show_total_stock(self):
        """Display and update total stock"""

        total_stock = 0
        for album in stock.values():
            total_stock += int(album.amount_of_copies)

        self.total_stock_label.config(text=f"Total Stock: {total_stock}")


    def show_total_sold(self):
        """Display total amount sold"""

        total_sold = 0
        for album in stock.values():
            total_sold += int(album.sold)

        self.total_sold_label.config(text=f"Total Sold: {total_sold}")


    def checkout_item(self):
        """Allows user to choose and checkout an item"""

    def restock_item(self):
        """Allows user to choose and restock an item"""
        
if __name__ == "__main__":
    root = Tk()
    gui = AlbumGUI(root)
    root.mainloop()
