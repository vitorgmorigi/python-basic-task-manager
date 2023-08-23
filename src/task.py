class Task:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def setStatus(self, newStatus):
        self.status = newStatus

    def listTask(self):
        print("Tarefa: ", self.name, "\t", "Status: ", self.status)