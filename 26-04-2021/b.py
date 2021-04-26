"""
Soal 1
Batas Run-time:	1 detik / test-case
Batas Memori:	32 MB
DESKRIPSI SOAL
Diberikan n buah bilangan bulat, a1, a2, ..., an. Kemudian dibentuk binary search tree dari barisan tersebut. Tugas Anda ialah menentukan tinggi dari binary search tree tersebut.

PETUNJUK MASUKAN
Input terdiri atas 2 baris. Baris pertama berisi sebuah bilangan bulat positif n yang menyatakan banyak bilangan. Baris kedua berisi n buah bilangan bulat, yang menyatakan a1, a2, ..., an

PETUNJUK KELUARAN
Outputkan sebuah bilangan bulat yang merupakan tinggi dari binary search tree yang terbentuk.

CONTOH MASUKAN
9
3 0 8 2 4 9 1 5 6
CONTOH KELUARAN 1
5
KETERANGAN
Pada contoh testcase, binary search tree yang terbentuk adalah sebagai berikut.

Sehingga, tingginya adalah 5.
"""


class Node:
    def __init__(self, angka=None):
        self.angka = angka
        self.left = None
        self.right = None


class ST:
    def __init__(self):
        self.root = None

    def insert(self, angka):
        if self.root is None:
            nodeBaru = Node(angka)
            self.root = nodeBaru
            self.root.left = ST()
            self.root.right = ST()
        else:
            if self.root.angka > angka:
                self.root.left.insert(angka)
            else:
                self.root.right.insert(angka)

    def getTinggi(self):
        if self.root is None:
            return -1
        else:
            return 1 + max(self.root.left.getTinggi(), self.root.right.getTinggi())


pohon = ST()
n = int(input())
list_ = input().split()
for i in list_:
    pohon.insert(i)
print(pohon.getTinggi() + 1)
