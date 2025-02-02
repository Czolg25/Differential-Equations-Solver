from repositories.TaskRepository import TasksRepository
from objects.TaskData import TaskData
from plots.ChoosePlot import ChoosePlot
from objects.functions.error.AbsError import AbsError
from objects.functions.error.PercentError import PercentError

class TaskService:
    def __init__(self, task_repository: TasksRepository):
        self.__task_repository = task_repository

    def solve(self,epochs: int,multiply_space: int = 10):
        for task in self.__task_repository.get_tasks():
            self.__run_task(task,epochs,multiply_space)

    def __run_task(self, task:TaskData, epoch:int, multiply_space: int):
        equation = task.get_equation()

        ai_solution = equation.get_solution_function()
        ai_solution.solve(epoch)

        test_space = task.get_space_range().split(multiply_space)
        y = ai_solution.calculate_as_numpy(test_space)
        choose_plot = ChoosePlot(test_space, y)
        choose_plot.choose().plot()

        exact_solution = equation.get_exact_solution()
        if exact_solution is not None:

            choose_plot = ChoosePlot(test_space, exact_solution.calculate_as_numpy(test_space))
            choose_plot.choose().plot()

            abs_error_function = AbsError(ai_solution, exact_solution)

            choose_plot = ChoosePlot(test_space, abs_error_function.calculate(test_space))
            choose_plot.choose().plot()

            #percent_error_function = PercentError(ai_solution, exact_solution)
            #choose_plot = ChoosePlot(test_space, percent_error_function.calculate(test_space))
            #choose_plot.choose().plot()