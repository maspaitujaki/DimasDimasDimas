def modify_nilai(pencari,kolom_pencari,kolom_dicari,value,array_data):
    for lines in array_data:
        if (lines[kolom_pencari] == pencari):
            lines[kolom_dicari] = value
    return

def ayo_ambil_sebagian(array_data, pencari, kolom_pencari, kolom_dicari):
    '''
        I.S array_data : list
            pencari : bebas
            kolom_pencari : indeks kolom yang akan dilihat isinya
            kolom_dicari : 
        O.S list
        Jika fungsi sebelumnya mengembalikan satu baris entri, fungsi ini hanya mengembalikan isi dari kolom tertentu
    '''
    for line in array_data: 
        if line[kolom_pencari] == pencari:
            return line[kolom_dicari]
    return 

def cek(entri,data,kolom):
    """
        I.S entri : tipe bebas
            data  : array
            kolom : integer
        O.S Boolean
        Fungsi ini bertujuan untuk mencari apakah terdapat 'entri' pada 'data' di 'kolom' tertentu.
        Contoh nya: Data user memiliki kolom username yang berindex 1. Pemanggilan fungsi cek(dimas, data_pengguna_global, 1)
        akan mencari apakah username 'dimas' ada pada kolom username pada data_pengguna_global. Jika ada maka akan mengembalikan True
        dan jika tidak akan mengembalikan False
    """
    for baris in data:
        if baris[kolom] == entri:
            return True
    return False

def id_to_name_consum(iD):
    return ayo_ambil_sebagian(data_consumable_global,iD,0,1)


def minta():
    from datetime import datetime
    
    minta_iD = input('Masukkan ID item :')
    while not cek(minta_iD, data_consumable_global, 0) : #validasi apakah id ada
        print('Input tidak valid atau ID consumable tidak terdaftar')
        minta_iD = input('Masukkan ID item :')

    jumlah_asli = ayo_ambil_sebagian(data_consumable_global, minta_iD, 0, 3)
    
    if jumlah_asli == 0:
        print('Item sudah habis! Maaf')
        return #fungsi berhenti
    else:
        minta_jumlah = input('Jumlah :') 
        while True:
            try:
                minta_jumlah = int(minta_jumlah)
                break #validasi masukan jumlah
            except:
                print('Masukkan harus berupa integer!')
                print()
                minta_jumlah = input('Jumlah :')
        
        if jumlah_asli < minta_jumlah:
            print('Jumlah yang diminta terlalu banyak, hanya ada sisa {} buah di kantung.'.format(jumlah_asli))
            print()
            return # jika jumlah kurang maka akan keluar
        else:
            minta_tanggal = input('Tanggal permintaan :')
            format_tanggal = '%d/%m/%Y'
            while True:
                try:
                    datetime.strptime(minta_tanggal, format_tanggal)
                    break #validasi tanggal
                except:
                    print('Format tanggal tidak sesuai. harus dd/mm/yyyy')
                    print()
                    minta_tanggal = input('Tanggal permintaan:')
            
            # di titik ini semua masukan sudah tervalidasi maka selanjutnya adalah
            # membuat entri baru pada histori pengambilan
            # kita punya:
            # minta_iD
            # minta_jumlah
            # minta_tanggal
            id_peminta = active_person[0] # active person merupakan variabel global dari main yang berisikan 
                                          # data orang yang sedang login
            if data_consumable_history_global == []:
                data_consumable_history_global.append([0,id_peminta,minta_iD,minta_tanggal,minta_jumlah])
            else:
                id_baru = data_consumable_history_global[-1][0] + 1
                data_consumable_history_global.append([id_baru,id_peminta,minta_iD,minta_tanggal,minta_jumlah])

            # saatnya mengubah data consumable
            jumlah_baru = jumlah_asli - minta_jumlah
            modify_nilai(minta_iD, 0, 3, jumlah_baru, data_consumable_global)
            print("Item {} (x{}) telah berhasil diambil!".format(id_to_name_consum(minta_iD), minta_jumlah))
            print(data_consumable_history_global)