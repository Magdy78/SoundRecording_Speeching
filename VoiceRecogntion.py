import speech_recognition as sr

def transcribe_audio(audio_file_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)

    try:
        # Use Sphinx for speech recognition
        text = recognizer.recognize_sphinx(audio_data)
        return text
    except sr.UnknownValueError:
        print("Sphinx could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Sphinx; {e}")

audio_file_path = "output_filtered.wav"
transcribed_text = transcribe_audio(audio_file_path)
print(transcribed_text)
