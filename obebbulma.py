######obeb bulma(en büyük ortakbölen bulma)#######
sayi1 = int(input()) 
sayi2 = int(input())
while sayi1 != sayi2:
    if sayi1 > sayi2 :
        sayi1 = sayi1 - sayi2
    elif sayi2 > sayi1:
        sayi2 = sayi2 - sayi1
print(sayi1)