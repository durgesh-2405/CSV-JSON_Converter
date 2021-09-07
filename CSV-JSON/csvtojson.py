# importing tkinter library to create GUI
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *

# importing pandas library
import pandas as pd

# initializing
head = tk.Tk()
head.title('CSV TO JSON')
head.geometry("500x500")

# creating the canvas of the Tool
canvas = tk.Canvas(head, bg='light cyan', relief='raised')
canvas.pack(fill=BOTH, expand=True)

# creating label heading.
labelHead = tk.Label(head, compound=tk.CENTER, text='\t        CSV TO JSON CONVERTER\t', bg='light cyan')
labelHead.config(font=('Arial', 25))

# determining the window size of heading
canvas.create_window(200, 75, anchor=CENTER, window=labelHead)
canvas.pack(fill=BOTH, expand=True)
#

# creating a global dictionary that will store the data read from CSV file.
dataframe = pd.DataFrame()


# function to select CSV file and read the data.
def read_csv():
    pathOfCSV = filedialog.askopenfilename()
    df = pd.read_csv(pathOfCSV)
    global dataframe
    dataframe = df.copy(deep=True)
    print(dataframe.head())


# creating a button which will call the readFromCSV function.
buttonToOpenCSV = tk.Button(text='  CHOOSE CSV FILE  ', command=read_csv, bg='OliveDrab1', fg='black',
                            font=('Arial', 15, 'bold'))
canvas.create_window(200, 160, window=buttonToOpenCSV)


# function to write the data to the JSON file.
def write_json():
    pathOfJSON = filedialog.asksaveasfilename(defaultextension='.json')
    dataframe.to_json(pathOfJSON)


# creating button which will call the writeToJSON function.
buttonToSaveJSON = tk.Button(text='  CONVERT CSV TO JSON  ', command=write_json, bg='OliveDrab1', fg='black',
                             font=('Arial', 15, 'bold'))
canvas.create_window(200, 210, window=buttonToSaveJSON)


# function to quit the application with a warning dialog box.
def close_app():
    warningBox = tk.messagebox.askquestion('Quit Application', 'Are you sure you want to quit.', icon='warning')
    if warningBox == 'yes':
        head.destroy()


# creating button to quit the application
buttonToQuit = tk.Button(text='  QUIT APPLICATION  ', command=close_app, bg='red', fg='black',
                         font=('Arial', 15, 'bold'))
canvas.create_window(200, 260, window=buttonToQuit)

# to run the tkinter event loop until the application is closed by the user.
head.mainloop()
