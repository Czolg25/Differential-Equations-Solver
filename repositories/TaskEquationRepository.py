from objects.tasks.TaskEquationData import TaskEquationData

class TaskEquationRepository:
    def __init__(self):
        self.tasks = []

    def add(self, task: TaskEquationData):
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks