'''
Fibonacci
Batas Run-time:	1 detik / test-case
Batas Memori:	32 MB
DESKRIPSI SOAL
Al-Kisah...

Buatlah program dengan input suatu angka integer yang menghasilkan urutan angka pada deret fibonacci

PETUNJUK MASUKAN
Input terdiri atas 1 buah angka

PETUNJUK KELUARAN
Output terdiri dari 1 angka yang merupakan angka ke i pada deret fibonacci

CONTOH MASUKAN
5
CONTOH KELUARAN
5
CONTOH MASUKAN
7
CONTOH KELUARAN
13
'''


def Fibonacci(n):
    if n < 0:
        return
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


n = int(input())
print(Fibonacci(n))
