import wfdb
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Load ECG Data
record_name = "100"
database = "mitdb"
signal, fields = wfdb.rdsamp(record_name, pn_dir=database)
fs = fields["fs"]  # Sampling frequency
t = np.arange(len(signal)) / fs  # Time axis
ecg_lead = signal[:, 0]  # Select first ECG lead (MLII)

# Low-Pass Filter Parameters
cutoff = 40  # Cutoff frequency (Hz)
order = 4  # Filter order

# Design Low-Pass Butterworth Filter
b, a = butter(order, cutoff / (fs / 2), btype="low", analog=False)

# Apply Low-Pass Filtering
filtered_signal = filtfilt(b, a, ecg_lead)

# Function for Zooming In on Specific Time Ranges
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

# Plot Full Signal
plt.figure(figsize=(12, 5))
plt.plot(t, ecg_lead, label="Original ECG", alpha=0.6)
plt.plot(t, filtered_signal, label="Low-Pass Filtered ECG (40 Hz)", color="r")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude (mV)")
plt.title("ECG Before & After Low-Pass Filtering (40 Hz)")
plt.legend()
plt.grid()
plt.show()

# Predefined Zoom Ranges
zoom_start = 0
zoom_end = 5
plot_zoomed_signal(ecg_lead, t, "Original ECG", zoom_start, zoom_end, "b")
plot_zoomed_signal(filtered_signal, t, "Low-Pass Filtered ECG", zoom_start, zoom_end, "r")
    
