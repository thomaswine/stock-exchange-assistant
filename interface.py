from stock_api import StockApi
from PIL import ImageTk, Image  
import customtkinter

stockApi = StockApi()

class AssistantInterface:
    
    global entry1
    global menu_var
    
    def APIcall(*args):
        global dropdown
        dropdown = str(menu_var.get())
        stockApi.getCompanyCashflowData(dropdown)    
        
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    root = customtkinter.CTk()
    root.title("Stock Exchange Assistant")
    root.geometry("500x800")

    test_list = ["IBM", "TSLA", "AAPL"]
    menu_var = customtkinter.StringVar(root)
    menu_var.set("Choose Symbol")
        
    front_image = customtkinter.CTkImage(light_image=Image.open("./Pictures/logo.png"), size=(400, 400))
    
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label =customtkinter.CTkLabel(master=frame, text="Stock Exchange Assistant", font=("Roboto", 24)) # Custom text
    label.pack(pady=12, padx=10)

    entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Company Symbol") # Input field
    entry1.pack(pady=12, padx=10)

    label2 = customtkinter.CTkLabel(master=frame, image=front_image, text="")
    label2.pack(side = "bottom", fill = "both", expand = "yes")
    
    menu = customtkinter.CTkOptionMenu(master=frame, hover=True, variable=menu_var, values=test_list)
    menu.pack(pady=12, padx=10)
    
    button = customtkinter.CTkButton(master=frame, text="Draw diagramm", hover=True, command=APIcall) # Button
    button.pack(pady=12, padx=10)
    
    root.mainloop()


