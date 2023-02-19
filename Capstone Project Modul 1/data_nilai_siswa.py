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
3. Menghapus Data Siswa
4. Mengubah Data Siswa
5. Keluar
''')

# FUNCTION UNTUK MENGHITUNG RATA2 NILAI SISWA
def avg(l1, i):
    index = list(l1[i].values())
    rata2 = round(float(index[3] + index[4] + index [5])/3, 2)
    return rata2

# FUNCTION TO READ DATA
def show(list):
    print('\n\t\tDATABASE SISWA SMAN 1 MOJOKERTO\n')
    print('NIM\t|Name\t\t|Gender\t|Bahasa\t|Math\t|Fisika\t|Rata-Rata')
    for i in range(len(list)):
        print(f'{list[i]["NIM"]}\t|{list[i]["Name"]:<10}\t|{list[i]["Gender"]}\t|{list[i]["Bahasa"]}\t|{list[i]["Math"]}\t|{list[i]["Fisika"]}\t|{avg(list, i)}')

def subshow(list, index):
    print('\nDATA SISWA\n')
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

        # OPSI 1
        if menuNumber == 1:
            show(list)

        # OPSI 2
        elif menuNumber == 2:
            nim = (input('\nMasukan NIM Siswa: ')).upper()
            i = 0
            for i in range(len(list)):
                if nim in list[i].values():
                    subshow(list, i)
                    break
                i += 1
                    
            else:
                print('\nNIM Yang Anda Input Tidak Ada Di Database')  
        
        # OPSI 3            
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
        
        # OPSI 1
        if menuNumber == 1:
            nim = input('Masukan NIM Siswa: ').upper()
            i = 0
            while i < len(list):
                if nim in list[i].values():
                    print('\nNIM Yang Anda Input Sudah Ada!!!\n')
                    break
                i += 1

            else:
                name = input('Masukan Nama Siswa: ').title()
                gender = input('Masukan Jenis Kelamin Siswa: ').capitalize()
                nilaiBahasa = int(input('Masukan Nilai Bahasa: '))
                nilaiMath = int(input('Masukan Nilai Math: '))
                nilaFisika = int(input('Masukan Nilai Fisika: '))
                simpanData = input('Apakah anda ingin menyimpan data Y/N: ').upper()
                if simpanData == 'Y' :
                    list.append(
                        {
                            'NIM' : nim,
                            'Name' : name,
                            'Gender' : gender,
                            'Bahasa' : nilaiBahasa,
                            'Math' : nilaiMath,
                            'Fisika' : nilaFisika
                        })
                    print('\nData Sudah Ditambahkan Ke Database\n')
                    
                elif simpanData != 'Y' :
                    print('\nData Tidak Tersimpan\n')
        
        # OPSI 2  
        elif menuNumber >= 2:
            break      
       
# FUNCTION UPDATE DATA
def update(list):
    while True:
        print('''
==========PILIH MENU================

List menu:
1. Mengubah Seluruh Data Siswa
2. Mengubah Data Tertentu
3. Kembali Ke Menu Utama
''')
        menuNumber = int(input('Masukan Pilihan Menu: '))
        
        # OPSI 1
        if menuNumber == 1:
            nim = input('\nMasukan NIM Siswa: ').upper()
            i = 0
            while i < len(list):
                if nim in list[i].values():
                    subshow(list, i)  
                    print('\nMasukan Data Siswa Yang Baru')                 
                    name = input('Masukan Nama Siswa: ').title()
                    gender = input('Masukan Jenis Kelamin Siswa: ').capitalize()
                    nilaiBahasa = int(input('Masukan Nilai Bahasa: '))
                    nilaiMath = int(input('Masukan Nilai Math: ')) 
                    nilaiFisika = int(input('Masukan Nilai Fisika: '))  
                    list[i].update(
                    {
                        'Name' : name,
                        'Gender' : gender,
                        'Bahasa' : nilaiBahasa,
                        'Math' : nilaiMath,
                        'Fisika' : nilaiFisika
                    })
                    print(f'\nData Siswa {list[i]["NIM"]} {list[i]["Name"]} Sudah Terupdate')
                    subshow(list, i) 
                    break
                i+= 1

            else :
                print('\nData Yang Anda Cari Tidak Ada')

        # OPSI 2
        elif menuNumber == 2 :
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
                    nim = input('\nMasukan NIM Siswa: ').upper()
                    i = 0
                    while i < len(list):
                        if nim in list[i].values():
                            subshow(list, i)  
                            nim2 = input('Masukan NIM Baru Siswa: ').title()
                            x = 0
                            while x < len(list):
                                if nim2 in list[x].values():
                                    print('\nNIM Yang Anda Input Sudah Ada Didatabase')
                                    break
                                x += 1
                                    
                            else : 
                                list[i].update({'NIM':nim2})
                                print(f'\nData NIM Siswa {list[i]["Name"]} Sudah Diubah Menjadi {nim2}')
                                break 
                            break  
                        i += 1
            
                    else:
                        print('\nNIM Yang Anda Input Tidak Ada Didatabase')
                                                 
                elif kolom == 2:
                    nim = input('\nMasukan NIM Siswa: ').upper()
                    i = 0
                    while i < len(list):
                        if nim in list[i].values():
                            subshow(list, i)  
                            name = input('\nMasukan Nama Baru Siswa: ').title()
                            list[i].update({'Name':name})
                            print(f'\nNama Siswa {list[i]["NIM"]} Sudah Diubah Menjadi {name} ')
                            break
                        i += 1

                    else:  
                        print('\nNIM Yang Anda Input Tidak Ada Di Database')
                
                elif kolom == 3:
                    nim = input('\nMasukan NIM Siswa: ').upper()
                    i = 0
                    while i < len(list):
                        if nim in list[i].values():
                            subshow(list, i)  
                            gender = input('\nMasukan Gender Baru Siswa: ').title()
                            list[i].update({'Gender':gender})
                            print(f'\nGender Siswa {list[i]["NIM"]} Sudah Diubah Menjadi {gender} ')
                            break  
                        i += 1

                    else:  
                        print('\nNIM Yang Anda Input Tidak Ada Di Database')
                        
                elif kolom == 4 :
                    nim = input('\nMasukan NIM Siswa: ').upper()
                    i = 0
                    while i < len(list):
                        if nim in list[i].values():
                            subshow(list, i)  
                            nilaiBahasa = int(input('Masukan Nilai Bahasa: '))
                            nilaiMath = int(input('Masukan Nilai Math: ')) 
                            nilaiFisika = int(input('Masukan Nilai Fisika: '))
                            list[i].update(
                        {
                            'Bahasa' : nilaiBahasa,
                            'Math' : nilaiMath,
                            'Fisika' : nilaiFisika
                        })
                            print(f'\nData Nilai Siswa {nim} Sudah Tersimpan')
                            break
                        i += 1

                    else:
                        print('\nNIM Yang Anda Input Tidak Ada Di Database')
                          
                elif kolom >= 5:
                    break
        
        # OPSI 3
        elif menuNumber >= 3 :
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
        
        # OPSI 1
        if menuNumber == 1:
            nim = input('Masukan NIM Siswa Yang Ingin Dihapus: ').upper()
            i = 0
            while i < len(list):
                if nim in list[i].values():
                    subshow(list, i)
                    hapusData = input('Apakah anda ingin menghapus data Y/N: ').upper()
                    if hapusData == 'Y':
                        del list[i]
                        print('\nData Berhasil Dihapus')
                        break
                    elif hapusData != 'Y':
                        break
                i += 1

            else:
                print('\nNIM Yang Anda Masukan Tidak Ada')

        # OPSI 2            
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
        delete(listSiswa)

    elif menuNumber == 4:
        update(listSiswa)

    elif menuNumber > 5:
        print('Menu Tidak Ada. Silahkan Masukan Nomor Yang Sesuai.')

    else:
        break
