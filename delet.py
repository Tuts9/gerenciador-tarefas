import customtkinter as ctk
import sqlite3
from conID import ConsultarID

ctk.set_appearance_mode('light')

class DeletarTarefa:
    def __init__(self, root):
        self.root = root
        self.root.title('Deletar tarefa')
        self.root.geometry('400x400')
        
        self.label_inicio = ctk.CTkLabel(self.root, text='Deletar Tarefas', font=('Arial', 25, 'bold'), text_color='#4169E1')
        self.label_inicio.pack(pady=15)

        self.label_del = ctk.CTkLabel(self.root, text='Digite o id da tarefa que deseja apagar:', font=('Arial', 15))
        self.label_del.pack(pady=10)
        
        
        self.entry_delet = ctk.CTkEntry(self.root, placeholder_text='Id da tarefa..')
        self.entry_delet.pack()
        self.bt_delet = ctk.CTkButton(self.root, text='Apagar tarefa', command=self.deletar_tarefa)
        self.bt_delet.pack(pady=10)


        self.bt_id = ctk.CTkButton(self.root, text='Consultar ID', command=self.consultar_id)
        self.bt_id.pack(pady=65)


    def deletar_tarefa(self):
        conexao = sqlite3.connect('listTasks.db')
        c = conexao.cursor()
        c.execute("DELETE FROM tb_tarefas WHERE N_ID_TAREFA = ?", (self.entry_delet.get(),))
        conexao.commit()
        conexao.close()

        self.entry_delet.delete(0, ctk.END)

    def consultar_id(self):
        nova_janela = ctk.CTk()
        interface_id = ConsultarID(nova_janela)
        interface_id.iniciarInterface()
        
    def iniciarInterface(self):
        self.root.mainloop()

if __name__ == '__main__':
    root = ctk.CTk()
    merc = DeletarTarefa(root)
    merc.iniciarInterface()