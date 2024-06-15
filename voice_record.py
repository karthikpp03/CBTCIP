import sounddevice as sd
import wavio

def record_voice(filename, duration, samplerate=44100):
    print("Recording...")
    
    audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2, dtype='int16')
    sd.wait()  
    print("Recording finished.")

    
    wavio.write(filename, audio_data, samplerate, sampwidth=2)
    print(f"Saved as {filename}")


filename = "recorded_voice.wav"
duration = 5  
record_voice(filename, duration)
