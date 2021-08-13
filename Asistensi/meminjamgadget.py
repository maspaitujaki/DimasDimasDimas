# Ada perubahan di bagian register, aku nambahin variabel global



def modify_nilai(pencari,kolom_pencari,kolom_dicari,value,array_data):
    for lines in array_data:
        if (lines[kolom_pencari] == pencari):
            lines[kolom_dicari] = value
    return

def cek_user_masih_meminjam(id_peminjam,id_gadget):
    # Mengecek apakah user sedang meminjam gadget 
    # True jika iya
    for baris in data_gadget_borrow_history_global :
        if baris[1] == id_peminjam and baris[2] == id_gadget and baris[5] == 'false' :
            return True
    return False
    
def validasi_tanggal(tanggal):
    import datetime
    try:
        datetime.datetime.strptime(tanggal, '%d/%m/%Y')
        return True
    except:
        return False

def pinjam_gadget():
    input_id_item = input("Masukan ID: ")
    input_tanggal_pinjam = input("Tanggal peminjaman: ")
    input_jumlah_pinjam = int(input("Jumlah peminjaman: "))

    if cek(input_id_item,data_gadget_global,0) and validasi_tanggal(input_tanggal_pinjam):

        id_peminjam = ayo_ambil_sebagian(data_pengguna_global, username, 1, 0)
        nama_gadget = ayo_ambil_sebagian(data_gadget_global, input_id_item, 0, 1)
        # Mengecek apakah user sudah pernah meminjam item tsb dan belum direturn
        # Jika user belum mereturn, maka tidak bisa diproses
        if cek_user_masih_meminjam(id_peminjam,input_id_item):
            print("Item sedang dipinjam")
        else:
            jumlah_gadget = ayo_ambil_sebagian(data_gadget_global, input_id_item, 0, 3)
            if(jumlah_gadget < input_jumlah_pinjam):
                print("Item tidak bisa dipinjam")
            else: # memenuhi
                jumlah_akhir = jumlah_gadget - input_jumlah_pinjam
                modify_nilai(input_id_item,0,3,jumlah_akhir,data_gadget_global)
                if data_gadget_borrow_history_global == []:
                    data_gadget_borrow_history_global.append([0,id_peminjam,input_id_item,input_tanggal_pinjam,input_jumlah_pinjam,'false'])
                else:
                    id = data_gadget_borrow_history_global[-1][0] + 1
                    data_gadget_borrow_history_global.append([id,id_peminjam,input_id_item,input_tanggal_pinjam,input_jumlah_pinjam,'false'])
    
                print("Item "+ str(nama_gadget)+" (x" + str(input_jumlah_pinjam) + ") berhasil dipinjam!")
            
    else:
        if (cek(input_id_item,data_gadget_global,0)==False) and (validasi_tanggal(input_tanggal_pinjam) == True):
            print("Tidak ada item dengan ID tersebut!")
        elif (cek(input_id_item,data_gadget_global,0)==True) and (validasi_tanggal(input_tanggal_pinjam) == False):
            print("Tanggal tidak sesuai")
        else:
            print("ID item dan tanggal peminjaman tidak sesuai")



