print('hello')
f = open("1.txt", 'r')
while f:
    l = f.readline()
    if not l:
        break
    print(l)
f.close()

def cena(rub: object, kop: object = 0) -> object:
    return "%i руб. %i коп." % (rub,kop)

print (cena(3,5))
print (cena(2,5))

D = {}
D[1], D[2], D[3] = "ABB"
D[0], D[1] = "AB"
print ( len(D))

print(0 < [1, 4][1] < 3 or None)