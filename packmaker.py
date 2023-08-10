import os
import shutil
import glob
import random

n = input("pack name: ")
if not os.path.exists(n):
    os.mkdir(n)
else:
    shutil.rmtree(n)
    os.mkdir(n)
    
print("loading samples")
sample_list = glob.glob("./**/*.flac", recursive=True)

print("making pack")
pack_samples = random.sample(sample_list, random.randint(7, 31))

for smp in pack_samples:
    filename = smp.split("/")[-1].split("\\")[-1]
    shutil.copy(smp, f"./{n}/{filename}")
