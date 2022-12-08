masukUang = int(input("Masukkan jumlah uang: Rp"))
mulaiBeli = str(input("Ketik 'START' untuk memulai: "))

barangJual = ["susu", "permen", "roti", "indomie", "vitamin"]

susu = 20000
permen = 500
roti = 15000
indomie = 3000
vitamin = 50000

tanya = str(input("Apa barang yang akan Anda beli? "))

mb = str.lower(mulaiBeli)

if start.lower() == 'start':
    while True:
        beli = input('beli? ')

        if beli.lower() =='susu':
            if uangAwal >= susu:
                uangAwal -= susu
                print("Sisa uang anda"+ str(masukUang-susu))
            else:
                print("Uang anda tidak cukup")

        elif beli.lower() =='permen':
            if uangAwal >= permen:
                uangAwal -= permen
                print("Sisa uang anda"+ str(masukUang-permen))
            else:
                print("Uang anda tidak cukup")

        elif beli.lower() =='roti':
            if uangAwal >= roti:
                uangAwal -= roti
                print("Sisa uang anda"+ str(masukUang-roti))
            else:
                print("Uang anda tidak cukup")

        elif beli.lower() =='indomie':
            if uangAwal >= indomie:
                uangAwal -= indomie
                print("Sisa uang anda"+ str(masukUang-indomie))
            else:
                print("Uang anda tidak cukup")

        elif beli.lower() =='vitamin':
            if uangAwal >= vitamin:
                uangAwal -= vitamin
                print("Sisa uang anda"+ str(masukUang-vitamin))
            else:
                print("Uang anda tidak cukup")
        elif beli.lower() == 'sudah':
            break
    else:
        print("Barang tidak tersedia")