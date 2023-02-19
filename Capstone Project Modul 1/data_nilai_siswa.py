listSiswa =[
    {
    'NIM' : 'A001',
    'Name' : 'Soekarno',
    'Gender' : 'Male',
    'Bahasa' : 70,
    'Math' : 90,
    'Fisika' : 65,
    },
    {
    'NIM' : 'A002',
    'Name' : 'Kartini',
    'Gender' : 'Female',
    'Bahasa' : 80,
    'Math' : 10,
    'Fisika' : 65,
    },
    {
    'NIM' : 'A003',
    'Name' : 'Habibie',
    'Gender' : 'Male',
    'Bahasa' : 60,
    'Math' : 50,
    'Fisika' : 35,
    }
]

def mainScreen():
    print('''
====SELAMAT DATANG DI SISTEM DATABASE====
\t    SMAN 1 MOJOKERTO\t

List menu:
1. Menampilkan Data Siswa
2. Menambahkan Data Siswa Baru
3. Mengubah Data Siswa
4. Menghapus Data Siswa
5. Keluar
''')

def findNim(list): # untuk mengecek apakah nim ada di dalam list data
    nim = (input('\nMasukan NIM Siswa: ')).upper()
    i = 0
    for i in range(len(list)): 
        if nim in list[i].values():
            return True, i, nim
    else:
        return False, i, nim

# FUNCTION UNTUK MENGHITUNG RATA2 NILAI SISWA
def avg(l1, i):
    index = list(l1[i].values()) # Untuk mengubah type file dict ke list
    rata2 = round(float(index[3] + index[4] + index [5])/3, 2) #Untuk menambahkan index 3,4,dan 5 dari list u/ mendapatkan rata nila siswa
    return rata2

# FUNCTION TO READ DATA
def show(list): # untuk menampilkan seluruh data yang ada
    print('\n\t\tDATABASE SISWA SMAN 1 MOJOKERTO\n')
    print('NIM\t|Name\t\t|Gender\t|Bahasa\t|Math\t|Fisika\t|Rata-Rata') # Nama Kolom
    for i in range(len(list)):
        print(f'{list[i]["NIM"]}\t|{list[i]["Name"]:<10}\t|{list[i]["Gender"]}\t|{list[i]["Bahasa"]}\t|{list[i]["Math"]}\t|{list[i]["Fisika"]}\t|{avg(list, i)}')

def subshow(list, index): # untuk menampilkan data siswa tertentu
    print('\nDATA SISWA==========================\n') 
    print('NIM\t|Name\t\t|Gender\t|Bahasa\t|Math\t|Fisika\t|Rata-Rata')
    print(f'{list[index]["NIM"]}\t|{list[index]["Name"]:<10}\t|{list[index]["Gender"]}\t|{list[index]["Bahasa"]}\t|{list[index]["Math"]}\t|{list[index]["Fisika"]}\t|{avg(list, index)}')

def read_data(list): 
    while True:
        print('''
==========PILIH MENU================

List menu:
1. Menampilkan Seluruh Data Siswa
2. Menampilkan Data Siswa Tertentu
3. Kembali Ke Menu Utama
    ''')
        menuNumber = int(input('Masukan Pilihan Menu: '))

        # OPSI 1 untuk menampilkan seluruh data yang ada
        if menuNumber == 1:
            show(list)

        # OPSI 2 untuk menampilkan seluruh data siswa tertentu
        elif menuNumber == 2:
            x =  findNim(list)
            if x[0] == True:
                subshow(list, x[1])
                                            
            elif x[0] != True :
                print('\nNIM Yang Anda Input Tidak Ada Di Database')  
        
        # OPSI 3 untuk kembali ke menu utama          
        elif menuNumber >= 3:
            break

# FUNCTION CREATE DATA
def add(list):
    while True:
        print('''
==========PILIH MENU================

List menu:
1. Menambahkan Data Siswa
2. Kembali Ke Menu Utama
''')
        menuNumber = int(input('Masukan Pilihan Menu: '))
        
        # OPSI 1 untuk menambahkan data
        if menuNumber == 1:
            x = findNim(list) 
            if x[0] == True:
                print('\nNIM Yang Anda Input Sudah Ada!!!\n')
                            
            elif x[0] != True:
                name = input('Masukan Nama Siswa: ').title()
                gender = input('Masukan Jenis Kelamin Siswa: ').capitalize()
                nilaiBahasa = int(input('Masukan Nilai Bahasa: '))
                nilaiMath = int(input('Masukan Nilai Math: '))
                nilaFisika = int(input('Masukan Nilai Fisika: '))
                simpanData = input('Apakah anda ingin menyimpan data Y/N: ').upper()
                if simpanData == 'Y' :
                    list.append(
                        {
                            'NIM' : x[2],
                            'Name' : name,
                            'Gender' : gender,
                            'Bahasa' : nilaiBahasa,
                            'Math' : nilaiMath,
                            'Fisika' : nilaFisika
                        })
                    print('\nData Sudah Ditambahkan Ke Database')
                    subshow(list, x[1]+1)
                    
                elif simpanData != 'Y' :
                    print('\nData Tidak Tersimpan')
        
        # OPSI 2 untuk kembali ke menu utama
        elif menuNumber >= 2:
            break      

def update(list):
    while True:
        print('''
==========PILIH MENU================

List menu:
1. Mengubah Data Siswa
2. Kembali Ke Menu Utama
''')
        menuNumber = int(input('Masukan Pilihan Menu: '))
        
        if menuNumber == 1 :
            while True:
                       
                print('''
==========PILIH MENU================

List menu:
1. Ganti NIM
2. Ganti Nama
3. Ganti Gender
4. Ganti Nilai Siswa
5. Keluar
            ''')
                kolom = int(input('Masukan Nomor Menu: '))
                                    
                if kolom == 1:
                    x = findNim(list)
                    if x[0] == True:
                        subshow(list, x[1])
                        ubahData = input('\nAnda Ingin Mengubah NIM Siswa Ini Y/N: ').upper()
                        if ubahData == 'Y':
                            print('\nMasukan NIM Siswa Yang Baru')  
                            y = findNim(list)
                            if y[0] == True:
                                print('\nNIM Yang Anda Input Sudah Ada Didatabase')
                                    
                            elif y[0] != True: 
                                list[x[1]].update({'NIM':y[2]})
                                print(f'\nNIM Siswa {list[x[1]]["Name"]} Sudah Diubah Menjadi {y[2]}')
                                subshow(list, x[1])
                        
                        elif ubahData != 'Y':
                            print('\nData Tidak Diubah')
                                                                
                    elif x[0] != True:
                        print('\nNIM Yang Anda Input Tidak Ada Didatabase')
                                                 
                elif kolom == 2:
                    x = findNim(list)
                    if x[0] == True:
                        subshow(list, x[1])
                        ubahData = input('\nAnda Ingin Mengubah Nama Siswa Ini Y/N: ').upper()
                        if ubahData == 'Y':
                            name = input('\nMasukan Nama Baru Siswa: ').title()
                            list[x[1]].update({'Name':name})
                            print(f'\nNama Siswa {list[x[1]]["NIM"]} Sudah DiUbah ')
                            subshow(list, x[1])
                        
                        elif ubahData != 'Y':
                            print('\nData Tidak Diubah')
                                               
                    elif x[0] != True:  
                        print('\nNIM Yang Anda Input Tidak Ada Di Database')
                
                elif kolom == 3:
                    x = findNim(list)
                    if x[0] == True:
                        subshow(list, x[1])
                        ubahData = input('\nAnda Ingin Mengubah Gender Siswa Ini Y/N: ').upper()
                        if ubahData == 'Y':  
                            gender = input('\nMasukan Gender Baru Siswa: ').title()
                            list[x[1]].update({'Gender':gender})
                            print(f'\nGender Siswa {list[x[1]]["NIM"]} Sudah DiUbah ')
                            subshow(list, x[1])
                        
                        elif ubahData != 'Y':
                            print('\nData Tidak Diubah')
                    
                    elif x[0] != True:    
                        print('\nNIM Yang Anda Input Tidak Ada Di Database')
                        
                elif kolom == 4 :
                    x = findNim(list)
                    if x[0] == True:
                        subshow(list, x[1]) 
                        ubahData = input('\nAnda Ingin Mengubah Nilai Siswa Ini Y/N: ').upper()
                        if ubahData == 'Y':   
                            nilaiBahasa = int(input('Masukan Nilai Bahasa: '))
                            nilaiMath = int(input('Masukan Nilai Math: ')) 
                            nilaiFisika = int(input('Masukan Nilai Fisika: '))
                            list[x[1]].update(
                        {
                            'Bahasa' : nilaiBahasa,
                            'Math' : nilaiMath,
                            'Fisika' : nilaiFisika
                        })
                            print(f'\nData Nilai Siswa {list[x[1]]["NIM"]} Sudah Diubah')
                            subshow(list, x[1])

                        elif ubahData != 'Y':
                            print('\nData Tidak Diubah')
                                          
                    elif x[0] != True:    
                        print('\nNIM Yang Anda Input Tidak Ada Di Database')
                          
                elif kolom >= 5:
                    break
        
        # OPSI 2 kembali ke menu utama
        elif menuNumber >= 2 :
            break

# FUNCTION DELETE DATA        
def delete(list):
    while True:
        print('''
==========PILIH MENU================

List menu:
1. Menghapus Data Siswa
2. Kembali Ke Menu Utama
''')
        menuNumber = int(input('Masukan Pilihan Menu: '))
        
        # OPSI 1 mengjapus Data Siswa
        if menuNumber == 1:
            x = findNim(list)
            if x[0] == True:
                subshow(list, x[1])
                hapusData = input('\nApakah anda ingin menghapus data Y/N: ').upper()
                if hapusData == 'Y':
                    del list[x[1]]
                    print('\nData Berhasil Dihapus')
                    
                elif hapusData != 'Y':
                    print('\nData Tidak Dihapus')
            
            else:
                print('\nNIM Yang Anda Masukan Tidak Ada')

        # OPSI 2 Kembali Ke Menu Utama       
        elif menuNumber >= 2:
            break

# LAYAR MENU UTAMA
while True:
    mainScreen()
    
    menuNumber = int(input('Masukan Nomor Menu: '))

    if menuNumber == 1: 
        read_data(listSiswa)
       
    elif menuNumber == 2:
        add(listSiswa)

    elif menuNumber == 3:
        update(listSiswa)

    elif menuNumber == 4:
        delete(listSiswa)

    elif menuNumber > 5:
        print('Menu Tidak Ada. Silahkan Masukan Nomor Yang Sesuai.')

    else:
        break
