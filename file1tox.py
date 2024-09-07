n = int(input())
res = ""
for i in range(1, n):
    res += f"{i}, "
res = res[:-2]
with open("./file1tox.txt", "w") as f:
    f.write(res)