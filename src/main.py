from manager import Manager
from task import Task

def showMenu():
    print("Menu:")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas Pendentes")
    print("3. Listar todas as tarefas")
    print("4. Marcar Tarefa como Concluída")
    print("5. Remover Tarefa")
    print("6. Sair")


def run():
    manager = Manager()
    while 1:
        showMenu()
        selectedInput = int(input("Digite a opção desejada: "))

        match selectedInput:
            case 1:
                taskName = input("Digite o nome da tarefa: ")
                task = Task(taskName, "pendente")
                manager.addTaskToList(task)
            case 2:
                manager.listPendingTasks()
            case 3:
                manager.listAllTasks()
            case 4:
                updatedTask = input("Digite o nome da tarefa concluída: ")
                manager.markTaskAsDone(updatedTask)
            case 5:
                removedTask = input("Digite o nome da tarefa removida: ")
                manager.removeTaskFromList(removedTask)
            case _:
                return 0
        
run()
