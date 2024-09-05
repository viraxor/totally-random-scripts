import glob

filelist = glob.glob('/storage/emulated/0/Music/modules/Nagz/*.s3m')
print(filelist)

for file in filelist:
    with open(file, "rb") as f:
        content = f.read()
    content = b'\x00'*28 + content[28:]
    with open(file, "wb") as f:
        f.write(content)
    print(file)