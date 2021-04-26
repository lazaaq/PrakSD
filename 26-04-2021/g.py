"""
CariDeleteNode
Batas Run-time:	1 detik / test-case
Batas Memori:	32 MB
DESKRIPSI SOAL
Binary Search Tree (BST) adalah suatu keadaan dimana setiap node X, semua elemen di subpohon kirinya bernilai lebih kecil dari nilai X dan semua elemen di subpohon kanannya bernilai lebih besar dari nilai X. Oleh Karena itu, saat akan menghapus sebuah node, kita juga harus memikirkan seluruh node anak dari node tsb. Hal penting adalah agar pohon setelah dihapus tetap merupakan BST

Ada 3 kasus dalam penghapusan Node.

1. Node merupakan leaf/daun. Pada kasus ini, penghapusan bisa langsung dilakukan.

2. Pada kasus Node memiliki degree 1, maka node anak bisa langsung menggantikan posisinya.

3. Kasus terakhir menjadi sedikit rumit, yaitu ketika Node memiliki degree 2. Pada kasus ini, maka harus dipilih node yang bisa menggantikan. Node yang dapat menggantikan adalah Node yang nilainya terbesar dari dari subpohon sebelah kirinya. perlu diingat, jika suatu Node digunakan untuk menggantikan posisi dari suatu node lain, maka posisinya seperti dilakukan penghapusan.

Buatlah Program yang meminta input deret angka, kemudian susunlah menjadi suatu tree, kemudian pilihlah Node mana yang layak menggantikan.

PETUNJUK MASUKAN
Input terdiri atas 3 baris. Baris pertama berisi sebuah bilangan bulat positif n yang menyatakan banyak bilangan. Baris kedua berisi n buah bilangan bulat, yang menyatakan a1, a2, ..., an

Baris 3 menunjukkan Node yang akan dihapus

PETUNJUK KELUARAN
Outputkan Node mana yang layak menggantikan. Jika tidak perlu digantikan Node lain, maka outputkan -1

CONTOH MASUKAN
9
8 9 4 6 5 2 1 3 7
1
CONTOH KELUARAN
-1
CONTOH MASUKAN
9
8 9 4 6 5 2 1 3 7
6
CONTOH KELUARAN
5
CONTOH MASUKAN
9
8 9 4 6 5 2 1 3 7
8
CONTOH KELUARAN
7
"""
n = int(input())
list_ = list(map(int, input().split()))
list_sorted = sorted(list_)
k = int(input())
idx = list_sorted.index(k)
if idx == 0:
    print(-1)
else:
    print(list_sorted[idx-1])
