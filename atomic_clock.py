'''
This program retrieves the time from an atomic clock using web scrapping techniques and python.

Important note: This program does not have any bad intention on web scrapping 
https://watches.uhrzeit.org/atomic-clock.php, it just has been made for learning purposes.
'''
from tkinter import *
import requests
import bs4

# We create a window.
window = Tk()
window.title("Py Atomic Clock")

# We create a textbox, here will be displayed the atomic time
txtbox = Entry(window, font="Calibri 20")
txtbox.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

# Function that retrieves the hour from the internet.
def get_hour():
    # We retrieve all the info from the main page where is located the atomic clock
    re = requests.get("https://watches.uhrzeit.org/atomic-clock.php")
    soup = bs4.BeautifulSoup(re.text, "lxml")
    # We retrieve the hour.
    atomic_time = soup.select(".anzeige.zeit")[0]
    # We put it in the textbox.
    txtbox.insert(0,atomic_time.getText())


# We create a button that when you pressed it, the time refreshes.
refresh_button = Button(window, text="Refresh the clock!", command=get_hour)
refresh_button.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

window.mainloop()

