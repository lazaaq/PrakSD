"""
Cermin Tree
Batas Run-time:	1 detik / test-case
Batas Memori:	32 MB
DESKRIPSI SOAL
Membentuk Cermin Tree dari N data (N<=0), tp tidak boleh ada angka yang sama.

Cermin Tree adalah efek Tree yang dicerminkan. Kita tahu efek dari suatu cermin adalah membalik yang kanan menjadi kiri dan sebaliknya. Sehingga Cermin Tree adalah suatu Tree dimana node dengan angka yang lebih besar berada di kiri dan yang lebih kecil berada di kanan

Anda diminta untuk menampilkan cermin tree ini dalam preOrder, InOrder dan PostOrder

PETUNJUK MASUKAN
Input terdiri atas 2 baris. Baris pertama berisi sebuah bilangan bulat positif n yang menyatakan banyak angka. Baris kedua berisi n buah bilangan bulat, yang akan digunakan untuk membentuk tree

PETUNJUK KELUARAN
outputkan 3 baris.

baris 1: output preorder, pisahkan setiap angka dengan spasi

baris 2: output inorder, pisahkan setiap angka dengan spasi

baris 3: output postorder, pisahkan setiap angka dengan spasi

CONTOH MASUKAN
5
4 5 5 6 2
CONTOH KELUARAN
4 5 6 2
6 5 4 2
6 5 2 4
CONTOH MASUKAN
6
1 1 1 1 1 1
CONTOH KELUARAN
1
1
1
"""
import sys


class Node:
    def __init__(self, angka):
        self.angka = angka
        self.left = None
        self.right = None


pre = ""
ino = ""
pos = ""

boolean1 = True
boolean2 = True
boolean3 = True


class BST:
    def __init__(self):
        self.root = None

    def insert(self, angka):
        if self.root == None:
            self.root = Node(angka)
            self.root.left = BST()
            self.root.right = BST()
        elif self.root.angka < angka:
            self.root.left.insert(angka)
        elif self.root.angka > angka:
            self.root.right.insert(angka)
        else:
            return


pre = []
ino = []
pos = []


def preOrder(self):
    global pre
    if self.root != None:
        pre.append(str(self.root.angka))
        preOrder(self.root.left)
        preOrder(self.root.right)


def inOrder(self):
    global ino
    if self.root != None:
        inOrder(self.root.left)
        ino.append(str(self.root.angka))
        inOrder(self.root.right)


def postOrder(self):
    global pos
    if self.root != None:
        postOrder(self.root.left)
        postOrder(self.root.right)
        pos.append(str(self.root.angka))


pohon = BST()
n = int(input())
l = [int(i) for i in input().split()]
for i in l:
    pohon.insert(i)
preOrder(pohon)
inOrder(pohon)
postOrder(pohon)
print(" ".join(pre) + " ")
print(" ".join(ino) + " ")
print(" ".join(pos) + " ")
