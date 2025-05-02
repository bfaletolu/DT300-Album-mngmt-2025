PROJECT TITLE:
Album_mngmt_system


PURPOSE OF PROJECT:
Managing the stock of albums in the shop.


VERSION DATE:
28/04/2025


AUTHORS:
Brooklyn Faletolu


USER INSTRUCTIONS:
The large white box on the right side of the screen is the “Output Box”, where information depending on what button you press will be displayed. In the bottom left corner, you’ll find two labels: “Total stock” and “Total sold”. These display the current amount of album copies in stock and the total number of album copies that have been sold. These labels will instantly update whenever an album is checked out or restocked.


Checking out:
To check out an album, enter the album name in the white input box located at the top of the screen, next to the “Input:” label. Then, confirm your checkout by pressing the “checkout album” button located on the left just under the “Input:” label. When an album is successfully checked out, a message will appear in the “Output box” that confirms the check out, along with the remaining stock of the chosen album. However, if the chosen album is out of stock, you will get an error message.


Restocking:
To restock an album, find the input bar to the right of the label named “Input:” and insert your chosen album and amount of copies you wish to restock by typing in the album name and restock amount separated by a comma (e.g: Thriller, 24). Then, confirm your restock by pressing the “Restock album” button found on the left side. When a restock is successful, a message will appear in the “Output box” that confirms the restock, along with the album details. However, there is a limit to the amount of albums allowed to restock at once and a max amount of copies per album the store can hold. If you enter a number surpassing the restock number limit an error message will display in the “Output box”. If you enter a number that would make the stock of that album surpass the max number of album copies per album limit an error message will appear in the “Output box”.
(Note: The store can only hold up to 150 album copies at once, 50 per album.)


Viewing the inventory:
To view the albums in the inventory, find and click the button labelled “Show album”. By pressing this button all of the albums in the store's inventory will be displayed in the “Output box” detailing the album name, artist and total copies currently in stock.


Editing the code:
You can edit the “MAX_STOCK_LIMIT” variable on line 44 if you want to change the amount of copies per album the store can hold at once. 


You can also change the “MAX_RESTOCK_LIMIT” variable to set the max amount of copies a restock is allowed. And, on line 46 is the “MIN_RESTOCK_LIMIT” variable which controls the lowest restock amount that is allowed.