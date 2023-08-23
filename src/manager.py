from typing import List
from task import Task

class Manager:
    def __init__(self):
        self.tasks: List[Task] = []

    def __findTaskByName(self, name: str):
        for task in self.tasks:
            if task.name == name:
                return task
        return None

    def __listTasks(self, tasks: List[Task]):
        result: List[Task] = []
        for task in tasks:
            task.listTask()
            result.append(task)

        return result

    def addTaskToList(self, task: Task):
        self.tasks.append(task)

    def removeTaskFromList(self, name: str):
        task = self.__findTaskByName(name)
        if task != None:
            self.tasks.remove(task)
        else:
            print("Não foi encontrada nenhuma tarefa com esse nome")

    def listPendingTasks(self):
        pendingTasks: List[Task] = filter(lambda task: task.status == "pendente", self.tasks)
        return self.__listTasks(pendingTasks)

    def listAllTasks(self):
        return self.__listTasks(self.tasks)

    def markTaskAsDone(self, name: str):
        task = self.__findTaskByName(name)
        if task != None:
            task.setStatus("concluida")
        else:
            print("Não foi encontrada nenhuma tarefa com esse nome")

