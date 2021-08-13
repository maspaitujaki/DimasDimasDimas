def id_to_name_gadget(id_gadget):
    # mereturn nama gadget dengan id gadget tertentu
    return ayo_ambil_sebagian(data_gadget_global,id_gadget,0,1)

# def ayo_ambil_sebagian():
# def 


def kembalikan_gadget():
    id_peminjam = ayo_ambil_sebagian(data_pengguna_global, username, 1, 0)

    data_pinjam = []
    for baris in data_gadget_borrow_history_global:
        if (baris[1] == id_peminjam) and (baris[5] == 'false'):
            data_pinjam.append(baris)

    if data_pinjam != []:

        for i in range (len(data_pinjam)):
        print(i+1,". ",id_to_name_gadget(data_pinjam[i][2]))

        nomor_pinjam = int(input("Masukkan nomor peminjaman:"))
        tanggal_pengembalian = input("Tanggal pengembalian:")

        if ( 1<= nomor_pinjam <= len(data_pinjam) and validasi_tanggal(tanggal_pengembalian) ):
            indeks_data_pinjam = nomor_pinjam - 1 
            id_gadget_kembali = data_pinjam[indeks_data_pinjam][2] # id gadget yang ingin dikembalikan
            jumlah_gadget_kembali = data_pinjam[indeks_data_pinjam][4] # jumlah gadget yang ingin dikembalikan


            # Mengembalikan gadget yang dipinjam
            jumlah_gadget_sebelum = ayo_ambil_sebagian(data_gadget_global,id_gadget_kembali,0,3)
            jumlah_gadget = jumlah_gadget_sebelum + jumlah_gadget_kembali
            modify_nilai(id_gadget_kembali,0,3,jumlah_gadget,data_gadget_global)

            id_riwayat_peminjaman = data_pinjam[indeks_data_pinjam][0]

            # Untuk gadget borrow history
            for baris in data_gadget_borrow_history_global:
                if (baris[0] == id_riwayat_peminjaman):
                    baris[5] = 'true'
    
            # Untuk gadget return history
            if data_gadget_return_history_global == []:
                data_gadget_return_history_global.append([0,id_riwayat_peminjaman,tanggal_pengembalian])
            else:
                id = data_gadget_return_history_global[-1][0] + 1
                data_gadget_return_history_global.append([id,id_riwayat_peminjaman,tanggal_pengembalian])

            print("Item " + id_to_name_gadget(id_gadget_kembali) + " (x" + str(jumlah_gadget_kembali) + ") telah dikembalikan")
        
        else:
            if (nomor_pinjam < 1 or nomor_pinjam > len(data_pinjam)) and (validasi_tanggal(tanggal_pengembalian) == True):
                print("Nomor peminjaman tidak valid")
            elif (1<= nomor_pinjam <= len(data_pinjam)) and (validasi_tanggal(tanggal_pengembalian) == False):
                print("Tanggal tidak sesuai")
            else:
                print("Nomor peminjaman dan tanggal peminjaman tidak sesuai")

    else: # data_gadget == []
        print("Tidak ada gadget yang sedang dipinjam")


def User_exist(username):
    for i in range(len(data_user)):
        if(data_user[i][1])==username:
            return True
    return False
    
    
    
