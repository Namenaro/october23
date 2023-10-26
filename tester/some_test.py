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




if __name__ == '__main__':
    log = HtmlLogger("TEST_FOR_R")


    log.add_text("Пример ситуации")


    signal = get_signal_snippet(lead_name='i', start_coord=23, end_coord=435)

    # заполняем программу
    programA = InderpolationInfo()
    u1 = 90
    programA.add(u=u1, v=10, name='first')
    u12 = 10
    programA.add(u=u12, v=200, name='second', parent_name='first', is_linked=True)

    # заполняем дестриптор (рез-т распознавания этой программы на этом сигнале)
    dA = InderpolationInfo()
    u1 = 90
    dA.add(u=u1, v=signal[u1], name='first')
    u12 = 102
    dA.add(u=u12, v=signal[u1 + u12], name='second', parent_name='first', is_linked=True)

    # заполняем наилучшую интерпроляцию (лучший интерполятор по такому же кол-ву точек)
    best = InderpolationInfo()
    u1 = 171
    best.add(u=u1, v=signal[u1], name='first')
    u12 = 11
    best.add(u=u12, v=signal[u1+u12], name='second', parent_name='first', is_linked=True)


    # отрисовываем этот тестовый случай
    fig = draw_case_to_log(signal, program_ii=programA, d_ii=dA, best_ii=best)

    plt.show()
    log.add_fig(fig)




