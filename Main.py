from objects.Range import Range
from objects.Space import Space
from plots.ChoosePlot import ChoosePlot

if __name__ == '__main__':
    s = Space(2,Range(1,2),Range(0,1))
    s2 = Space(2,Range(1,2))

    c = ChoosePlot(s.get_axis_as_numpy(0),s.get_axis_as_numpy(0))
    c.choose().plot()
    print("k")
    c1 = ChoosePlot([1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10.5])
    c1.choose()