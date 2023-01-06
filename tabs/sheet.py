import time
import tkinter.messagebox

from tkinter import ttk, END, BOTH, RIGHT, Y, filedialog
import customtkinter
from stegano import exifHeader


class Sheet(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.selected_line = ''

        self.columns = ('service', 'login', 'email', 'password', 'comment', 'changed')
        self.tree = ttk.Treeview(self.parent, columns=self.columns, show="headings")
        self.tree.pack(expand=1, fill=BOTH)

        self.tree.heading("service", text="service", anchor='center', command=lambda: self.sort(0, False))
        self.tree.heading("login", text="login", anchor='center', command=lambda: self.sort(1, False))
        self.tree.heading("email", text="email", anchor='center', command=lambda: self.sort(2, False))
        self.tree.heading("password", text="password", anchor='center', command=lambda: self.sort(3, False))
        self.tree.heading("comment", text="comment", anchor='center', command=lambda: self.sort(4, False))
        self.tree.heading("changed", text="changed", anchor='center', command=lambda: self.sort(5, False))

        for i in range(5):
            self.tree.column(f"#{i + 1}", width=150)

        self.service_entry = customtkinter.CTkTextbox(self, width=160, height=10)
        self.service_entry.grid(row=0, column=0, pady=[20, 0], padx=[30, 5])
        self.name_entry = customtkinter.CTkTextbox(self, width=160, height=10)
        self.name_entry.grid(row=0, column=1, padx=[0, 5], pady=[20, 0])
        self.email_entry = customtkinter.CTkTextbox(self, width=160, height=10)
        self.email_entry.grid(row=0, column=2, padx=[0, 5], pady=[20, 0])
        self.pass_entry = customtkinter.CTkTextbox(self, width=160, height=10)
        self.pass_entry.grid(row=0, column=3, padx=[0, 5], pady=[20, 0])
        self.comment_entry = customtkinter.CTkTextbox(self, width=160, height=10)
        self.comment_entry.grid(row=0, column=4, pady=[20, 0])

        self.add_line_button = customtkinter.CTkButton(self, text='Add line', command=self.add_line)
        self.add_line_button.grid(row=1, column=0, pady=[20, 10])
        self.edit_line_button = customtkinter.CTkButton(self, text='Update', command=self.update_line)
        self.edit_line_button.grid(row=1, column=1, pady=[20, 10])
        self.delete_line_button = customtkinter.CTkButton(self, text='Delete line', command=self.delete_line)
        self.delete_line_button.grid(row=1, column=2, pady=[20, 10])

        self.open_button = customtkinter.CTkButton(self, text='Open', command=self.open)
        self.open_button.grid(row=2, column=0)
        self.open_button = customtkinter.CTkButton(self, text='Save', command=self.save)
        self.open_button.grid(row=2, column=1)

        self.tree.bind("<<TreeviewSelect>>", self.item_selected)

    def sort(self, col, reverse):
        l = [(self.tree.set(k, col), k) for k in self.tree.get_children("")]
        l.sort(reverse=reverse)
        for index, (_, k) in enumerate(l):
            self.tree.move(k, "", index)
        self.tree.heading(col, command=lambda: self.sort(col, not reverse))

    def save(self):
        save_file_path = filedialog.asksaveasfilename()
        if save_file_path != "":
            save_list = []
            try:
                for child in self.tree.get_children():
                    save_values = []
                    save_values.append(self.tree.item(child)["values"][0])
                    save_values.append(self.tree.item(child)["values"][1])
                    save_values.append(self.tree.item(child)["values"][2])
                    save_values.append(self.tree.item(child)["values"][3])
                    save_values.append(self.tree.item(child)["values"][4])
                    save_values.append(self.tree.item(child)["values"][5])
                    save_list.append(save_values)
                exifHeader.hide(save_file_path, save_file_path, str(save_list))
                tkinter.messagebox.showinfo('Parole Info', 'D0N3!')
            except IndexError:
                tkinter.messagebox.showerror('Parole Info', 'Remove empty lines!')
            except Exception as e:
                tkinter.messagebox.showerror('Parole Info', e)

    def open(self):
        self.filepath = filedialog.askopenfilename()
        if self.filepath != "":
            [self.tree.delete(item) for item in self.tree.get_children()]
            base = eval(exifHeader.reveal(self.filepath).decode())
            [self.tree.insert("", END, values=data) for data in base]

    def add_line(self):
        new_line = ('', '', '', '', '')
        self.tree.insert("", 0, values=new_line)

    def delete_line(self):
        question = tkinter.messagebox.askyesno("Parole Info", "The line will be permanently deleted. Are you sure?")
        if question:
            self.tree.delete(self.selected_line)

    def item_selected(self, event):
        self.selected_line = self.tree.selection()
        for selected_item in self.selected_line:
            item = self.tree.item(selected_item)
            self.service_entry.delete('0.0', END)
            self.service_entry.insert('0.0', item['values'][0])
            self.name_entry.delete('0.0', END)
            self.name_entry.insert('0.0', item['values'][1])
            self.email_entry.delete('0.0', END)
            self.email_entry.insert('0.0', item['values'][2])
            self.pass_entry.delete('0.0', END)
            self.pass_entry.insert('0.0', item['values'][3])
            self.comment_entry.delete('0.0', END)
            self.comment_entry.insert('0.0', item['values'][4])

    def update_line(self):
        new_data = (self.service_entry.get('0.0', END).rstrip(), self.name_entry.get('0.0', END).rstrip(),
                    self.email_entry.get('0.0', END).rstrip(), self.pass_entry.get('0.0', END).rstrip(),
                    self.comment_entry.get('0.0', END).rstrip(), time.ctime())
        self.tree.item(self.selected_line, values=new_data)

