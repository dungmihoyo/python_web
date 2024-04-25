
from tkinter import StringVar, ttk 
from tkinter import PhotoImage 

from PIL import Image, ImageTk 
import tkinter as tk 

class App (tk.Tk) : 
    def __init__(self) -> None:
        super().__init__()
        
        self.username= tk.StringVar() 
        self.password = tk.StringVar() 
        
        
        self.title("Login Window")
        self.geometry("360x600")
        
        image = Image.open('./assert/bg.jpg')
        self.bg_image = ImageTk.PhotoImage(image) 
        ttk.Label(self, image= self.bg_image ).pack( )    
        
        self.label_intro = ttk.Label(self, text = "WELCOME TO \n  CHATBOT !!", font = ("Arial", 30) )
        

        self.entry_user = ttk.Entry(self, textvariable= self.username, font= ("Arial", 20), width= 19)  
        self.label_user = ttk.Label(self, text= "username: ", font = ("Arial", 12) )
 
        
        
        self.entry_pass = ttk.Entry(self, textvariable= self.password) 
        
        self.label_intro.place(x = 40, y = 70)
        
        self.entry_user.place(x = 40, y = 200)
        self.label_user.place(x = 45, y = 210)
        
        
if __name__ == "__main__" : 
    app = App() 
    app.mainloop( )

