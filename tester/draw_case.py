from interpolation1d import InderpolationInfo, Interpolator
from utils import HtmlLogger, get_signal_snippet, draw_ECG

import matplotlib.pyplot as plt


def draw_case_to_log(signal, program_ii, d_ii, best_ii):  # ii = interpolation info
    fig, ax = plt.subplots()
    draw_ECG(ax, signal)

    signal_len = len(signal)

    Interpolator(program_ii, signal_len=signal_len).draw(ax, color='blue', label='программа')
    Interpolator(d_ii, signal_len=signal_len).draw(ax, color='red', label='оцениваемый дескриптор')
    Interpolator(best_ii, signal_len=signal_len).draw(ax, color='green', label='лучший десриптор')
    return fig