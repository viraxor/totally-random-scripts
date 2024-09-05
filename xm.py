import glob

filelist = glob.glob('/storage/emulated/0/Music/modules/*.xm')
print(filelist)

for file in filelist:
    with open(file, "rb") as f:
        content = f.read()
    content = content[:17] + b'\x00'*20 + content[37:]
    with open(file, "wb") as f:
        f.write(content)
    print(file)