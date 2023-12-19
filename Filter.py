import wave
import numpy as np
from scipy.signal import butter, lfilter

def apply_band_stop_filter(data, lowcut, highcut, sample_rate, order=4):
    nyquist = 0.5 * sample_rate
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='bandstop')
    filtered_data = lfilter(b, a, data)
    return filtered_data

# Load the recorded sound from the WAV file
input_filename = "output.wav"
output_filename = "output_filtered.wav"

with wave.open(input_filename, 'rb') as wf:
    channels = wf.getnchannels()
    sample_width = wf.getsampwidth()
    sample_rate = wf.getframerate()
    frames = wf.readframes(wf.getnframes())

# Convert binary string frames to numpy array
audio_data = np.frombuffer(frames, dtype=np.int32)

# Apply band-stop filter
lowcut = 500  # Specify the lower cutoff frequency of the band-stop filter
highcut = 1500  # Specify the higher cutoff frequency of the band-stop filter
filtered_data = apply_band_stop_filter(audio_data, lowcut, highcut, sample_rate)

# Convert the filtered data back to binary string
filtered_frames = filtered_data.astype(np.int32).tobytes()

# Save the filtered audio to a new WAV file
with wave.open(output_filename, 'wb') as wf:
    wf.setnchannels(channels)
    wf.setsampwidth(sample_width)
    wf.setframerate(sample_rate)
    wf.writeframes(filtered_frames)

print(f"Filtered audio saved as {output_filename}")
