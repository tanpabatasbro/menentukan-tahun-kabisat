print('''Menentukan Tahun Kabisat
''')


tahun = int(input("Masukkan Tahun : "))

#Perulangan Pertama

if (tahun % 4) == 0:
 
   #Perulangan Kedua
    if (tahun % 100) == 0:
 
       #Perulangan Ketiga
        if (tahun % 400) == 0:
 
           #Tergolong Tahun Kabisat
            print(f"{tahun} adalah Tahun Kabisat")
 
       #Bukan Tergolong Tahun Kabisat
        else:
            print(f"{tahun} bukan Tahun Kabisat")
 
   #Tergolong Tahun Kabisat
    else:
        print(f"{tahun} adalah Tahun Kabisat")
 
#Bukan Tergolong Tahun Kabisat
else:
    print(f"{tahun} bukan Tahun Kabisat")
