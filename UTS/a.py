import sys
def binerKeDesimal(biner):
    pangkat = len(biner) - 1
    desimal = 0
    for i in range(len(biner)):
        iBin = int(biner[i])
        iDes = iBin * (2 ** pangkat)
        desimal += iDes
        pangkat -= 1
    return str(desimal)
a = binerKeDesimal(input())
sys.stdout.write(a)