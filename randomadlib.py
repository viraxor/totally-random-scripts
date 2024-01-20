import random

output = b"\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"

for i in range(8):
    output += bytes([random.randint(0, 255)])
for i in range(2):
    output += bytes([random.randint(0, 7)])
for i in range(3):
    output += bytes([random.randint(0, 255)])
    
output += b"\x00\x00\x00\xAB\x20\x00\x00\x4F\x70\x65\x6E"
for i in range(36):
    output += b"\x00"
output += b"SCRI"

with open("./adlib.s3i", "wb") as f:
    f.write(output)