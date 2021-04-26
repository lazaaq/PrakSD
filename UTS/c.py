n = int(input())
besar = 0
sedang = 0
kecil = 0
if n <= 9000 and n >= 0:
    besar = n // 1500
    print(besar)
if n <= 13200 and n > 9000:
    besar = 6
    sedang = (n - besar * 1500) // 600
    print(besar + sedang)
if n <= 15000 and n > 13200:
    besar = 6
    sedang = 7
    kecil = (n - besar * 1500 - sedang * 600) // 200
    print(besar + sedang + kecil)
if n > 15000:
    print(22)