print("~~~~~ Tabel Matematika Nich ~~~~~")
print("Pilihan Model Maatematika")
print("1. Perkalian")
print("2. Pembagian")
    
p = int(input("Masukkan model matematika yang diinginkan 1/2 : "))

k = int(input("Menampilkan table matematika dari angka: "))

if p == 1:
    for i in range(1,11):
        print(f'{k} x {i} = {k*i}')
elif p == 2:
    for i in range(50,66):
        print(f'{i} : {k} = {i/k}')
else:
    print("Pilihan tiidak tersedia, jangan ngasal!")