# libraries
from scipy.io import wavfile 
from scipy import signal 
import matplotlib.pyplot as plt
import librosa 
import numpy as np 
import pandas as pd 
import os	

# to make spectrogram image
def log_spectrogram(audio, sample_rate, window_size=10, step_size=10, eps=1e-10):
	nperseg = int(round(window_size * sample_rate / 1e3))
	noverlap = int(round(step_size * sample_rate / 1e3))
	_, _, spec = signal.spectrogram(audio, fs=sample_rate, window='hann', nperseg=nperseg, noverlap=noverlap, detrend=False)
	return np.log(spec.T.astype(np.float32) + eps)

# read file
sample_rate, audio = wavfile.read(source_wav_path + sub_dirs[i] + "/" + files[j])

# get spectrogram
spectrogram = (log_spectrogram(audio, sample_rate, 10, 0)).T

# save matplotlib figure
plt.tight_layout()
plt.axis("off")
plt.imshow(spectrogram)
plt.savefig(target_spec_path + sub_dirs[i] + "/" + files[j].split(".")[0] + ".png", bbox_inches='tight', pad_inches=0)
plt.close()
plt.clf()