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

        return f"{self.album_name} by {self.artist}\n-- {self.amount_of_copies} copies."


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
        self.output_text = Text(root, height=30, width=50)
        self.output_text.pack()

        # Checkout, restock & show buttons
        self.btn1 = Button(root, text="Checkout Album", command=self.checkout_album)
        self.btn1.pack()
        self.btn2 = Button(root, text="Restock Album", command=self.restock_album)
        self.btn2.pack()
        self.btn3 = Button(root, text="Show Albums", command=self.show_albums)
        self.btn3.pack()

        # Total stock label
        self.total_stock_label = Label(root, text="")
        self.total_stock_label.pack()
        
        # Total sold label
        self.total_sold_label = Label(root, text="")
        self.total_sold_label.pack()

        # Show totals at start
        self.show_total_stock()
        self.show_total_sold()

        # Show all albums at start
        self.show_albums()


    def get_entry(self):
        """Get user input from entry box"""

        return self.entry_box.get().title().strip()


    def show_output(self, text):
        """Display text in output area"""

        self.output_text.delete("1.0", END) # Clear box before adding new text
        self.output_text.insert(END, text)


    def show_total_stock(self):
        """Display and update total stock"""

        # Total number of album copies
        total_stock = 0

        # Loop through album values
        for album in stock.values():
            total_stock += int(album.amount_of_copies) # Add amount_of_copies to total_sold


        # Update total_stock_label with total_stock using config
        self.total_stock_label.config(text=f"Total Stock: {total_stock}")


    def show_total_sold(self):
        """Display total amount sold"""
        
        # Total number of album copies sold
        total_sold = 0

        # Loop through album values
        for album in stock.values():
            total_sold += int(album.sold) # Add sold to total_sold

        # Update total_sold_label with total_sold using config 
        self.total_sold_label.config(text=f"Total Sold: {total_sold}")


    def show_albums(self):
        """Display album with information"""
        
        album_list = "Please select an album:\n\n"

        # Loop through album values
        for album in stock.values():
            album_list += album.get_info() + "\n\n" # Add get _info to album list

        # Print album list using show_output
        self.show_output(album_list)
        
  
    def checkout_album(self):
        """Shows stock and allows user to choose and checkout an album"""

        # Get user input
        album_name = self.get_entry()

        
        if album_name in stock:
            album = stock[album_name] # Get album from stock

            if album.amount_of_copies > 0: # Ensure the album is in stock
                album.amount_of_copies -= 1
                album.sold += 1

                # Show success and remaining stock
                self.show_output(f"Checkout successful!\n\nRemaining stock: {album.amount_of_copies}")

                # Update total stock and sold
                self.show_total_stock()
                self.show_total_sold()
                       
            else:
                self.show_output("Sorry, out of stock!")
            
        else:
            self.show_output("Please choose an album that is in our stock.\n")                


    def restock_album(self):
        """Allows user to choose and restock an album"""

        


if __name__ == "__main__":
    root = Tk()
    gui = AlbumGUI(root)
    root.mainloop()
