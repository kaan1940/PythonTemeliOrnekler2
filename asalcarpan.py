########asal carpan bulma##########
sayi = int(input())
bolen = 2
bolenadedi = 0
while sayi > 1:
    if sayi % bolen == 0:
        bolenadedi +=1
        sayi = sayi / bolen
        print(bolen)
    else:
        bolen +=1
print("bolenadedi:" + str(bolenadedi))