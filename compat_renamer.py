import glob
import os

for file in glob.glob("./*.compat.*"):
    os.rename(file, file.replace(".compat", ""))