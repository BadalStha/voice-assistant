import sounddevice as sd

duration = 5
fs = 44100

sd.default.device = 13

#record
print("Recoding...")
myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()
print("Recoding finished")

#playback
print("Playing back...")
sd.play(myrecording, fs)
sd.wait()
print("Done")