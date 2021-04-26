"""
Soal 4
Batas Run-time:	1 detik / test-case
Batas Memori:	32 MB
DESKRIPSI SOAL
Diberikan n buah bilangan bulat, a1, a2, ..., an. Kemudian dibentuk binary search tree dari barisan tersebut. Tugas Anda ialah menentukan apakah terdapat bilangan k pada binary search tree yang terbentuk. Untuk lebih jelasnya, perhatikan contoh testcase di bawah.

PETUNJUK MASUKAN
Input terdiri atas 3 baris. Baris pertama berisi sebuah bilangan bulat positif n yang menyatakan banyak bilangan. Baris kedua berisi n buah bilangan bulat, yang menyatakan a1, a2, ..., an. Baris ketiga berisi sebuah bilangan bulat k yang menyatakan bilangan yang akan ditanyakan.

PETUNJUK KELUARAN
Outputkan "YA" jika terdapat bilangan k pada binary search tree yang terbentuk, atau outputkan "TIDAK" jika tidak terdapat bilangan k pada binary search tree yang terbentuk.

CONTOH MASUKAN 1
9
3 0 8 2 4 9 1 5 6
0
CONTOH KELUARAN 1
YA
CONTOH MASUKAN 2
9
3 0 8 2 4 9 1 5 6
7
CONTOH KELUARAN 2
TIDAK
KETERANGAN
Pada kedua contoh, binary search tree yang terbentuk adalah sebagai berikut.

Pada contoh pertama, outputnya adalah "YA", karena terdapat bilangan 0 pada binary search tree yang terbentuk.

Pada contoh kedua, outputnya adalah "TIDAK", karena tidak terdapat bilangan 7 pada binary search tree yang terbentuk.
"""
n = int(input())
list_ = input().split()
k = input()
if k in list_:
    print("YA")
else:
    print("TIDAK")
