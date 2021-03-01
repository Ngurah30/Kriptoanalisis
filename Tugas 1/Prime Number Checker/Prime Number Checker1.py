# Menginputin bilangan yang akan di cek
bil = int(input("Masukkan bilangan : "))
# Bilangan prima harus lebih besar dari 1
if bil > 1:
    for i in range(2, bil):
        if (bil % i) == 0:
            print(bil, "bukan bilangan prima")
            break
    else:
        print(bil,"adalah bilangan prima")
# Jika bilangan kurang atau sama dengan satu
else:
    print(bil, "bukan bilangan prima")
