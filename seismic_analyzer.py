import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, spectrogram


# ============================================================
# 1. LOAD SEISMIC DATA
# ============================================================

file_name = "earthquake.csv"

data = pd.read_csv(file_name)

time = data["time"].values
signal = data["acceleration"].values


# ============================================================
# 2. BASIC SIGNAL INFORMATION
# ============================================================

number_of_samples = len(signal)

dt = time[1] - time[0]

sampling_frequency = 1 / dt

duration = time[-1] - time[0]


print()
print("==========================================")
print("       SEISMIC SIGNAL ANALYZER")
print("==========================================")

print("Number of samples:", number_of_samples)

print(
    "Sampling frequency:",
    round(sampling_frequency, 2),
    "Hz"
)

print(
    "Signal duration:",
    round(duration, 2),
    "seconds"
)


# ============================================================
# 3. RAW SEISMIC SIGNAL
# ============================================================

plt.figure(figsize=(12, 5))

plt.plot(time, signal)

plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude (counts)")

plt.title("Raw Seismic Signal - Time Domain")

plt.grid(True)

plt.tight_layout()

plt.show()


# ============================================================
# 4. FFT
# ============================================================

N = len(signal)

fft_values = np.fft.rfft(signal)

frequencies = np.fft.rfftfreq(
    N,
    d=1 / sampling_frequency
)

magnitude = np.abs(fft_values)

magnitude[0] = 0


# ============================================================
# 5. DOMINANT FREQUENCY
# ============================================================

dominant_index = np.argmax(magnitude)

dominant_frequency = frequencies[dominant_index]

print(
    "Dominant frequency:",
    round(dominant_frequency, 3),
    "Hz"
)


# ============================================================
# 6. FREQUENCY SPECTRUM
# ============================================================

plt.figure(figsize=(12, 5))

plt.plot(
    frequencies,
    magnitude
)

plt.xlabel("Frequency (Hz)")

plt.ylabel("Magnitude")

plt.title("Frequency Spectrum of Seismic Signal")

plt.xlim(
    0,
    sampling_frequency / 2
)

plt.grid(True)

plt.tight_layout()

plt.show()


# ============================================================
# 7. BAND-PASS FILTER
# ============================================================

low_cutoff = 0.5

high_cutoff = min(
    8,
    sampling_frequency / 2 - 1
)


if high_cutoff <= low_cutoff:

    print()
    print("Sampling frequency is too low for filtering.")

    filtered_signal = signal.copy()

else:

    normalized_low = (
        low_cutoff /
        (sampling_frequency / 2)
    )

    normalized_high = (
        high_cutoff /
        (sampling_frequency / 2)
    )

    b, a = butter(
        4,
        [
            normalized_low,
            normalized_high
        ],
        btype="bandpass"
    )

    filtered_signal = filtfilt(
        b,
        a,
        signal
    )

    print()
    print(
        "Band-pass filter:",
        low_cutoff,
        "-",
        high_cutoff,
        "Hz"
    )


# ============================================================
# 8. FILTERED SIGNAL
# ============================================================

plt.figure(figsize=(12, 5))

plt.plot(
    time,
    filtered_signal
)

plt.xlabel("Time (seconds)")

plt.ylabel("Amplitude (counts)")

plt.title("Filtered Seismic Signal")

plt.grid(True)

plt.tight_layout()

plt.show()


# ============================================================
# 9. SPECTROGRAM
# ============================================================

frequencies_stft, times_stft, power = spectrogram(
    filtered_signal,
    fs=sampling_frequency
)


# ============================================================
# 10. SPECTROGRAM PLOT
# ============================================================

plt.figure(figsize=(12, 6))

power_db = 10 * np.log10(
    power + 1e-12
)

plt.pcolormesh(
    times_stft,
    frequencies_stft,
    power_db,
    shading="auto"
)

plt.xlabel("Time (seconds)")

plt.ylabel("Frequency (Hz)")

plt.title(
    "Seismic Signal Time-Frequency Analysis"
)

plt.colorbar(
    label="Power (dB)"
)

plt.ylim(
    0,
    min(
        8,
        sampling_frequency / 2
    )
)

plt.tight_layout()

plt.show()


# ============================================================
# 11. FINAL SUMMARY
# ============================================================

print()
print("==========================================")
print("           ANALYSIS SUMMARY")
print("==========================================")

print(
    "Samples:",
    number_of_samples
)

print(
    "Sampling frequency:",
    round(sampling_frequency, 2),
    "Hz"
)

print(
    "Signal duration:",
    round(duration, 2),
    "seconds"
)

print(
    "Dominant frequency:",
    round(dominant_frequency, 3),
    "Hz"
)

print(
    "Filter range:",
    low_cutoff,
    "-",
    high_cutoff,
    "Hz"
)

print()
print("Analysis completed successfully.")