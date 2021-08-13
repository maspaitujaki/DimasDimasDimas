def ayo_ambil_sebagian(array_data, pencari, kolom_pencari, kolom_dicari):
    for line in array_data: 
        if line[kolom_pencari] == pencari:
            return line[kolom_dicari]
    return 


def id_to_name_gadget(iD):
    return ayo_ambil_sebagian(data_gadget_global,iD,0,1)

def id_to_name_consum(iD):
    return ayo_ambil_sebagian(data_consumable_global,iD,0,1)

def id_to_name_user(iD):
    return ayo_ambil_sebagian(data_pengguna_global,int(iD),0,2)
    
def idPinjam_to_nama_gadget_id(iD):
    nama_peminjam = ayo_ambil_sebagian(data_gadget_borrow_history_global, iD, 0, 1)
    nama_gadget = ayo_ambil_sebagian(data_gadget_borrow_history_global, iD, 0, 2)

    return nama_peminjam, nama_gadget

def lihat_history_return():
    from datetime import datetime
    
    all_dates = []

    for entry in data_gadget_return_history_global:
        if entry[2] in all_dates:
            pass
        else:
            all_dates.append(entry[2])
    
    print(all_dates)
    all_dates.sort(key = lambda date: datetime.strptime(date, '%d/%m/%Y'))
    
    

    data_gadget_return_history_global_sorted = []
    for date in all_dates:
        for entry in data_gadget_return_history_global:
            if entry[2] == date : data_gadget_return_history_global_sorted.append(entry)

    banyak_entri = len(data_gadget_return_history_global_sorted)    


    while banyak_entri > 0:
        if banyak_entri <= 5 :
            for i in range(banyak_entri-1,-1,-1):
                useriD, gadgetiD = idPinjam_to_nama_gadget_id(data_gadget_return_history_global_sorted[i][1])
                print('ID Pengembalian        : {}'.format(data_gadget_return_history_global_sorted[i][0]))
                print('Nama Pengambil         : {}'.format(id_to_name_user(int(useriD))))
                print('Nama Gadget            : {}'.format(id_to_name_gadget(gadgetiD)))
                print('Tanggal Pengembalian   : {}'.format(data_gadget_return_history_global_sorted[i][2]))
                print()
            break 
        else:
            for i in range(banyak_entri-1,banyak_entri-6,-1):
                useriD, gadgetiD = idPinjam_to_nama_gadget_id(data_gadget_return_history_global_sorted[i][1])
                print('ID Pengembalian        : {}'.format(data_gadget_return_history_global_sorted[i][0]))
                print('Nama Pengambil         : {}'.format(id_to_name_user(int(useriD))))
                print('Nama Gadget            : {}'.format(id_to_name_gadget(gadgetiD)))
                print('Tanggal Pengembalian   : {}'.format(data_gadget_return_history_global_sorted[i][2]))
                print()
            banyak_entri -= 5

            masukan = input('Tampilkan yang lain?(Y/N')
            while not masukan in ['Y','y','N','n']:
                print('Masukkan tidak valid')
                masukan = input('Tampilkan yang lain?(Y/N')
                    
            if masukan.lower() == 'y':continue
            else: break

def lihat_history_borrow():
    from datetime import datetime
    

    all_dates = []

    for entry in data_gadget_borrow_history_global: # untuk setiap baris pada data borrow histori
        if entry[3] in all_dates: # jika kolom tanggal pada baris sudah ada di list all_dates
            pass
        else:
            all_dates.append(entry[3])

    all_dates.sort(key = lambda date: datetime.strptime(date, '%d/%m/%Y'))
    
    

    data_gadget_borrow_history_global_sorted = []
    for date in all_dates:
        for entry in data_gadget_borrow_history_global:
            if entry[3] == date : data_gadget_borrow_history_global_sorted.append(entry)

    banyak_entri = len(data_gadget_borrow_history_global_sorted)    


    while banyak_entri > 0:
        
        if banyak_entri <= 5 :
            for i in range(banyak_entri-1,-1,-1):

                print('ID Peminjaman        : {}'.format(data_gadget_borrow_history_global_sorted[i][0]))
                print('Nama Pengambil       : {}'.format(id_to_name_user(data_gadget_borrow_history_global_sorted[i][1])))
                print('Nama Gadget          : {}'.format(id_to_name_gadget(data_gadget_borrow_history_global_sorted[i][2])))
                print('Tanggal peminjaman   : {}'.format(data_gadget_borrow_history_global_sorted[i][3]))
                print('Jumlah               : {}'.format(data_gadget_borrow_history_global_sorted[i][4]))
                print()
            break
        else:
            for i in range(banyak_entri-1,banyak_entri-6,-1):

                print('ID Peminjaman        : {}'.format(data_gadget_borrow_history_global_sorted[i][0]))
                print('Nama Pengambil       : {}'.format(id_to_name_user(data_gadget_borrow_history_global_sorted[i][1])))
                print('Nama Gadget          : {}'.format(id_to_name_gadget(data_gadget_borrow_history_global_sorted[i][2])))
                print('Tanggal peminjaman   : {}'.format(data_gadget_borrow_history_global_sorted[i][3]))
                print('Jumlah               : {}'.format(data_gadget_borrow_history_global_sorted[i][4]))
                print()
            banyak_entri -= 5

            masukan = input('Tampilkan yang lain?(Y/N')
            while not masukan in ['Y','y','N','n']:
                print('Masukkan tidak valid')
                masukan = input('Tampilkan yang lain?(Y/N')
                    
            if masukan.lower() == 'y':continue
            else: break
    
    # OPSI 2
    # banyak_entri = len(data_gadget_borrow_history_global_sorted)
    # data_gadget_borrow_history_global_sorted.reverse()
    # for index in range(1, banyak_entri + 1):
        
    #     print('ID Peminjaman        : {}'.format(data_gadget_borrow_history_global_sorted[index-1][0]))
    #     print('Nama Pengambil       : {}'.format(id_to_name_user(data_gadget_borrow_history_global_sorted[index-1][1])))
    #     print('Nama Gadget          : {}'.format(id_to_name_gadget(data_gadget_borrow_history_global_sorted[index-1][2])))
    #     print('Tanggal peminjaman   : {}'.format(data_gadget_borrow_history_global_sorted[index-1][3]))
    #     print('Jumlah               : {}'.format(data_gadget_borrow_history_global_sorted[index-1][4]))
    #     print()
                
    #     if index % 5 == 0 :
    #         if input('Tampilkan yang lain?(Y/N)').lower() == 'y': 
    #             print() 
    #             continue        
    #         else: break

def lihat_history_consum():
    from datetime import datetime
    

    all_dates = []

    for entry in data_consumable_history_global:
        if entry[3] in all_dates:
            pass
        else:
            all_dates.append(entry[3])
    
    print(all_dates)
    all_dates.sort(key = lambda date: datetime.strptime(date, '%d/%m/%Y'))
    
    

    data_consumable_history_global_sorted = []
    for date in all_dates:
        for entry in data_consumable_history_global:
            if entry[3] == date : data_consumable_history_global_sorted.append(entry)

    banyak_entri = len(data_consumable_history_global_sorted)    


    while banyak_entri > 0:

        
        if banyak_entri <= 5 :
            for i in range(banyak_entri-1,-1,-1):
                print('ID Pengambilan       : {}'.format(data_consumable_history_global_sorted[i][0]))
                print('Nama Pengambil       : {}'.format(id_to_name_user(int(data_consumable_history_global_sorted[i][1]))))
                print('Nama Consumable      : {}'.format(id_to_name_consum(data_consumable_history_global_sorted[i][2])))
                print('Tanggal Pengambilan  : {}'.format(data_consumable_history_global_sorted[i][3]))
                print('Jumlah               : {}'.format(data_consumable_history_global_sorted[i][4]))
                print()
            break
        else:
            for i in range(banyak_entri-1,banyak_entri-6,-1):
                print('ID Pengambilan       : {}'.format(data_consumable_history_global_sorted[i][0]))
                print('Nama Pengambil       : {}'.format(id_to_name_user(int(data_consumable_history_global_sorted[i][1]))))
                print('Nama Consumable      : {}'.format(id_to_name_consum(data_consumable_history_global_sorted[i][2])))
                print('Tanggal Pengambilan  : {}'.format(data_consumable_history_global_sorted[i][3]))
                print('Jumlah               : {}'.format(data_consumable_history_global_sorted[i][4]))
                print()
            banyak_entri -= 5

            masukan = input('Tampilkan yang lain?(Y/N')
            while not masukan in ['Y','y','N','n']:
                print('Masukkan tidak valid')
                masukan = input('Tampilkan yang lain?(Y/N')
                    
            if masukan.lower() == 'y':continue
            else: break