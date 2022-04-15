#######10luk sayiyi 2lik sayiya cevirme######
sayi = int(input())
ikisayitabani =""
while sayi > 1:
    kalan = sayi % 2
    sayi = int(sayi / 2)
    ikisayitabani = str(kalan) + ikisayitabani
ikisayitabani = "1" + ikisayitabani
print("ikilik tabanda: " + ikisayitabani)