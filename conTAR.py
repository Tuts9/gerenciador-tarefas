import customtkinter as ctk
import sqlite3

ctk.set_appearance_mode('light')

class ConsultarTarefa:
    def __init__(self, root):
        self.root = root
        self.root.title('Consultar tarefas')
        self.root.geometry('400x400')

        

    def iniciarInterface(self):
        self.root.mainloop()

if __name__ == '__main__':
    root = ctk.CTk()
    merc = ConsultarTarefa(root)
    merc.iniciarInterface()