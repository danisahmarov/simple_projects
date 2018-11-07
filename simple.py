print('hello')
f = open("1.txt", 'r')
while f:
    l = f.readline()
    if not l:
        break
    print(l)
f.close()

def cena(rub,kop=0):
    return "%i руб. %i коп." % (rub,kop)

print (cena(3,5))
print (cena(2,5))