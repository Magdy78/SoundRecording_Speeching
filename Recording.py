import pyaudio
import wave


frames_per_buffer = 3200  # Record in buffer of 3200 samples Chunk
format = pyaudio.paInt32  # 32 bit per sample
channels = 2 # Stereo
sample_rate = 16000



p = pyaudio.PyAudio()  # pyaudio object instance 


stream = p.open(format=format,
                channels=channels,
                rate=sample_rate,
                input=True,  # to capture audio
                frames_per_buffer=frames_per_buffer)


print("Start Recording")

seconds = 5  # record duration
frames = []  # Initialize array to store frames
for i in range(0, int(sample_rate / frames_per_buffer * seconds)):
    data = stream.read(frames_per_buffer)  # read 3200 frame at each iteration
    frames.append(data)# append to list of Frames
    
    
print("Finished Recording")
stream.stop_stream()
stream.close()
p.terminate()


wf = wave.open("output.wav", "wb")
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(format))
wf.setframerate(sample_rate)
# write all frames in binary string, combine all frames into binary string .
wf.writeframes(b''.join(frames))
wf.close()
