import customtkinter as ctk
from tkinter import messagebox
import sqlite3
from sqlite3 import Error

ctk.set_appearance_mode('light')

class AdicionarTarefa:
    def __init__(self, root):
        self.root = root
        self.root.title('Adicionar tarefa')
        self.root.geometry('450x400')
        self.root.resizable(False, False)

        self.label_inicio = ctk.CTkLabel(self.root, text='Adicionar Tarefas', font=('Arial', 25, 'bold'), text_color='#4169E1')
        self.label_inicio.grid(row=0, column=0, padx=10, pady=10)

        self.entry_tarefa = ctk.CTkEntry(self.root, placeholder_text='Título da tarefa...', width=400)
        self.entry_tarefa.grid(row=1, column=0, pady=10, padx=25)
        
        self.entry_data_venc = ctk.CTkEntry(self.root, placeholder_text='Data de vencimento da tarefa', width=200)
        self.entry_data_venc.grid(row=2, column=0)
        
        self.prioridade_label = ctk.CTkLabel(self.root, text='Defina a prioridade da sua tarefa:')
        self.prioridade_label.grid(row=3, column=0, padx=10, pady=10)
        self.prioridade = ctk.CTkEntry(self.root, placeholder_text='Baixa, média ou alta', width=200) # Aqui é onde eu quero o texto minusculo
        self.prioridade.grid(row=4, column=0)
        
        self.bt_adc = ctk.CTkButton(self.root, text='Adicionar', command=self.adc_tarefa)
        self.bt_adc.grid(row=7, column=0, padx=10, pady=10)

    def adc_tarefa(self):
        prioridade = self.prioridade.get().lower()

        # if prioridade != ['baixa','media','média','alta']:
        #     messagebox.showerror('Erro', 'Digite apenas Alta, média ou baixa')
        #     self.prioridade.delete(0, ctk.END)
        #     return

        if prioridade == 'baixa':
            prioridade = 'Baixa'
        elif prioridade == 'media' or self.prioridade == 'média':
            prioridade = 'Média'
        elif prioridade == 'alta':
            prioridade = 'Alta'
        
        
        conexao = sqlite3.connect('listTasks.db')
        c = conexao.cursor()
        c.execute(" INSERT INTO tb_tarefas (T_TITULO_TAREFA, T_DATA_VENCIMENTO, T_PRIORIDADE) VALUES (:T_TITULO_TAREFA, :T_DATA_VENCIMENTO, :T_PRIORIDADE)",
                {
                    'T_TITULO_TAREFA': self.entry_tarefa.get(),
                    'T_DATA_VENCIMENTO': self.entry_data_venc.get(),
                    'T_PRIORIDADE': prioridade
                })
        conexao.commit()
        conexao.close()

        self.entry_tarefa.delete(0, ctk.END)
        self.entry_data_venc.delete(0, ctk.END)
        self.prioridade.delete(0, ctk.END)
        self.entry_tarefa.focus_set()

    def iniciarInterface(self):
        self.root.mainloop()

if __name__ == '__main__':
    root = ctk.CTk()
    merc = AdicionarTarefa(root)
    merc.iniciarInterface()