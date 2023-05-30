from stock_api import StockApi
from PIL import ImageTk, Image
from database import StockDatabase  
import customtkinter
import tkinter as tk
from tkinter import ttk

stockApi = StockApi()
database = StockDatabase()

class GridAssistantInterface:
    
    #####ROOT#####

    root = tk.Tk()
    root.title("Stock Exchange Assistant")
    
     #####STYLING#####
    
    s = ttk.Style()
    s.configure('mainFrame.TFrame', background = '#3A3845')
    s.configure('Frame2.TFrame', background = '#ECF8F9')
    
    
    #####WIDGETS#####
    mainFrame = ttk.Frame(root, width = 250, height = 250, style = "mainFrame.TFrame")
    mainFrame.grid()
    
    #Frame2 = ttk.Frame(mainFrame, width = 200, height = 200, style = 'Frame2.TFrame')
    #Frame2.grid(padx = 10, pady = 10)
    
    button = ttk.Button(root, text = "Test")
    button.grid(column = 1, row = 1)
    #####GRID CONFIGURATIONS#####
    
    root.resizable(width = False, height = False)
    root.mainloop()