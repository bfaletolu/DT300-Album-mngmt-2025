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
        
