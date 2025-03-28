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

#Since in the original signal there is no baseline issue, We add low frequency noise for experimental purpose
ecg_lead += np.sin(2*np.pi*0.2*t)

# High-Pass Filter Parameters
cutoff = 0.5  # Cutoff frequency (Hz)
order = 4  # Filter order

# Design High-Pass Butterworth Filter
b, a = butter(order, cutoff / (fs / 2), btype="high", analog=False)

# Apply High-Pass Filtering
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
plt.plot(t, filtered_signal, label="High-Pass Filtered ECG (0.5 Hz)", color="r")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude (mV)")
plt.title("ECG Before & After High-Pass Filtering (0.5 Hz)")
plt.legend()
plt.grid()
plt.show()

# Fixed Zoom Range for Better Visualization
zoom_start = 0
zoom_end = 5
plot_zoomed_signal(ecg_lead, t, "Original ECG", zoom_start, zoom_end, "b")
plot_zoomed_signal(filtered_signal, t, "High-Pass Filtered ECG", zoom_start, zoom_end, "r")
