from interpolation1d import Interpolator, InderpolationInfo
from utils import HtmlLogger
from pandas import DataFrame

class RObject:
    def __init__(self, signal, program_ii, d_ii, best_ii):
        self.signal = signal
        self.program_ii = program_ii
        self.d_ii = d_ii
        self.best_ii = best_ii

    def to_dataframe(self):
        data = {'col_1': [3], 'col_2':['a']}
        df = DataFrame.from_dict(data)
        log = HtmlLogger("rrrrrrrrrr")
        log.add_dataframe(df)
        return df


r = RObject(0,0,0,0)
r.to_dataframe()