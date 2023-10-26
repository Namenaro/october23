from interpolation1d import Interpolator, InderpolationInfo

import matplotlib.pyplot as plt

if __name__ == '__main__':
    interpolation_info = InderpolationInfo()

    interpolation_info.add(u=14, v=6, name='first', parent_name=None)
    interpolation_info.add(u=4, v=12, name='second', parent_name='first', is_linked=True)
    interpolation_info.add(u=-5, v=14, name='third', parent_name='first', is_linked=True)
    interpolation_info.add(u=15, v=18, name='fourth', parent_name='second', is_linked=False)


    fig, ax = plt.subplots()
    Interpolator(interpolation_info, signal_len=70).draw(ax, color='red')
    plt.show()

