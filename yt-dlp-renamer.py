import glob
import os

artist = input("Artist name:")

filelist = glob.glob("./*.mp3")
for file in filelist:
    ren_filename = file[2:-4] # gets out ./ and .mp3
    if not ren_filename.lower().startswith(artist.lower()):
        ren_filename = artist + "-" + ren_filename
        
    if "[" in ren_filename:
        pos = ren_filename.index("[")
        ren_filename = ren_filename[:pos-1]
    try:
        os.rename(file, f"./{ren_filename}.mp3")
    except FileExistsError:
        os.remove(file)