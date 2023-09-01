import glob

all_splits = sorted(glob.glob("sharedassets*.assets.split*"))
number = -1
index = 0

ordered_splits = []

for splitfile in all_splits:
    split_number = int(splitfile.split(".")[0][12:])
    if split_number != number:
        if index != 0:
            ordered_splits.append(all_splits[index:all_splits.index(splitfile)])
        index = all_splits.index(splitfile)
        number = split_number

for splits in ordered_splits:
    print(splits)
    content = b""
    for file in splits:
        with open(file, "rb") as f:
            content += f.read()
        split_number = file.split(".")[0][12:]
    with open(f"sharedassets{split_number}.assets", "wb") as f:
        f.write(content)