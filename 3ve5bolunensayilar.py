##########0-100 arasi 3 ve 5 bolunen sayilari bulduk###########
sayi = 0
ucevebesebolunensayiadedi = 0
while sayi < 100:
    sayi += 1
    if sayi %3 == 0 and sayi % 5 == 0:
        ucevebesebolunensayiadedi += 1
        print(sayi)
print("ucevebesebolunensayiadedi: " + str(ucevebesebolunensayiadedi))