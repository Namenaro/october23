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
        err_before = self.get_err_before()

        data = {'ошибка до': [err_before], 'col_2':['a']}
        df = DataFrame.from_dict(data)
        return df

    def get_err_before(self):
        err = sum(list([abs(v) for v in self.signal]))
        return err





r = RObject([6,6,-6],0,0,0)
df = r.to_dataframe()

log = HtmlLogger("rrrrrrrrrr")
log.add_dataframe(df)
