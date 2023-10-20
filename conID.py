import customtkinter as ctk
import sqlite3
from sqlite3 import Error

ctk.set_appearance_mode('light')

class ConsultarID:
    def __init__(self, root):
        self.root = root
        self.root.title('Consultar ID')
        self.root.geometry('400x400')

    def query(self, conexao, sql, params=None):
        try:
            c = conexao.cursor()
            if params:
                c.execute(sql, params)
            else:
                c.execute(sql)
            conexao.commit()
        except Error as ex:
            print(ex)
        finally:
            print('Operação realizada com sucesso')
            conexao.close()

    def consultar(self, conexao, id_tarefa):
        c = conexao.cursor()
        c.execute("SELECT * FROM tb_tarefas WHERE N_ID_TAREFA = ?", (id_tarefa,))
        res = c.fetchall()
        conexao.close()
        return res




    def iniciarInterface(self):
        self.root.mainloop()

if __name__ == '__main__':
    root = ctk.CTk()
    merc = ConsultarID(root)
    merc.iniciarInterface()