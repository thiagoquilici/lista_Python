# lista vazia
lista_de_tarefas = []

# laço de repetição
while True:
# o usuário insere a nova tarefa na lista    
    nova_tarefa = input('Informe a nova tarefa ou deixe vazio para encerrar e exibir a lista: ')

    # verifica se o usuário inseriu nova tarefa
    if nova_tarefa != '':

    # nova tarefa é inserida na lista
        lista_de_tarefas.append(nova_tarefa)
        continue
    else:
        break
   
# exibe na tela a lista
for tarefa in lista_de_tarefas:
        print(tarefa)
   