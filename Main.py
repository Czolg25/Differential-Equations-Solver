from objects.Range import Range
from objects.space.SpaceRanges import SpaceRanges
from plots.ChoosePlot import ChoosePlot

if __name__ == '__main__':
    s = SpaceRanges(2,Range(1,2),Range(0,1)).split()
    c = ChoosePlot(s)
    c.choose().plot()