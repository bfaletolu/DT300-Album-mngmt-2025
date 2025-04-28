"""This file enables the user to manage their album stock."""

##
# album_mngmt_system.py
# program that manages albums and their information in one system using GUI
# Brooklyn Faletolu
# 15/04/2025

from tkinter import *


class Album:
    """Supporting class for GUI."""

    def __init__(self, album_name, artist, amount_of_copies, sold):
        """Initialize album objects with provided details and parameters."""
        self.album_name = album_name
        self.artist = artist
        self.amount_of_copies = int(amount_of_copies)
        self.sold = sold

    def get_total_sold(self):
        """Track total amount checkecd out for an album."""
        return self.sold

    def get_total_stock(self):
        """Track total amount of stock left for an album."""
        return self.amount_of_copies

    def get_info(self):
        """Return a formatted string of the stocks details."""
        return(f"{self.album_name} by {self.artist}\n"
               f"-- {self.amount_of_copies} copies.")


# Dictionary of stock and associated info mapped by album name
stock = {
    "Thriller": Album("Thriller", "Micheal Jackson", 15, 0),
    "Rumours": Album("Rumours", "Fleetwood Mac", 20, 0),
    "Born To Run": Album("Born To Run", "Bruce Springsteen", 10, 0)
    }

# Constants for code
MAX_STOCK_LIMIT = 50
MAX_RESTOCK_LIMIT = 50
MIN_RESTOCK_LIMIT = 1


class AlbumGUI:
    """Setting up GUI structure to manage stock records."""

    def __init__(self, root):
        """Initialise GUI components & layout with parameters."""
        self.root = root
        self.root.title("Album Management")
        self.root.geometry("560x230+200+200")
        self.root.configure(bg='#001d3e')

        # Entry input & label
        self.entry_label = Label(root, text="Input:", anchor="w",
                                 bg='#001d3e', fg='#ff97cc',
                                 font=('comic sans ms', 13, 'bold'))
        self.entry_label.grid(row=0, column=0, pady=10, padx=10, sticky=E+W)
        self.entry_box = Entry(root, bg='#ff97cc')
        self.entry_box.grid(row=0, column=2, pady=10, padx=10, sticky=E+W)

        # Output display area
        self.output_text = Text(root, height=10, width=50, bg='#ff97cc')
        self.output_text.grid(row=1, column=2, rowspan=5,
                              padx=10, sticky=N+S+E+W)

        # Checkout, restock & show buttons
        self.btn1 = Button(root, text="Checkout Album", bg='#ff97cc',
                           fg='#001d3e', command=self.checkout_album,
                           font=('comic sans ms', 10, 'bold'))
        self.btn1.grid(row=1, column=0, padx=10, sticky=E+W)
        self.btn2 = Button(root, text="Restock Album", bg='#ff97cc',
                           fg='#001d3e', command=self.restock_album,
                           font=('comic sans ms', 10, 'bold'))
        self.btn2.grid(row=2, column=0, padx=10, sticky=E+W)
        self.btn3 = Button(root, text="Show Albums", bg='#ff97cc',
                           fg='#001d3e', command=self.show_albums,
                           font=('comic sans ms', 10, 'bold'))
        self.btn3.grid(row=3, column=0, padx=10, sticky=E+W)

        # Total stock and sold labels
        self.total_stock_label = Label(root, text="", anchor="w",
                                       bg='#001d3e', fg='#ff97cc',
                                       font=('comic sans ms', 10, 'bold'))
        self.total_stock_label.grid(row=4, column=0, padx=10, sticky=E+W)
        self.total_sold_label = Label(root, text="", anchor="w",
                                      bg='#001d3e', fg='#ff97cc',
                                      font=('comic sans ms', 10, 'bold'))
        self.total_sold_label.grid(row=5, column=0, padx=10, sticky=E+W)

        # Show totals at start
        self.show_total_stock()
        self.show_total_sold()

        # Show all albums at start
        self.show_albums()

    def get_entry(self):
        """Get user input from entry box."""
        return self.entry_box.get().title().strip()

    def show_output(self, text):
        """Display text in output area."""
        self.output_text.delete("1.0", END)  # Clear box before adding new text
        self.output_text.insert(END, text)

    def show_total_stock(self):
        """Display and update total stock."""
        # Total number of album copies
        total_stock = 0

        # Loop through album values
        for album in stock.values():
            # Add get_total_stock() to total_sold
            total_stock += album.get_total_stock()

        # Update total_stock_label with total_stock using config
        self.total_stock_label.config(text=f"Total Stock: {total_stock}")

    def show_total_sold(self):
        """Display total amount sold."""
        # Total number of album copies sold
        total_sold = 0

        # Loop through album values
        for album in stock.values():
            # Add get_total_sold() to total_sold
            total_sold += album.get_total_sold()

        # Update total_sold_label with total_sold using config
        self.total_sold_label.config(text=f"Total Sold: {total_sold}")

    def show_albums(self):
        """Display album with information."""
        album_list = "Inventory:\n\n"

        # Loop through album values
        for album in stock.values():
            # Add get_info() to album list
            album_list += album.get_info() + "\n\n"

        # Print album list using show_output
        self.show_output(album_list)

    def checkout_album(self):
        """Show stock and allow user to choose and checkout an album."""
        # Get user input
        album_name = self.get_entry()

        # Check if album is in stock dictionary
        if album_name in stock:
            album = stock[album_name]  # Get album from stock

            if album.get_total_stock() > 0:  # Ensure the album is in stock
                album.amount_of_copies -= 1
                album.sold += 1

                # Show success message and stock using get_total_stock
                self.show_output(
                    f"Checkout successful!\n\n"
                    f"{album.get_info()}"
                )

                # Update total stock and sold
                self.show_total_stock()
                self.show_total_sold()

            else:
                self.show_output(f"Sorry, {album_name} is out of stock!")

        else:
            self.show_output("Please choose an album that is in our stock.\n")

    def restock_album(self):
        """Allow user to choose and restock an album."""
        # Get user entry
        input_data = self.get_entry()

        if input_data == "":  # Ensure data was entered
            self.show_output(
                "Please enter the album and restock amount in this format:\n"
                "\nalbum name,restock amount"
                )
            return

        # Split input string by commas
        parts = [p.strip() for p in input_data.split(',')]

        # Rebuild album name until we reach restock amount
        album_name_parts = []

        # Keep taking parts until restock amount found
        while parts and not parts[0].isdigit():
            album_name_parts.append(parts.pop(0))
        album_name = " ".join(album_name_parts)  # reconstruct album name

        if not parts:
            self.show_output(
                "Please include a restock amount."
                "\n(album name,restock amount)"
                )
            return

        restock_amount_str = parts.pop(0)  # Get restock amount as a string

        if not restock_amount_str.isdigit():  # Make sure it is a number
            self.show_output("Please use a number for restock amount.")
            return

        restock_amount = int(restock_amount_str)  # Convert to integer

        # Check if album is in stock dictionary
        if album_name in stock:
            album = stock[album_name]  # Get album from stock

            # set reasonable boundaries with constants
            if MAX_RESTOCK_LIMIT >= restock_amount >= MIN_RESTOCK_LIMIT:

                # Ensure album copies are within MAX_STOCK_LIMIT
                if MAX_STOCK_LIMIT < album.amount_of_copies + restock_amount:

                    # Calculate max restock number allowed
                    max_restock = MAX_STOCK_LIMIT - album.amount_of_copies

                    # Show max limit reached message and max restock allowed
                    self.show_output(
                        f"Maximum of {MAX_STOCK_LIMIT} copies per album.\n\n"
                        f"{album_name} has {album.get_total_stock()} in stock."
                        f"\nYou are able to restock {max_restock} copies."
                        f"\n\nPlease enter an amount between:\n"
                        f"{MIN_RESTOCK_LIMIT} to {max_restock}."
                        )

                else:
                    album.amount_of_copies += restock_amount

                    # Show success message and stock num using get_total_stock
                    self.show_output(
                        f"Restock Successful!\n"
                        f"{album.get_info()}"
                    )

                    # Update total stock and sold
                    self.show_total_stock()
                    self.show_total_sold()

            else:
                self.show_output(
                    "Please input a reasonable number to restock."
                    f"({MIN_RESTOCK_LIMIT} to {MAX_RESTOCK_LIMIT})"
                )

        else:
            self.show_output("Please choose an album that is in our stock.\n")


if __name__ == "__main__":
    root = Tk()
    gui = AlbumGUI(root)
    root.mainloop()
