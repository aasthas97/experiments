"""Allows user to log and view daily entries. Daily mood ratings and notes can be logged.
 Future updates: Convert to a single class
 Issues: formatting of summary window"""

import tkinter as tk
from tkinter.ttk import Combobox
from openpyxl import load_workbook
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import os.path

def SaveEntry(date, month, year, moodrating, note): # get entries from all fields and export to csv file
    fulldate = month + ' ' + date + ', ' + year
    if not os.path.isfile('moodjournal.xlsx'):
        blank = pd.DataFrame()
        blank.loc[0, 0] = 'Date'
        blank.loc[0, 1] = 'Rating'
        blank.loc[0, 2] = 'Notes'
        # blank.columns = ['Date', 'Rating', 'Notes]
        blank.to_excel("moodjournal.xlsx", index = False, header = False)
        
    wb = load_workbook('moodjournal.xlsx')
    sheet = wb["Sheet1"]
    rowData = [fulldate, moodrating, note]
    sheet.append(rowData)
    wb.save('moodjournal.xlsx')
    
def AddEntry():
    EntryWindow = tk.Toplevel()
    EntryWindow.title('Add an entry')
    EntryWindow.geometry("800x300")
    EntryWindow.configure(background = 'white')
    tk.Label(EntryWindow, "", bg = 'white').grid(row = 0, column = 0)
    tk.Label(EntryWindow, text = "Date    ", bg = 'white', font = ('Helvetica', 12)).grid(row = 1, column = 0)
    Date = Combobox(EntryWindow, values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])
    Date.grid(row = 1, column = 2)
    Month = Combobox(EntryWindow, values = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    Month.grid(row = 1, column = 1)
    Year = Combobox(EntryWindow, values = [2020, 2021, 2022, 2023, 2024, 2025])
    Year.grid(row = 1, column = 3)
    tk.Label(EntryWindow, "", bg = 'white').grid(row = 2, column = 0)
    tk.Label(EntryWindow, text = "How do you feel today?", bg = 'white', font = ('Helvetica', 12)).grid(row = 3, column = 0)
    rating = tk.Scale(EntryWindow, bg = 'white', from_ = 0,  to = 10, orient = 'horizontal', width = 20, length = 400)
    rating.grid(row = 3, column = 1, columnspan = 3)
    tk.Label(EntryWindow, "", bg = 'white').grid(row = 5, column = 0)
    tk.Label(EntryWindow, text = 'Notes', bg = 'white', font = ('Helvetica', 12)).grid(row = 6, column = 0)
    notes = tk.Text(EntryWindow, bg = 'white', height = 5, width = 40)
    notes.grid(row = 6, column = 1, columnspan = 3)
    tk.Label(EntryWindow, "", bg = 'white').grid(row = 7, column = 0)
    tk.Label(EntryWindow, "", bg = 'white').grid(row = 8, column = 0)
    Save = tk.Button(EntryWindow, text = 'Save', padx = 50, pady = 5, bg = 'white', command = lambda: [SaveEntry(Date.get(), Month.get(), Year.get(), rating.get(), notes.get('1.0', 'end-1c')), EntryWindow.destroy()])
    Save.grid(row = 9, column = 2)
    
def OpenSummaryWindow():
    StatsWindow = tk.Toplevel()
    StatsWindow.title('View Summary')
    StatsWindow.configure(background = 'white')
    StatsWindow.geometry("700x400")
    statsframe = tk.Frame(StatsWindow, bg = 'white', height = 400, width = 700)
    statsframe.grid(row = 0, column = 0)
    tk.Label(statsframe, text = "", bg = 'white').grid(row = 0, column = 0)
    tk.Button(statsframe, text = 'View by Month', padx = 40, pady = 8, bg = 'white', command = lambda: [statsframe.destroy(), ChooseTime(StatsWindow, 'month')]).grid(row = 1, column = 1)
    tk.Label(statsframe, text = "", bg = 'white').grid(row = 2, column = 0)
    tk.Button(statsframe, text = 'View by Year', padx = 45, pady = 8, bg = 'white', command = lambda: [statsframe.destroy(), ChooseTime(StatsWindow, 'year')]).grid(row = 3, column = 1)

def ChooseTime(mainwindow, monthoryear):
    choosingframe = tk.Frame(mainwindow)
    choosingframe.pack()
    txt = 'View by ' + monthoryear
    tk.Label(choosingframe, text = txt, font = ('Helvetica', 16), bg = 'white').pack()
    if monthoryear == 'month':
        tk.Label(choosingframe, text = 'Choose month:', bg = 'white').pack()
        choice = Combobox(choosingframe, values = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    elif monthoryear == 'year':
        tk.Label(choosingframe, text = 'Choose year:', bg = 'white').pack()
        choice = Combobox(choosingframe, values = [2020, 2021, 2022, 2023, 2024, 2025])
        
    choice.pack()
    show = tk.Button(choosingframe, text = 'Show', bg = 'white', padx = 45, pady = 8, command = lambda: [ShowStats(mainwindow, choice.get()), choosingframe.destroy()])
    show.pack()
        
def ShowStats(mainwindow, choosetime):
    df = pd.read_excel('moodjournal.xlsx')
    dates = pd.Series.tolist(df.loc[:, 'Date'])
    ratings = [pd.Series.tolist(df.loc[df['Date'] == date, 'Rating']) for date in dates if choosetime in date]
    ratings = [item for sublist in ratings for item in sublist]
    # plot graph now
    f = Figure(figsize=(5,5), dpi=100)
    a = f.add_subplot(111)
    a.plot(ratings)  
    canvas = FigureCanvasTkAgg(f, master = mainwindow)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    
root = tk.Tk()
root.title('Mood Journal')
root.geometry("350x300")
root.configure(background = 'white')
tk.Label(root, text = "", bg = 'white').pack(side = 'top')
tk.Label(root, text = "Mood Journal",font=("Helvetica", 20), bg = 'white').pack(side = 'top')
tk.Label(root, text = "", bg = 'white').pack()
add_entry = tk.Button(root, text = 'Add entry', command = AddEntry, padx = 55, pady = 5, bg = 'white').pack()
tk.Label(root, text = "", bg = 'white').pack()
tk.Label(root, text = "", bg = 'white').pack()
view_stats = tk.Button(root, text = 'View Summary', command = OpenSummaryWindow, padx = 50, pady = 5, bg = 'white').pack()
tk.mainloop()
