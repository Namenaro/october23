import matplotlib.pyplot as plt
import numpy as np

def get_m(a_pred, a_real, old_a_pred=0):
    err_old = abs(a_real - old_a_pred)
    err_new = abs(a_real - a_pred)
    if err_old == 0:
        if err_new == 0:
            return 0 # совпало с тривиальным предсказанием и оказалось верным (обе ошибки нулевые)
        else:
            return 1 # тривиальное предсказание было идеальным, а мы испортили

    if err_old < err_new:  # обе ошибки не нулевые и новое предсказание ухудшило ситуацию
        return 1

    return err_new/err_old  # # обе ошибки не нулевые и новое предсказание улудшило ситуацию



if __name__ == '__main__':
    a_real = 2
    as_pred =  list(np.arange(-5, 7, 0.5))

    mus = list([get_m(a_real=a_real, a_pred=as_pred[i]) for i in range(len(as_pred))])

    fig, ax = plt.subplots()
    ax.plot(as_pred, mus, 'o')
    ax.vlines(x=a_real, ymin=0, ymax=1, colors='red', lw=2, alpha=0.5, label="a_real")
    ax.set_xlabel("a_pred")
    ax.set_ylabel("m (a_pred, a_real)")
    ax.legend()
    plt.show()

