import customtkinter
import tkinter  


class About(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
            
        self.label = customtkinter.CTkLabel(self, text='GitHub', font=('', 16))
        self.label.grid(row=0, column=4, padx=400, pady=[40,0])
        text_var1 = tkinter.StringVar(value='https://github.com/StripedBear/Parole')
        self.label2 = customtkinter.CTkEntry(self, width=270, state='readonly', textvariable=text_var1, font=('', 13))
        self.label2.grid(row=1, column=4, pady=[20, 40])
        
        self.label = customtkinter.CTkLabel(self, text='If you have any questions:', font=('', 16))
        self.label.grid(row=2, column=4, pady=[40,0])
        text_var2 = tkinter.StringVar(value='stripedbear@tutanota.com')
        self.label2 = customtkinter.CTkEntry(self, width=190, state='readonly', textvariable=text_var2, font=('', 13))
        self.label2.grid(row=3, column=4, pady=[20, 0])
 
