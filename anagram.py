s = input()
s = s.replace(" ", "").lower()

def anagram(s):
    rtlist = []
    if s == "":
        return [""]
    for i in range(len(s)):
        l = s[i]
        if ord(l) >= 97 and ord(l) <= 122:
            for new in anagram(s[:i] + s[i+1:]):
                rtlist.append(l + new)
    return rtlist
    
list = anagram(s)
ws = ""
for i in list:
    ws += f"{i}\n"
with open("anagrams.txt", "w") as f:
    f.write(ws)