from interpolation1d import Interpolator, InderpolationInfo
from utils import HtmlLogger
from .m_formula import get_m


from pandas import DataFrame
from copy import deepcopy

class RObject:
    def __init__(self, signal, program_ii, d_ii, best_ii):
        self.signal = signal
        self.program_ii = program_ii
        self.d_ii = d_ii
        self.best_ii = best_ii

        self.signal_mass = sum(list([abs(signal[i]) for i in range(len(self.signal))]))

        self.data = {}

        self.fill_best()
        self.fill_our()


    def to_log(self, log):
        names, ms = self.get_m_data()
        m_full = sum(ms)
        self.data["редакция нашего"] = m_full


        data_frame = self.to_dataframe()
        log.add_dataframe(data_frame)

    def to_dataframe(self):
        temp = {}
        for name, val in self.data.items():
            temp[name]=[val]

        df = DataFrame.from_dict(temp)
        return df

    def get_m_data(self):
        m_getter = StepwiseRedactions(program_ii=self.program_ii, d_ii=self.d_ii)
        names, ms = m_getter.get_points_ms()
        return names, ms

    def fill_best(self):
        best = Interpolator(self.best_ii, signal_len=len(self.signal)).get_interpolation()
        err = sum(list([abs(self.signal[i] - best[i]) for i in range(len(self.signal))]))
        self.data['выигрыш ошибки лучшего'] = (self.signal_mass - err)/self.signal_mass
        self.data['редакция лучшего'] = len(self.best_ii.order)*2


    def fill_our(self):
        interp = Interpolator(self.d_ii, signal_len=len(self.signal)).get_interpolation()
        err = sum(list([abs(self.signal[i] - interp[i]) for i in range(len(self.signal))]))
        self.data['выигрыш ошибки нашего'] = (self.signal_mass - err) / self.signal_mass



class PointRedactionData:
    def __init__(self, u_real, u_predicted, v_real, v_predicted):
        self.u_real = u_real
        self.u_predicted = u_predicted
        self.v_real = v_real
        self.v_predicted = v_predicted

    def get_m_u(self):
        return get_m(a_pred=self.u_predicted, a_real=self.u_real, old_a_pred=0)

    def get_m_v(self):
        return get_m(a_pred=self.v_predicted, a_real=self.v_real, old_a_pred=0)

    def get_point_m(self):
        mv = self.get_m_v()
        mu = self.get_m_u()
        return mv + mu


class  StepwiseRedactions:
    def __init__(self, program_ii, d_ii):
        self.program_ii = program_ii
        self.d_ii = d_ii

        self.points_data ={}  # name:PointData
        self._fill_points_data()

    def _fill_points_data(self):
        for name in self.program_ii.order:
            u_real = self.d_ii.get_u_by_name(name)
            v_real = self.d_ii.get_v_by_name(name)

            u_predicted = self.program_ii.get_u_by_name(name)
            v_predicted = self.program_ii.get_v_by_name(name)

            self.points_data[name] = PointRedactionData(u_real=u_real, u_predicted=u_predicted, v_real=v_real, v_predicted=v_predicted  )


    def get_points_ms(self):
        points_names = []
        points_ms = []
        for name, point_data in self.points_data.items():
            points_names.append(name)
            points_ms.append(point_data.get_point_m())

        return points_names, points_ms









