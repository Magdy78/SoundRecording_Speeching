import speech_recognition as sr

audio_file_path = "output_filtered.wav"
recognizer = sr.Recognizer()
recognizer.energy_threshold = 300

audio_file = sr.AudioFile(audio_file_path)
print(type(audio_file))

with audio_file as source:
    recognizer.adjust_for_ambient_noise(source, duration=0.5)
    audio_file_data = recognizer.record(source)

try:
    # Recognize speech using Sphinx
    text = recognizer.recognize_sphinx(audio_file_data)
    print("Sphinx recognition result:", text)
except sr.UnknownValueError:
    print("Sphinx could not understand the audio")
except sr.RequestError as e:
    print(f"Sphinx request failed; {e}")
