import math
print("Silahkan Pilih")
print("a). Bola")
print("b). Kubus")
print("c). Balok")
pilihan_utama = input("Masukkan pilihan utama (a/A/b/B/c/C): ")

if pilihan_utama == "a":
    print("Pilihan pemilihan:")
    print("1. Keliling")
    print("2. Luas")
    print("3. Volume")

    pilihan_bola = int(input("Masukkan pilihan menghitung bola (1/2/3): "))

    if pilihan_bola == 1:
        jari_jari = int(input("Masukkan jari-jari bola: "))
        keliling = 2 * math.pi * jari_jari
        print("Keliling bola:", keliling)
    elif pilihan_bola == 2:
        jari_jari = int(input("Masukkan jari-jari bola: "))
        luas = 4 * math.pi * jari_jari ** 2
        print("Luas permukaan bola:", luas)
    elif pilihan_bola == 3:
        jari_jari = int(input("Masukkan jari-jari bola: "))
        volume = (4/3) * math.pi * jari_jari ** 3
        print("Volume bola:", volume)
    else:
        print("pilihan_bola tidak ada")
        
elif pilihan_utama == "b":
    print("Pilihan pemilihan:")
    print("1. Keliling")
    print("2. Luas")
    print("3. Volume")

    pilihan_kubus = int(input("Masukkan pilihan menghitung kubus (1/2/3): "))

    if pilihan_kubus == 1:
        sisi = int(input("Masukkan panjang sisi kubus: "))
        keliling = 12 * sisi
        print("Keliling kubus:", keliling)
    elif pilihan_kubus == 2:
        sisi = int(input("Masukkan panjang sisi kubus: "))
        luas = 6 * sisi ** 2
        print("Luas permukaan kubus:", luas)
    elif pilihan_kubus == 3:
        sisi = int(input("Masukkan panjang sisi kubus: "))
        volume = sisi ** 3
        print("Volume kubus:", volume)
    else:
        print("Pilihan tidak ada")

elif pilihan_utama == "c":
    print("Pilihan pemilihan:")
    print("1. Keliling")
    print("2. Luas")
    print("3. Volume")

    pilihan_balok = int(input("Masukkan pilihan menghitung balok (1/2/3): "))

    if pilihan_balok == 1:
        panjang = int(input("Masukkan panjang balok: "))
        lebar = int(input("Masukkan lebar balok: "))
        tinggi = int(input("Masukkan tinggi balok: "))
        keliling = 4 * (panjang + lebar + tinggi)
        print("Keliling balok:", keliling)
    elif pilihan_balok == 2:
        panjang = int(input("Masukkan panjang balok: "))
        lebar = int(input("Masukkan lebar balok: "))
        tinggi = int(input("Masukkan tinggi balok: "))
        luas = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))
        print("Luas permukaan balok:", luas)
    elif pilihan_balok == 3:
        panjang = int(input("Masukkan panjang balok: "))
        lebar = int(input("Masukkan lebar balok: "))
        tinggi = int(input("Masukkan tinggi balok: "))
        volume = panjang * lebar * tinggi
        print("Volume balok:", volume)
    else:
        print("Pilihan tidak ada")

else:
    print("Pilihan tidak ada")