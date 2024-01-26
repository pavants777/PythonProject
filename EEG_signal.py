import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Function to classify frequency band
def classify_frequency_band(frequency):
    if 0.5 <= frequency <= 4:
        return 'Delta', 0.5, 4
    elif 4 <= frequency <= 8:
        return 'Theta', 4, 8
    elif 8 <= frequency <= 12:
        return 'Alpha', 8, 12
    elif 12 <= frequency <= 30:
        return 'Beta', 12, 30
    elif 30 <= frequency <= 100:
        return 'Gamma', 30, 100
    else:
        return 'Other', 100, 1000

# Function to apply bandpass filtering
def bandpass_filter(signal_data, lowcut, highcut, fs, order=4):
    nyquist = 2 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = signal.butter(order, [low, high], btype='band')
    filtered_signal = signal.filtfilt(b, a, signal_data)
    return filtered_signal

# Get user input for the frequency
try:
    frequency = float(input("Enter a frequency (Hz): "))
except ValueError:
    print("Invalid input. Please enter a numeric value.")
    exit()

# Generate synthetic EEG data as an example
fs = 100  
t = np.arange(0, 10, 1/fs)  # 10 seconds of data
eeg_signal = np.sin(2 * np.pi * frequency * t) + 0.5 * np.random.randn(len(t))

# Classify the frequency band
classified_band, low, high = classify_frequency_band(frequency)

# Apply bandpass filter to extract the specified frequency band
filtered_band = bandpass_filter(eeg_signal, low, high, fs)

# Plot the original and filtered signals
plt.figure(figsize=(12, 4))

plt.subplot(211)
plt.plot(t, eeg_signal, label='Original EEG Signal')
plt.title('Original EEG Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(212)
plt.plot(t, filtered_band, label=f'{classified_band} Band ({low} - {high} Hz)')
plt.title(f'{classified_band} Band')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.show()

print(f'Classified Frequency Band: {classified_band}')
