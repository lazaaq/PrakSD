"""
Soal 2
Batas Run-time:	1 detik / test-case
Batas Memori:	32 MB
DESKRIPSI SOAL
Diberikan n buah bilangan bulat, a1, a2, ..., an. Kemudian dibentuk binary search tree dari barisan tersebut. Tugas Anda ialah menentukan banyaknya leaf dari binary search tree yang terbentuk. Untuk lebih jelasnya, perhatikan contoh testcase di bawah.

PETUNJUK MASUKAN
Input terdiri atas 2 baris. Baris pertama berisi sebuah bilangan bulat positif n yang menyatakan banyak bilangan. Baris kedua berisi n buah bilangan bulat, yang menyatakan a1, a2, ..., an

PETUNJUK KELUARAN
Outputkan sebuah bilangan bulat yang merupakan banyaknya leaf dari binary search tree yang terbentuk.

CONTOH MASUKAN
9
3 0 8 2 4 9 1 5 6
CONTOH KELUARAN 1
3
KETERANGAN
Pada contoh testcase, binary search tree yang terbentuk adalah sebagai berikut.

Sehingga, banyaknya leaf adalah 3.
"""


class Node:
    def __init__(self, angka):
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

    def preOrder(self):
        if self.root != None:
            print(self.root.angka)
            self.root.left.preOrder()
            self.root.right.preOrder()


pohon = ST()
n = int(input())
list_ = input().split()
for i in list_:
    pohon.insert(i)
print(pohon.preOrder())
