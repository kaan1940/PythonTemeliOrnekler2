############asal sayi tespiti############3
sayi = int(input())
asaldurumkontrol = 0
for i in range(2, (int(sayi / 2) + 1)):
    if sayi % i == 0:
        asaldurumkontrol = 1
if asaldurumkontrol == 0:
    print(str(sayi) + ":sayiniz asaldir")
else:
    print(str(sayi) + ":sayiniz asal degildir")