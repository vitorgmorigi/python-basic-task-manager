from manager import Manager
from task import Task
from typing import List

def test_add_task_to_manager():
    manager = Manager()

    task = Task("Estudar", "pendente")
    manager.addTaskToList(task)
    assert len(manager.tasks) == 1


def test_list_pending_tasks(): 
    manager = Manager()

    task1 = Task("Estudar", "pendente")
    task2 = Task("Comer", "concluida")
    manager.addTaskToList(task1)
    manager.addTaskToList(task2)
    result: List[Task] = manager.listPendingTasks()

    assert len(result) == 1
    assert result[0].name == "Estudar"

def test_list_all_tasks():
    manager = Manager()

    task1 = Task("Estudar", "pendente")
    task2 = Task("Comer", "concluida")
    manager.addTaskToList(task1)
    manager.addTaskToList(task2)
    result: List[Task] = manager.listAllTasks()

    assert len(result) == 2
    assert result[0].name == "Estudar"
    assert result[1].name == "Comer"

def test_remove_task():
    manager = Manager()

    task1 = Task("Estudar", "pendente")
    task2 = Task("Comer", "concluida")
    manager.addTaskToList(task1)
    manager.addTaskToList(task2)
    manager.removeTaskFromList("Comer")

    assert len(manager.tasks) == 1
    assert manager.tasks[0].name == "Estudar"