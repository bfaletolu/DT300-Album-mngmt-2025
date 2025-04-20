##
# album_mngmt_system.py
# program that manages albums and their information in one system using GUI
# Brooklyn Faletolu
# 15/04/2025

from tkinter import *

Class Album:
    """Supporting class for GUI"""

    def __init__(self, album_name, artist, amount_of_copies):
        """Setting up parameters for information for the albums & initialise album object with provided details"""
        self.album_name = album_name
        self.artist = artist
        self.amount_of_copies = amount_of_copies

    def get_info(self):
        """Return a formatted string of the stocks details"""

        return()


# Dictionary of stock and associated info mapped by album name
stock = {
    "Thriller": Album("Thriller", "Micheal Jackson", "15"),
    "Rumours": Album("Rumours", "Fleetwood Mac", "20"),
    "Born To Run": Album("Born To Run", "Bruce Springsteen", "10")
    }



Class AlbumGUI:        
    """Setting up GUI structure to manage stock records"""

    def __init__(self, root):
        """Initialise GUI components & layout with parameters"""

        self.root = root
        self.root.title("Album Management")
        self.root.geometry("400x600")

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
