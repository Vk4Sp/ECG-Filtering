import wfdb
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
from scipy.fft import fft, fftfreq

# Load ECG Data
record_name = "100"
database = "mitdb"
signal, fields = wfdb.rdsamp(record_name, pn_dir=database)
fs = fields["fs"]
t = np.arange(len(signal)) / fs
ecg_lead = signal[:, 0]

# Low-Pass Filter Parameters
cutoff = 50  # Hz
order = 6

# Apply Low-Pass Filter
b, a = butter(order, cutoff / (fs / 2), btype='low', analog=False)
filtered_signal = filtfilt(b, a, ecg_lead)

# Function for Zoomed Plot
def plot_zoomed_signal(signal, t, title, zoom_start, zoom_end, c):
    start_idx = int(zoom_start * fs)
    end_idx = int(zoom_end * fs)
    plt.figure(figsize=(12, 5))
    plt.plot(t[start_idx:end_idx], signal[start_idx:end_idx], label=title, color=c)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude (mV)")
    plt.title(f"{title} ({zoom_start}-{zoom_end} sec)")
    plt.legend()
    plt.grid()
    plt.show()

# FFT Analysis
n = len(ecg_lead)
freqs = fftfreq(n, 1/fs)
ecg_fft = np.abs(fft(ecg_lead))
filtered_fft = np.abs(fft(filtered_signal))

# Plot Frequency Spectrum
plt.figure(figsize=(12, 5))
plt.subplot(2,1,1)
plt.plot(freqs[:n // 2], ecg_fft[:n // 2], label="Original ECG Spectrum", color="b")
plt.ylabel("Magnitude")
plt.title("Frequency Spectrum Before & After Low-Pass Filtering (50 Hz)")
plt.legend()
plt.grid()
plt.ylim(0, 4000)

plt.subplot(2,1,2)
plt.plot(freqs[:n // 2], filtered_fft[:n // 2], label="Filtered ECG Spectrum (Low-Pass)", color="r")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.legend()
plt.grid()
plt.ylim(0, 4000)
plt.show()

# Full Signal Plot
plt.figure(figsize=(12, 5))
plt.plot(t, ecg_lead, label="Original ECG", alpha=0.6)
plt.plot(t, filtered_signal, label="Low-Pass Filtered ECG (50 Hz)", color="r")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude (mV)")
plt.title("ECG Before & After Low-Pass Filtering (50 Hz)")
plt.legend()
plt.grid()
plt.show()

# Zoomed-in Signal Plot
zoom_start = 0
zoom_end = 5
plot_zoomed_signal(ecg_lead, t, "Original ECG", zoom_start, zoom_end, "b")
plot_zoomed_signal(filtered_signal, t, "Low-Pass Filtered ECG", zoom_start, zoom_end, "r")
