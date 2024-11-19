from objects.tasks.TaskEquationData import TaskEquationData
from repositories.TaskEquationRepository import TaskEquationRepository
from functions.SolutionFuncton import SolutionFunction
from objects.Variables import Variables
from plots.Plot import Plot

class EquationService:
    def __init__(self,repository: TaskEquationRepository):
        self.repository = repository
        self.learning_rate = 0.1

    def run(self,epochs:int):
        tasks = self.repository.get_tasks()
        for task in tasks:
            self._run_task(epochs,task)

    def _run_task(self,epochs:int,taskEquationData:TaskEquationData):
        space = taskEquationData.get_space()

        solution = SolutionFunction(space,taskEquationData.get_loss_function(),self.learning_rate)
        solution.ai_solver.solve(epochs)

        variables = Variables(space.split())

        plots = []
        plots.append(Plot(variables,taskEquationData.get_labels(),taskEquationData.get_function_name()+f" - ai epochs: {epochs}",solution))
        plots.append(Plot(variables,taskEquationData.get_labels(),taskEquationData.get_function_name()+f" error epochs: {epochs}",taskEquationData.
                          get_error_function(solution)))
        plots.append(
            Plot(variables, taskEquationData.get_labels(), taskEquationData.get_function_name()+f" error(%) epochs: {epochs}", taskEquationData.
                 get_error_abs_function(solution)))

        for plot in plots:
            plot.choose().show()

