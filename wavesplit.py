import wave
import sys

filename = sys.argv[1]
f = wave.open(filename, 'r')

fr = f.getframerate()
channels = f.getnchannels()
sampwidth = f.getsampwidth()
seconds = fr * 60

total = f.getnframes()
max_i = total // seconds
for i in range(max_i):
    new_f = wave.open(f"filename_{i}.wav", "w")
    new_f.setframerate(fr)
    new_f.setnchannels(channels)
    new_f.setsampwidth(sampwidth)
    frames = f.readframes(seconds)
    new_f.writeframes(frames)
    new_f.close()
new_f = wave.open(f"filename_{max_i}.wav", "w")
new_f.setframerate(fr)
new_f.setnchannels(channels)
new_f.setsampwidth(sampwidth)
frames = f.readframes(total - seconds*max_i)
new_f.writeframes(frames)
new_f.close()