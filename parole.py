import customtkinter

from tabs import sheet, password_gen, about


class Parole(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Parole')
        self.geometry('900x650')
        self.tab_names = ["Sheet", "Password Gen", "About"]
        self.tabview = customtkinter.CTkTabview(self, width=900, height=650)
        self.tabview.pack()

        [self.tabview.add(tab) for tab in self.tab_names]

        sheet.Sheet(self.tabview.tab("Sheet")).pack(fill='both', expand=True)
        password_gen.PasswordGen(self.tabview.tab("Password Gen")).pack(fill='both', expand=True)
        about.About(self.tabview.tab("About")).pack(fill='both', expand=True)

        for item in self.tab_names:
            customtkinter.CTkLabel(self.tabview.tab(item),
                                   text='v.0.1 by StripedBear', font=('Arial', 10)).pack()


def close_window():
    program.destroy()


if __name__ == '__main__':
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")
    program = Parole()
    program.protocol('WM_DELETE_WINDOW', close_window)
    program.mainloop()


