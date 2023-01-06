from typing import Callable, Union
import string
import random


from tkinter import END
import customtkinter


class PasswordGen(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label = customtkinter.CTkLabel(self, text='Password Generator', font=('', 16))
        self.label.grid(row=0, column=4, pady=20)

        self.upper = customtkinter.CTkCheckBox(self, text='bigs')
        self.upper.grid(row=2, column=0, pady=[0, 10])
        self.lower = customtkinter.CTkCheckBox(self, text='smalls')
        self.lower.grid(row=2, column=2, pady=[0, 10])
        self.special = customtkinter.CTkCheckBox(self, text='special')
        self.special.grid(row=3, column=0, pady=[0, 10])
        self.numbers = customtkinter.CTkCheckBox(self, text='numbers')
        self.numbers.grid(row=3, column=2, pady=[0, 10])

        self.spinbox_label = customtkinter.CTkLabel(self, text='<- Password Size ->')
        self.spinbox_label.grid(row=4, column=0, pady=[0, 10])
        self.spinbox_1 = FloatSpinbox(self, width=150, step_size=1)
        self.spinbox_1.grid(row=4, column=2, pady=[0, 10], padx=[0, 30])
        self.spinbox_1.set(8)

        self.generate_button = customtkinter.CTkButton(self, text='Go!', command=self.generator)
        self.generate_button.grid(row=6, column=0, pady=[0, 10], padx=[30, 30])
        self.textbox = customtkinter.CTkTextbox(self, width=430, height=400, corner_radius=8)
        self.textbox.grid(row=2, column=4, rowspan=6, columnspan=3, pady=[0, 10], padx=[30, 0])
        self.textbox.configure(state="disabled")

    def generator(self):
        self.textbox.configure(state="normal")
        self.textbox.delete('0.0', END)
        pass_set = ''
        if self.numbers.get():
            pass_set += string.digits
        if self.upper.get():
            pass_set += string.ascii_uppercase
        if self.lower.get():
            pass_set += string.ascii_lowercase
        if self.special.get():
            pass_set += string.punctuation
        parole = ''
        for n in range(self.spinbox_1.get()):
            parole += random.choice(pass_set)
        self.textbox.insert("0.0", parole)
        self.textbox.configure(state="disabled")


class FloatSpinbox(customtkinter.CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 32,
                 step_size: Union[int, float] = 1,
                 command: Callable = None,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.step_size = step_size
        self.command = command

        self.configure(fg_color=("gray78", "gray28"))  # set frame color

        self.grid_columnconfigure((0, 2), weight=0)  # buttons don't expand
        self.grid_columnconfigure(1, weight=1)  # entry expands

        self.subtract_button = customtkinter.CTkButton(self, text="-", width=height - 6, height=height - 6,
                                                       command=self.subtract_button_callback)
        self.subtract_button.grid(row=0, column=0, padx=(3, 0), pady=3)

        self.entry = customtkinter.CTkEntry(self, width=width - (2 * height), height=height - 6, border_width=0)
        self.entry.grid(row=0, column=1, columnspan=1, padx=3, pady=3, sticky="ew")

        self.add_button = customtkinter.CTkButton(self, text="+", width=height - 6, height=height - 6,
                                                  command=self.add_button_callback)
        self.add_button.grid(row=0, column=2, padx=(0, 3), pady=3)

        # default value
        self.entry.insert(0, "0.0")

    def add_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = int(self.entry.get()) + self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    def subtract_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = int(self.entry.get()) - self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    def get(self) -> Union[int, None]:
        try:
            return int(self.entry.get())
        except ValueError:
            return None

    def set(self, value: int):
        self.entry.delete(0, "end")
        self.entry.insert(0, str(int(value)))