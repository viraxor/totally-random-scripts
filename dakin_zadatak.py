br = [1998, 1999]

print(1998)
print(1999)
for i in range(10):
    st_br = br[0]
    br[0] = br[1]
    br[1] = (st_br % 1000) * (br[1] % 10)
    print(br[1])
