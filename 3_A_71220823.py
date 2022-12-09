b = int(input('Masukkan Pembatas: '))
a = int(input('Masukkan Angka yang dilarang: '))
for i in range(b):
    if i == a:
        continue
    print(i,end=" ")
