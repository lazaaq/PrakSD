n = int(input())
arr = input().split() #1 2 3 4 5
arr_baru = []
for i in range(n): #0 / n-1
    arr_baru.insert(i // 2, arr[i])
a = " ".join(arr_baru) + " "
print(a)