import glob
import os

for file in glob.glob("./*.compat.*"):
    os.rename(file, file.replace(".compat", ""))
    
for file in glob.glob("./*.*"):
    os.rename(file, file.replace(" ", "_").replace("(", "_").replace(")", ""))
