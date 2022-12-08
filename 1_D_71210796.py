masukUang = int(input("Masukkan jumlah uang: Rp"))
mulaiBeli = str(input("Ketik 'START' untuk memulai: "))

barangJual = ["susu", "permen", "roti", "indomie", "vitamin"]

susu = 20000
permen = 500
roti = 15000
indomie = 3000
vitamin = 50000

if mulaiBeli.lower() == 'start':

    while True:
        tanya = str(input("Apa barang yang akan Anda beli? "))
        if tanya.lower() =='susu':
            if masukUang >= susu:
                masukUang -= susu
                print("Sisa uang Anda", masukUang)
            else:
                print("Uang anda tidak cukup")

        elif tanya.lower() =='permen':
            if masukUang >= permen:
                masukUang -= permen
                print("Sisa uang Anda", masukUang)
            else:
                print("Uang anda tidak cukup")

        elif tanya.lower() =='roti':
            if masukUang >= roti:
                masukUang -= roti
                print("Sisa uang Anda", masukUang)
            else:
                print("Uang anda tidak cukup")

        elif tanya.lower() =='indomie':
            if masukUang >= indomie:
                masukUang -= indomie
                print("Sisa uang Anda", masukUang)
            else:
                print("Uang anda tidak cukup")

        elif tanya.lower() =='vitamin':
            if masukUang >= vitamin:
                masukUang -= vitamin
                print("Sisa uang Anda", masukUang)
            else:
                print("Uang anda tidak cukup")

        elif tanya.lower() == 'sudah':
            break

        else:
            print("Barang tidak tersedia")