import glob
from pydub import AudioSegment
import random

audio = AudioSegment.empty()
globlist = glob.glob("./smp/*.flac")
smplist = []

print("loading samples")
for sample in globlist:
    smplist.append(AudioSegment.from_file(sample, "flac"))

print("making song")
for i in range(random.randint(256, 2048)):
    sample = random.choice(smplist)
    audio += sample
    
print("exporting")
audio.export("track.mp3", format="mp3")
