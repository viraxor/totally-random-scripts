from pydub import AudioSegment

start = AudioSegment.from_mp3("start.mp3")
repeat = AudioSegment.from_mp3("repeat.mp3")
length = 240

new_audio = start
while new_audio.duration_seconds < length:
    new_audio = new_audio.append(repeat, crossfade=0)
    print(new_audio.duration_seconds)
    
new_audio.export("export.mp3", format="mp3")