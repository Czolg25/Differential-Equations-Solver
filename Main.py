from repositories.TaskEquationRepository import TaskEquationRepository
from services.EquationService import EquationService
from examples.tasks.Second import Second
from examples.tasks.SimpleEquation import SimpleEquation
from examples.tasks.Part import Part


if __name__ == '__main__':
    task_repository = TaskEquationRepository()
    equation_service = EquationService(task_repository)

    task_repository.add(SimpleEquation())
    task_repository.add(Second())

    equation_service.run(50000)
