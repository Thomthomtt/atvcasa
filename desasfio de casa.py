resp=0
lista_todas_tarefas=[]
while resp!=4:
    resp=int(input("1. listar tarefas\n"
               "2. lista adicionar tarefas\n"
               "3. excluir tarefas\n"
               "4. sair\n"
               "O que deseja fazer? "))
    if resp==1:
        nomedatarefa=input("Digite o nome da tarefa")
        lista_todas_tarefas.append(nomedatarefa)
    elif resp==2:
        print(f"Aqui estão suas tarefas:\n{lista_todas_tarefas}")
    elif resp==3:
        for i in range(len(lista_todas_tarefas)):
            print(f"Qual item deseja exluir na lista de tarefas? {lista_todas_tarefas}")
            excluir = int(input("Qual tarefa deseja exluir? "))
            excluido=lista_todas_tarefas.pop(excluir)
            break
    if resp==4:
        break


