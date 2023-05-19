from stock_api import StockApi
from PIL import ImageTk, Image  
import customtkinter

stockApi = StockApi()

class AssistantInterface:
    
    global entry1
    
    def APIcall():
        stockApi.getCompanyCashflowData(entry1.get())

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    root = customtkinter.CTk()
    root.title("Stock Exchange Assistant")
    root.geometry("500x500")
    
    front_image = Image.open("./Pictures/logo.png")
    test = ImageTk.PhotoImage(front_image)
    
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label =customtkinter.CTkLabel(master=frame, text="Stock Exchange Assistant", font=("Roboto", 24)) # Custom text
    label.pack(pady=12, padx=10)

    entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Company Symbol") # Input field
    entry1.pack(pady=12, padx=10)

    button = customtkinter.CTkButton(master=frame, text="Draw diagramm", command=APIcall) # Button
    button.pack(pady=12, padx=10)
    
    label2 = customtkinter.CTkLabel(master=frame, image=test, text="")
    label2.pack(side = "bottom", fill = "both", expand = "yes")

    root.mainloop()


