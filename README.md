# ECG Signal Filtering Project

## Project Overview
This project focuses on denoising real-world ECG signals by applying multiple filtering techniques to remove artifacts.

- **Dataset:** MIT-BIH Arrhythmia Database (PhysioNet)
- **Filtering Methods:** Notch, Low-Pass, High-Pass, Band-Stop, Band-Pass
- **Analysis:** Time-domain & Frequency-domain (FFT) comparison
- **Results:** Plotted before & after filtering

## Objectives
- Load real ECG signals and analyze their raw characteristics.
- Apply different filtering techniques to remove artifacts.
- Use FFT analysis to compare frequency spectra before & after filtering.
- Provide zoomed-in views for better ECG visualization.

## Dataset Details
- **Source:** MIT-BIH Arrhythmia Database ([PhysioNet](https://physionet.org/content/mitdb/1.0.0/))
- **Sampling Frequency:** 360 Hz
- **Lead Used:** MLII (Lead II)
- **Example Record:** 100

## Filtering Techniques Used

### 1. Notch Filter (50/60 Hz)
- **Purpose:** Removes powerline interference at 50 Hz.
- **Method:** Implemented using `scipy.signal.iirnotch()`.
- **Effectiveness:** Verified using FFT before & after filtering.

### 2. Low-Pass Filter (50 Hz)
- **Purpose:** Removes high-frequency noise (e.g., muscle artifacts).
- **Method:** Implemented using `scipy.signal.butter()` and `filtfilt()`.

### 3. High-Pass Filter (0.5 Hz)
- **Purpose:** Removes low-frequency drift (e.g., baseline wander).
- **Method:** Implemented using `scipy.signal.butter()` and `filtfilt()`.

### 4. Band-Stop Filter (55-65 Hz)
- **Purpose:** Removes a range of powerline noise instead of just 50/60 Hz.
- **Method:** Implemented using `scipy.signal.butter()` with `btype='bandstop'`.

### 5. Band-Pass Filter (0.5/1 - 40/50 Hz)
- **Purpose:** Most effective filtering method, removing both baseline drift & high-frequency noise while preserving ECG features.
- **Method:** Implemented using `scipy.signal.butter()` with `btype='band'`.

## Results & Visualizations
The project includes:
- Original ECG vs. Notch Filtered ECG
- Original ECG vs. Low-Pass Filtered ECG
- Original ECG vs. High-Pass Filtered ECG
- Original ECG vs. Band-Stop Filtered ECG
- Original ECG vs. Band-Pass Filtered ECG

### Sample FFT Analysis
- **Before Filtering (Original Signal FFT):** Shows noise peaks.
- **After Filtering (Processed Signal FFT):** Noise peaks are removed.
- **Zoomed ECG Views:** Highlighting signal improvements.

**Results are stored in the `results/` folder.**

## How to Run This Project?

### Install Required Libraries
```bash
pip install wfdb numpy scipy matplotlib
```

### Run Individual Filters
Example:
```bash
python band_pass_filter.py
```

### Run Complete Filtering Pipeline
```bash
python ecg_filtering.py
```

### Run in Jupyter Notebook (Recommended)
Use `ECG_Filtering.ipynb` for interactive visualization.

## Future Improvements
- Implement Adaptive Filtering for real-time ECG noise cancellation.
- Explore AI/ML-based ECG denoising techniques.
- Process multi-lead ECG analysis.

## References
- **MIT-BIH Arrhythmia Database:** [PhysioNet](https://physionet.org/content/mitdb/1.0.0/)
- **Signal Processing Techniques in ECG Analysis**

## Author
- **GitHub Repository:** [https://github.com/Vk4Sp/ECG-Filtering)]
- **License:** MIT License

 Contributions are welcome!

