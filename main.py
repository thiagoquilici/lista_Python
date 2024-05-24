# importar biblioteca
import os

# lista vazia
lista_de_tarefas = []

# laço de repetição
while True:
# o usuário insere a nova tarefa na lista    
    nova_tarefa = input('Insira a nova tarefa ou Enter para encerrar e exibir a lista: ')

    # verifica se o usuário inseriu nova tarefa
    if nova_tarefa != '':

    # nova tarefa é inserida na lista
        lista_de_tarefas.append(nova_tarefa)
        continue
    else:
        break

# limpa console
os.system('cls')

# exibe na tela a lista
print(f'{'-'*30} LISTA DE TAREFAS {'-'*30}')   

for tarefa in lista_de_tarefas:
        print(tarefa)
   