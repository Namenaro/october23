from interpolation1d import InderpolationInfo, Interpolator
from utils import HtmlLogger, get_signal_snippet, draw_ECG

from draw_case import draw_case_to_log

import matplotlib.pyplot as plt


def good_case(log, signal):
    log.add_text("Т-волна и хорошая программа")
    # заполняем программу
    programA = InderpolationInfo()
    u1 = 80
    programA.add(u=u1, v=210, name='1')
    u12 = 40
    programA.add(u=u12, v=0, name='2', parent_name='1', is_linked=True)

    u13 = -50
    programA.add(u=u13, v=0, name='3', parent_name='1', is_linked=True)

    # заполняем дестриптор (рез-т распознавания этой программы на этом сигнале)
    dA = InderpolationInfo()
    u1 = 106
    dA.add(u=u1, v=signal[u1], name='1')
    u12 = 35
    dA.add(u=u12, v=signal[u1 + u12], name='2', parent_name='1', is_linked=True)
    u13 = -55
    dA.add(u=u13, v=0, name='3', parent_name='1', is_linked=True)

    # заполняем наилучшую интерпроляцию (лучший интерполятор по такому же кол-ву точек)
    best = InderpolationInfo()
    u1 = 105
    best.add(u=u1, v=signal[u1], name='1')
    u12 = 35
    best.add(u=u12, v=signal[u1 + u12], name='2', parent_name='1', is_linked=True)
    u13 = -48
    best.add(u=u13, v=0, name='3', parent_name='1', is_linked=True)

    # отрисовываем этот тестовый случай
    fig = draw_case_to_log(signal, program_ii=programA, d_ii=dA, best_ii=best)
    return fig


def bad_case1(log, signal):
    log.add_text("Т-волна и плохая программа")
    # заполняем программу
    programA = InderpolationInfo()
    u1 = 80
    programA.add(u=u1, v=-5, name='1')
    u12 = 40
    programA.add(u=u12, v=0, name='2', parent_name='1', is_linked=True)

    u13 = -50
    programA.add(u=u13, v=0, name='3', parent_name='1', is_linked=True)

    # заполняем дестриптор (рез-т распознавания этой программы на этом сигнале)
    dA = InderpolationInfo()
    u1 = 106
    dA.add(u=u1, v=signal[u1], name='1')
    u12 = 35
    dA.add(u=u12, v=signal[u1 + u12], name='2', parent_name='1', is_linked=True)
    u13 = -55
    dA.add(u=u13, v=0, name='3', parent_name='1', is_linked=True)

    # заполняем наилучшую интерпроляцию (лучший интерполятор по такому же кол-ву точек)
    best = InderpolationInfo()
    u1 = 105
    best.add(u=u1, v=signal[u1], name='1')
    u12 = 35
    best.add(u=u12, v=signal[u1 + u12], name='2', parent_name='1', is_linked=True)
    u13 = -48
    best.add(u=u13, v=0, name='3', parent_name='1', is_linked=True)

    # отрисовываем этот тестовый случай
    fig = draw_case_to_log(signal, program_ii=programA, d_ii=dA, best_ii=best)
    return fig


def bad_case2(log, signal):
    log.add_text("Т-волна и плохая программа")
    # заполняем программу
    programA = InderpolationInfo()
    u1 = 80
    programA.add(u=u1, v=-5, name='1')
    u12 = 40
    programA.add(u=u12, v=0, name='2', parent_name='1', is_linked=True)

    u13 = -50
    programA.add(u=u13, v=0, name='3', parent_name='1', is_linked=True)

    # заполняем дестриптор (рез-т распознавания этой программы на этом сигнале)
    dA = InderpolationInfo()
    u1 = 80
    dA.add(u=u1, v=signal[u1], name='1')
    u12 = 35
    dA.add(u=u12, v=signal[u1 + u12], name='2', parent_name='1', is_linked=True)
    u13 = -55
    dA.add(u=u13, v=0, name='3', parent_name='1', is_linked=True)

    # заполняем наилучшую интерпроляцию (лучший интерполятор по такому же кол-ву точек)
    best = InderpolationInfo()
    u1 = 105
    best.add(u=u1, v=signal[u1], name='1')
    u12 = 35
    best.add(u=u12, v=signal[u1 + u12], name='2', parent_name='1', is_linked=True)
    u13 = -48
    best.add(u=u13, v=0, name='3', parent_name='1', is_linked=True)

    # отрисовываем этот тестовый случай
    fig = draw_case_to_log(signal, program_ii=programA, d_ii=dA, best_ii=best)
    return fig

if __name__ == '__main__':
    log = HtmlLogger("TEST_T")
    signal = get_signal_snippet(lead_name='i', start_coord=243, end_coord=435)


    fig = good_case(log, signal)
    plt.show()
    log.add_fig(fig)

    fig = bad_case1(log, signal)
    plt.show()
    log.add_fig(fig)

    fig = bad_case2(log, signal)
    plt.show()
    log.add_fig(fig)

