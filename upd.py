import customtkinter as ctk
import sqlite3
from sqlite3 import Error

ctk.set_appearance_mode('light')

class AtualizarTarefa:
    def __init__(self, root):
        self.root = root
        self.root.title('Atualizar tarefa')
        self.root.geometry('400x400')

        self.label = ctk.CTkLabel(self.root, text='Atualizar tarefa', font=('Arial', 25, 'bold'), text_color='#4169E1')
        self.label.pack(pady=20)

        self.id_att = ctk.CTkEntry(self.root, placeholder_text='ID da tarefa a ser atualizada')
        self.id_att.pack(pady=10)

        self.conf = ctk.CTkButton(self.root, text='Confirmar', command=self.carregarTarefa)
        self.conf.pack(pady=10)

        # Botão para salvar as alterações
        self.salvar = ctk.CTkButton(self.root, text='Salvar', command=self.salvarAlteracoes)
        self.salvar.pack(pady=5)
        
        # Variáveis para armazenar os novos valores
        self.titulo_novo = None
        self.data_nova = None
        self.prioridade_nova = None

    def ConexaoBanco(self):
        con = None
        try:
            con = sqlite3.connect('listTasks.db')
        except Error as ex:
            print(ex)
        return con

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

    def criarCampoEntrada(self, placeholder_text, width=300):
        entrada = ctk.CTkEntry(self.root, placeholder_text=placeholder_text, width=width)
        entrada.pack(pady=10)
        return entrada

    def carregarTarefa(self):
        id_tarefa = self.id_att.get()
        conexao = self.ConexaoBanco()
        resultado = self.consultar(conexao, id_tarefa)

        if resultado:
            titulo_atual = resultado[0][1]
            data_atual = resultado[0][2]
            prioridade_atual = resultado[0][3]

            # Cria campos de entrada para os novos valores e preenche com os valores atuais
            self.titulo_novo = self.criarCampoEntrada('Título da tarefa...')
            self.data_nova = self.criarCampoEntrada('Data de vencimento da tarefa')
            self.prioridade_nova = self.criarCampoEntrada('Nível de prioridade da tarefa')

            self.titulo_novo.insert(0, titulo_atual)
            self.data_nova.insert(0, data_atual)
            self.prioridade_nova.insert(0, prioridade_atual)

    def salvarAlteracoes(self):
        id_tarefa = self.id_att.get()
        titulo_novo = self.titulo_novo.get()
        data_nova = self.data_nova.get()
        prioridade_nova = self.prioridade_nova.get()

        if id_tarefa and titulo_novo and data_nova and prioridade_nova:
            conexao = self.ConexaoBanco()
            self.query(conexao, "UPDATE tb_tarefas SET T_TITULO_TAREFA=?, T_DATA_VENCIMENTO=?, T_PRIORIDADE=? WHERE N_ID_TAREFA = ?", (titulo_novo, data_nova, prioridade_nova, id_tarefa))
            
            # Limpa os campos de entrada após a atualização
            self.titulo_novo.delete(0, ctk.END)
            self.data_nova.delete(0, ctk.END)
            self.prioridade_nova.delete(0, ctk.END)

            # Tira os campos de entrada da interface após a atualização
            self.titulo_novo.forget()
            self.data_nova.forget()
            self.prioridade_nova.forget()

    def iniciarInterface(self):
        self.root.mainloop()

if __name__ == '__main__':
    root = ctk.CTk()
    merc = AtualizarTarefa(root)
    merc.iniciarInterface()
