"""
Soal 1
Batas Run-time:	1 detik / test-case
Batas Memori:	32 MB
DESKRIPSI SOAL
Diberikan n buah bilangan bulat, a1, a2, ..., an. Kemudian dibentuk binary search tree dari barisan tersebut. Tugas Anda ialah mengoutputkan secara postorder.

PETUNJUK MASUKAN
Input terdiri atas 2 baris. Baris pertama berisi sebuah bilangan bulat positif n yang menyatakan banyak bilangan. Baris kedua berisi n buah bilangan bulat, yang menyatakan a1, a2, ..., an

PETUNJUK KELUARAN
Outputkan secara preorder.

CONTOH MASUKAN
9
3 0 8 2 4 9 1 5 6
CONTOH KELUARAN 1
3
0
2
1
8
4
5
6
9
"""


class Node:
    def __init__(self, angka):
        self.angka = angka
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, angka):
        if self.root is None:
            nodeBaru = Node(angka)
            self.root = nodeBaru
            self.root.left = BST()
            self.root.right = BST()
        else:
            if self.root.angka > angka:
                self.root.left.insert(angka)
            else:
                self.root.right.insert(angka)

    def postOrder(self):
        if self.root is not None:
            self.root.left.postOrder()
            self.root.right.postOrder()
            print(self.root.angka)


pohon = BST()
n = int(input())
list_ = input().split()
for i in list_:
    pohon.insert(i)
pohon.postOrder()
