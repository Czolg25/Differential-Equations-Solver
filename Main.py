from repositories.TaskRepository import TasksRepository
from services.TaskService import TaskService


from tasks.ExampleTask import ExampleTask
from tasks.ApproximationExampleTask import ApproximationExampleTask
from tasks.Example2Task import Example2Task

if __name__ == '__main__':
    task_repository = TasksRepository()
    task_service = TaskService(task_repository)

    task_repository.add_task(ApproximationExampleTask())

    task_service.solve(5000)

