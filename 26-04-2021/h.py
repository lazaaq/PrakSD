"""
Hash Table
Batas Run-time:	1 detik / test-case
Batas Memori:	32 MB
DESKRIPSI SOAL
Hashing merupakan teknik yang secara khusus digunakan untuk mengidentifikasi obyek tertentu dari sekumpulan obyek yang serupa. Sebagai contoh, di universitas, setiap mahasiswa diberi nomor identifikasi khusus yang dapat digunakan untuk mendapatkan informasi mengenai mereka. Pada kedua contoh tersebut, mahasiswa diproses menggunakan hashing dengan nomor unik.

Pada kasus ini, akan digunakan fungsi menggunakan nim mahasiswa. nim mahasiswa akan di modulo n (n adalah banyak mahasiswa). Panjang Array yang akan digunakan adalah n.

Jika fungsi modulo ini menghasilkan collusion, maka digunakan metode linier, yaitu diletakkan pada index Array yang masih kosong disetelah index yang seharusnya.

Buatlah Program yang meminta input deret angka nim, tampilkan sesuai dengan isinya

PETUNJUK MASUKAN
Input terdiri atas 2 baris. Baris pertama berisi sebuah bilangan bulat positif n yang menyatakan banyak mahasiswa. Baris kedua berisi n buah bilangan bulat nim, yang menyatakan a1, a2, ..., an

PETUNJUK KELUARAN
Outputkan isi Array.

CONTOH MASUKAN
9
8 9 4 6 5 2 1 3 7
CONTOH KELUARAN
0=9
1=1
2=2
3=3
4=4
5=5
6=6
7=7
8=8
CONTOH MASUKAN
3
1 4 7
CONTOH KELUARAN
0=7
1=1
2=4
"""
n = int(input())
list_ = list(map(int, input().split()))
p = []
for i in range(len(list_)):
    mo = list_[i] % n
    while mo in p:
        mo += 1
        mo %= n
    p.append(mo)
for i in range(n):
    for j in range(0, n-i-1):
        if p[j] > p[j+1]:
            p[j], p[j+1] = p[j+1], p[j]
            list_[j], list_[j+1] = list_[j+1], list_[j]
for i in range(n):
    print(str(p[i])+"="+str(list_[i]))
