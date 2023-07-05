import mysql.connector
from tkinter import *


def crud_read():
    comando = f'SELECT * FROM bdyoutube.vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall()  # ler o banco de dados

    resultado_formatado = ""
    for linha in resultado:
        id = linha[0]
        nome_produto = linha[1]
        valor = linha[2]

        linha_formatada = f"ID: {id} | Nome: {nome_produto} | Valor: R${valor}"
        resultado_formatado += linha_formatada + "\n"

    texto_pesquisa['text'] = resultado_formatado

def crud_create():
    nome = entrada.get().lower()
    preco = entrada2.get().lower()

    comando = f'INSERT INTO vendas (nome , preco) VALUES ("{nome}", {preco})'
    cursor.execute(comando)
    conexao.commit() # quando o banco de dados é editado Create Update Delete
    

def crud_update():
    nome = entrada3.get().lower()
    valor = entrada4.get()
    comando = f'UPDATE vendas SET preco = {valor} WHERE nome = "{nome}"'
    cursor.execute(comando)
    conexao.commit()

def crud_delete():
    nome = entrada5.get().lower()
    comando = f'DELETE FROM vendas  WHERE nome = "{nome}"'
    cursor.execute(comando)
    conexao.commit()


conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='151096ara',
    database='bdyoutube',
)
cursor = conexao.cursor()

janela = Tk()
janela.title("Crud-Tkinter")

grupo2 = Frame(janela)
grupo2.grid(column=0, row=0, padx=10, pady=10)

texto_orientacao = Label(grupo2, text="Clique no Botão Para exibir as informações")
texto_orientacao.grid(column=0, row=0)

botao = Button(grupo2, text="Listar tudo do Banco de Dados", command=crud_read)
botao.grid(column=0, row=1, padx=10, pady=10)

texto_pesquisa = Label(grupo2, text="")
texto_pesquisa.grid(column=0, row=2, padx=10, pady=10)

grupo1 = Frame(janela)
grupo1.grid(column=0, row=1, padx=10, pady=10)

texto_ajuda = Label(grupo1, text="Nome de um Produto")
texto_ajuda.grid(column=0, row=0)

entrada = Entry(grupo1)
entrada.grid(column=1, row=0, padx=10, pady=10)

texto_ajuda2 = Label(grupo1, text="Preço do Produto (Por Favor digite um número inteiro)")
texto_ajuda2.grid(column=0, row=1)

entrada2 = Entry(grupo1)
entrada2.grid(column=1, row=1, padx=10, pady=10)

botao2 = Button(grupo1, text="Criar no Banco de Dados", command=crud_create)
botao2.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

grupo3 = Frame(janela)
grupo3.grid(column=0, row=3, padx=10, pady=10)

texto_ajuda3 = Label(grupo3, text="Nome do Produto que vai ser Alterado")
texto_ajuda3.grid(column=0, row=0)

entrada3 = Entry(grupo3)
entrada3.grid(column=1, row=0, padx=10, pady=10)

texto_ajuda4 = Label(grupo3, text="Novo Preço (Por Favor digite um número inteiro)")
texto_ajuda4.grid(column=0, row=2)

entrada4 = Entry(grupo3)
entrada4.grid(column=1, row=2, padx=10, pady=10)

botao3 = Button(grupo3, text="Alterar no Banco de Dados", command=crud_update)
botao3.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

grupo4 = Frame(janela)
grupo4.grid(column=0, row=13, padx=10, pady=10)

texto_ajuda5 = Label(grupo4, text="Nome do Produto que vai ser Excluído")
texto_ajuda5.grid(column=0, row=0)

entrada5 = Entry(grupo4)
entrada5.grid(column=1, row=0, padx=10, pady=10)

botao4 = Button(grupo4, text="Deletar do Banco de Dados", command=crud_delete)
botao4.grid(column=0, row=2,columnspan=2, padx=10, pady=10)

janela.mainloop()

conexao.close()
cursor.close()




#CRUD

#Create

# nome = 'chocolate'
# preco = 15

# comando = f'INSERT INTO vendas (nome , preco) VALUES ("{nome}", {preco})'
# cursor.execute(comando)
# conexao.commit() # quando o banco de dados é editado Create Update Delete

#Read
# comando = f'SELECT * FROM bdyoutube.vendas'
# cursor.execute(comando)
# resultado = cursor.fetchall() # ler o banco de dados
# print(f'{resultado}')

#Update

# nome = "todynho"
# valor = 6
# comando = f'UPDATE vendas SET preco = {valor} WHERE nome = "{nome}"'
# cursor.execute(comando)
# conexao.commit()

#Delete

# nome = "todynho"
# comando = f'DELETE FROM vendas  WHERE nome = "{nome}"'
# cursor.execute(comando)
# conexao.commit()