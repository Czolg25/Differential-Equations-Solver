from repositories.TaskRepository import TasksRepository
from services.TaskService import TaskService


from tasks.ExampleTask import ExampleTask

if __name__ == '__main__':
    task_repository = TasksRepository()
    task_service = TaskService(task_repository)

    task_repository.add_task(ExampleTask())

    task_service.solve(10000)

