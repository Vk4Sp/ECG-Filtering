import wfdb
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, iirnotch
from scipy.fft import fft, fftfreq

# Load ECG Data
record_name = "100"
database = "mitdb"
signal, fields = wfdb.rdsamp(record_name, pn_dir=database)
fs = fields["fs"]  # Sampling frequency
t = np.arange(len(signal)) / fs  # Time axis
ecg_lead = signal[:, 0]  # Select first ECG lead (MLII)

# Adding Artificial Noise for Testing
ecg_lead += 0.5 * np.sin(2 * np.pi * 0.2 * t)  # Baseline drift (0.2 Hz)
ecg_lead += 0.05 * np.sin(2 * np.pi * 50 * t)  # Powerline noise (50 Hz)

# Filtering Parameters
notch_freq = 50  # Hz
notch_Q = 40  # Quality factor
low_cutoff = 0.5  # Lower cutoff for band-pass filter (Hz)
high_cutoff = 40  # Upper cutoff for band-pass filter (Hz)
order = 4  # Filter order

# Apply Notch Filter (50 Hz)
b_notch, a_notch = iirnotch(notch_freq, notch_Q, fs)
notch_filtered = filtfilt(b_notch, a_notch, ecg_lead)

# Apply Band-Pass Filter (0.5 - 40 Hz)
b_bandpass, a_bandpass = butter(order, [low_cutoff / (fs / 2), high_cutoff / (fs / 2)], btype="band", analog=False)
bandpass_filtered = filtfilt(b_bandpass, a_bandpass, notch_filtered)

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
notch_fft = np.abs(fft(notch_filtered))
bandpass_fft = np.abs(fft(bandpass_filtered))

# Plot Frequency Spectrum Before & After Filtering
plt.figure(figsize=(12, 8))
plt.subplot(3,1,1)
plt.plot(freqs[:n // 2], ecg_fft[:n // 2], label="Original ECG Spectrum", color="b")
plt.ylabel("Magnitude")
plt.title("Frequency Spectrum Before & After Filtering")
plt.legend()
plt.ylim(0,6000)
plt.grid()

plt.subplot(3,1,2)
plt.plot(freqs[:n // 2], notch_fft[:n // 2], label="Notch Filtered ECG Spectrum (50 Hz)", color="g")
plt.ylabel("Magnitude")
plt.ylim(0,6000)
plt.legend()
plt.grid()

plt.subplot(3,1,3)
plt.plot(freqs[:n // 2], bandpass_fft[:n // 2], label="Band-Pass Filtered ECG Spectrum (0.5-40 Hz)", color="r")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.ylim(0,6000)
plt.legend()
plt.grid()
plt.show()

# Full Signal Plot
plt.figure(figsize=(12, 6))
plt.subplot(3,1,1)
plt.plot(t, ecg_lead, label="Original ECG", alpha=0.6)
plt.ylabel("Amplitude (mV)")
plt.legend()
plt.grid()

plt.subplot(3,1,2)
plt.plot(t, notch_filtered, label="Notch Filtered ECG (50 Hz)", color="g")
plt.ylabel("Amplitude (mV)")
plt.legend()
plt.grid()

plt.subplot(3,1,3)
plt.plot(t, bandpass_filtered, label="Band-Pass Filtered ECG (0.5-40 Hz)", color="r")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude (mV)")
plt.legend()
plt.grid()
plt.show()

# Zoomed-in Signal Plot
zoom_start = 0
zoom_end = 5
plot_zoomed_signal(ecg_lead, t, "Original ECG", zoom_start, zoom_end, "b")
plot_zoomed_signal(bandpass_filtered, t, "Final Filtered Result", zoom_start, zoom_end, "r")
