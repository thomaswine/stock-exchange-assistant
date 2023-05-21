from stock_api import StockApi
from PIL import ImageTk, Image
from database import StockDatabase  
import customtkinter

stockApi = StockApi()
database = StockDatabase()

class AssistantInterface:
    
    #####STYLING#####
    
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    
    #####ROOT#####

    root = customtkinter.CTk()
    root.title("Stock Exchange Assistant")
    root.geometry("500x800")
    
    #####STYLING#####
    
    #####WIDGETS#####
    
    #####GRID CONFIGURATIONS#####
    
    root.resizable(width=)