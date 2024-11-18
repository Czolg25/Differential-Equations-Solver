from repositories.TaskEquationRepository import TaskEquationRepository
from services.EquationService import EquationService
from examples.tasks.SimpleEquation import SimpleEquation

if __name__ == '__main__':
    task_repository = TaskEquationRepository()
    equation_service = EquationService(task_repository)

    task_repository.add(SimpleEquation())

    equation_service.run(100)
