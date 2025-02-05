from repositories.TaskRepository import TasksRepository
from services.TaskService import TaskService

from tasks.ai.article.examples.ArticleExamplesImport import *

if __name__ == '__main__':
    task_repository = TasksRepository()
    task_service = TaskService(task_repository)

    task_repository.add_task(FirstProblemSimpleTask())
    task_repository.add_task(FirstProblemLossTask())
    task_repository.add_task(SecondProblemSimpleTask())
    task_repository.add_task(SecondProblemLossTask())
    task_repository.add_task(ThirdProblemSimpleTask())

    task_service.solve(10000)

