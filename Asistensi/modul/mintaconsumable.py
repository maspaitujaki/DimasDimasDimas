def cek_user_masih_meminjam(id_peminjam,id_gadget):
    # Mengecek apakah user sedang meminjam gadget 
    # True jika iya
    for baris in data_gadget_borrow_history_global :
        if baris[1] == id_peminjam and baris[2] == id_gadget and baris[5] == 'false' :
            return True
    return False

def modify_nilai(pencari,kolom_pencari,kolom_dicari,value,array_data):
    for lines in array_data:
        if (lines[kolom_pencari] == pencari):
            lines[kolom_dicari] = value
    return

def minta_consumable():
    input_id_item = input("Masukan ID Item:")
    input_jumlah_pinjam = int(input("Jumlah peminjaman:"))
    input_tanggal_pinjam = input("Tanggal peminjaman:")

    if cek(input_id_item,data_consumable_global,0) and validasi_tanggal(input_tanggal_pinjam):

        jumlah_consumable = ayo_ambil_sebagian(data_consumable_global, input_id_item, 0, 3)
        nama_consumable = ayo_ambil_sebagian(data_consumable_global, input_id_item, 0, 1)
        id_peminjam = ayo_ambil_sebagian(data_pengguna_global, username, 1, 0)

        if(jumlah_consumable < input_jumlah_pinjam):
            print("Item tidak ada")
        else: # memenuhi
            jumlah_akhir = jumlah_consumable - input_jumlah_pinjam
            modify_nilai(input_id_item,0,3,jumlah_akhir,data_consumable_global)
            if data_consumable_history_global == []:
                data_consumable_history_global.append([0,id_peminjam,input_id_item,input_tanggal_pinjam,input_jumlah_pinjam])
            else:
                id = data_consumable_history_global[-1][0] + 1
                data_consumable_history_global.append([id,id_peminjam,input_id_item,input_tanggal_pinjam,input_jumlah_pinjam])                    
            
            print("Item "+ str(nama_gadget)+" (x" + str(input_jumlah_pinjam) + ") berhasil dipinjam!")
        
    else:
        if (cek(input_id_item,data_consumable_global,0)==False) and (validasi_tanggal(input_tanggal_pinjam) == True):
            print("Tidak ada item dengan ID tersebut!")
        elif (cek(input_id_item,data_consumable_global,0)==True) and (validasi_tanggal(input_tanggal_pinjam) == False):
            print("Tanggal tidak sesuai")
        else:
            print("ID item dan tanggal peminjaman tidak sesuai")