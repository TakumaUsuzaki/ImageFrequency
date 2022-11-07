import numpy as np
import pandas as pd
from scipy import signal


def FFT_image_max(li):
    N = len(li)
    if N > 0:
        F = np.fft.fft(li)
        freq = np.fft.fftfreq(N, d=1.0)[1:int(N/2)]
        Amp = np.abs(F/(N/2))[1:int(N/2)]
        maxId = signal.argrelmax(Amp)[0]
        if len(maxId) > 0:

            Amp_argrelmax = Amp[maxId]
            max_index_freq = np.argmax(Amp_argrelmax)
            freq_max = freq[1:int(N/2)][maxId[max_index_freq]]

            #print("max frequency = {}".format(freq_max))
            # Plot figure (If needed)
            """
            fig, ax = plt.subplots()
            ax.plot(freq, Amp)
            ax.set_xlabel("Freqency [Hz]")
            ax.set_ylabel("Amplitude")
            ax.grid()
            plt.show(block=False)
            plt.pause(0.3) # Not pythonic
            plt.close(fig)
            """
            return (freq_max)


def FFT_image(li, n):
    N = len(li)
    if N > 0:
        F = np.fft.fft(li)
        Amp = np.abs(F/(N/2))[1:int(N/2)]
        maxId = signal.argrelmax(Amp)[0]
        freq = np.fft.fftfreq(N, d=1.0)[1:int(N/2)][maxId]
        if len(maxId) >= n:
            df = pd.DataFrame({'maxId': maxId, 'freq': freq})
            df_s = df.sort_values('freq')
            return (df_s.iloc[n-1, 1])
