n = int(input())
arr = []
for i in range(n):
    a = input().split()
    arr.append(a)
nis = input()

ketemu = 0
for i in range(n):
    if (arr[i][0] == nis):
        ketemu = i
        break

if ketemu == 0:
    print("langsung bayar")
else:
    for i in range(ketemu - 1, -1, -1):
        print(arr[i][1])
# n = int(input())
# nis = []
# nama = []
# for i in range(n):
#     a, b = input().split()
#     nis.append(a)
#     nama.append(b)

# nis_fokus = input()

# ketemu = nis.index(nis_fokus)
# if ketemu == 0:
#     print("langsung bayar")
# else:
#     for i in range(ketemu - 1, -1, -1):
#         print(nama[i])