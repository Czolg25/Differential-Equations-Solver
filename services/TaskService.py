import numpy

from repositories.TaskRepository import TasksRepository
from objects.space.Space import Space
from objects.TaskData import TaskData
from plots.ChoosePlot import ChoosePlot
from objects.plot.PlotData import PlotData
from objects.functions.error.AbsError import AbsError
from objects.functions.error.PercentError import PercentError


class TaskService:
    def __init__(self, task_repository: TasksRepository):
        self.__task_repository = task_repository

    def solve(self, epochs: int, multiply_space: int = 10):
        for task in self.__task_repository.get_tasks():
            self.__run_task(task, epochs, multiply_space)

    def __run_task(self, task: TaskData, epoch: int, multiply_space: int):
        equation = task.get_equation()
        plot_title = f"{task.get_name()} epoches: {epoch}"

        ai_solution = equation.get_solution_function()
        ai_solution.solve(epoch)

        test_space = task.get_space_range().split(multiply_space)
        y = ai_solution.calculate_as_numpy(test_space)
        choose_plot = ChoosePlot(test_space, y,PlotData(f"Ai solution {plot_title}"))
        choose_plot.choose().plot()

        exact_solution = equation.get_exact_solution()
        if exact_solution is not None:

            choose_plot = ChoosePlot(test_space, exact_solution.calculate_as_numpy(test_space),PlotData(f"Exact solution {plot_title}"))
            choose_plot.choose().plot()

            abs_error_function = AbsError(ai_solution, exact_solution)

            choose_plot = ChoosePlot(test_space, abs_error_function.calculate(test_space), PlotData(f"Absolute error {plot_title}",["x","Error"]))
            choose_plot.choose().plot()

            percent_error_function = PercentError(ai_solution, exact_solution)
            percent_error = percent_error_function.calculate(test_space)
            if percent_error is not None:
                choose_plot = ChoosePlot(test_space, percent_error, PlotData(f"Error % {plot_title}",["x","Error (%)"]))
                choose_plot.choose().plot()

        loss_array = ai_solution.get_loss_array()
        if loss_array is not None:
            space = Space([numpy.linspace(1,epoch, epoch)])
            choose_plot = ChoosePlot(space, loss_array, PlotData("Convergence", ["epoch","loss"]))
            choose_plot.choose().plot()

            threshold = (loss_array[0] - loss_array[len(loss_array) - 1]) / 10
            intervals = self.__find_small_change_intervals(loss_array,threshold)
            while threshold > loss_array[len(loss_array) - 1]:
                for interval in intervals:
                    start = interval[0]
                    end = epoch
                    if len(interval) >= 2:
                        end = interval[1]

                    loss_sub_array = loss_array[start:end]

                    space = Space([numpy.linspace(start, end,end - start)])
                    choose_plot = ChoosePlot(space, loss_sub_array, PlotData("Convergence", ["epoch", "loss"]))
                    choose_plot.choose().plot()

                threshold = threshold/10
                intervals = self.__find_small_change_intervals(loss_array, threshold)


    def __find_small_change_intervals(self, array, change_threshold):
        intervals = []

        i = 0
        while i < len(array) - 1:
            start = i
            end = len(array)-1

            if start != 0 and abs(array[start] - array[end]) <= change_threshold:

                if end - start >= 4:
                    intervals.append((start, end))
                    return intervals

            i += 1

        return intervals

