import customtkinter as ctk
from tkinter import messagebox
import sqlite3
import pandas as pd
from adc import AdicionarTarefa
from delet import DeletarTarefa
from upd import AtualizarTarefa
from conID import ConsultarID
from conTAR import ConsultarTarefa

# ctk.set_appearance_mode('light')
# ctk.set_default_color_theme('green')

class ListaTarefas:
    def __init__(self, root):
        self.root = root
        self.root.title('Lista de tarefas')
        self.root.geometry('400x300') #+827+363
        self.root.resizable(False, False)
        
        # Labels
        self.label_inicio = ctk.CTkLabel(self.root, text='Lista de Tarefas', font=('Arial', 25, 'bold'))
        self.label_inicio.grid(padx=10,pady=10)

        # Botões
        self.botao_inserir = ctk.CTkButton(self.root, text='Adicionar tarefa', command=self.adicionar_tarefa, fg_color='#00FF00',hover_color='#228B22', text_color='#000000', font=('Arial', 15), height=35)
        self.botao_inserir.grid(row=1, column=0, padx=5, pady=5)
        
        self.botao_deletar = ctk.CTkButton(self.root, text='Apagar tarefa', command=self.deletar_tarefa, fg_color='#B22222',hover_color='#800000', text_color='#000000', font=('Arial', 15), height=35)
        self.botao_deletar.grid(row=1, column=1, padx=5, pady=5)
        
        self.botao_atualizar = ctk.CTkButton(self.root, text='Atualizar tarefa', command=self.atualizar_tarefa, text_color='#000000', font=('Arial', 15), height=35)
        self.botao_atualizar.grid(row=2, column=0, padx=5, pady=5)
        
        self.consultar_id = ctk.CTkButton(self.root, text='Consultar ID', command=self.consultar_id, fg_color='#B0C4DE', hover_color='#708090', text_color='#000000', font=('Arial', 15), height=35)
        self.consultar_id.grid(row=2, column=1, padx=5, pady=5)
        
        self.consultar_tarefa = ctk.CTkButton(self.root, text='Consultar tarefas', command=self.consultar_tarefa, fg_color='#F0E68C', hover_color='#FFD700', text_color='#000000', font=('Arial', 15), height=35)
        self.consultar_tarefa.grid(row=3, column=0, padx=5, pady=5, columnspan=2)

    def adicionar_tarefa(self):
        nova_janela = ctk.CTk()
        interface_adc = AdicionarTarefa(nova_janela)
        interface_adc.iniciarInterface()

    def deletar_tarefa(self):
        nova_janela = ctk.CTk()
        interface_delet = DeletarTarefa(nova_janela)
        interface_delet.iniciarInterface()

    def atualizar_tarefa(self):
        nova_janela = ctk.CTk()
        interface_upd = AtualizarTarefa(nova_janela)
        interface_upd.iniciarInterface()

    def consultar_id(self):
        nova_janela = ctk.CTk()
        interface_id = ConsultarID(nova_janela)
        interface_id.iniciarInterface()

    def consultar_tarefa(self):
        nova_janela = ctk.CTk()
        interface_tarefa = ConsultarTarefa(nova_janela)
        interface_tarefa.iniciarInterface()

    def iniciarInterface(self):
        self.root.mainloop()

    # conexao = sqlite3.connect('listTasks.db')
    # c = conexao.cursor()
    # c.execute('''
    #             CREATE TABLE tb_tarefas (
    #         N_ID_TAREFA INTEGER PRIMARY KEY AUTOINCREMENT,
    #         T_TITULO_TAREFA TEXT,
    #         T_DATA_VENCIMENTO TEXT,
    #         T_PRIORIDADE TEXT
    #         )
    #         ''')
    # conexao.commit()
    # conexao.close()


if __name__ == '__main__':
    root = ctk.CTk()
    merc = ListaTarefas(root)
    merc.iniciarInterface()