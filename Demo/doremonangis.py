import argparse
import os
import time

# FUNGSI FUNGSI TAMBAHAN

def clrs():
    '''
        Berfungsi membersihkan console
    '''
    os.system('cls')

def parser(dipisah, pemisah): 
    """
        Ini adalah fungsi parser yang dapat menggantikan peran X.split(). 
        Cara penggunaannya setara dengan dipisah.split(pemisah)
    """
    split_value = []
    tmp = ''
    for c in dipisah:
        if c == pemisah:
            split_value.append(tmp)
            tmp = ''
        else:
            tmp += c
    if tmp:
        split_value.append(tmp)
    return split_value


def convert_line_to_data(line):
    """
        Berdasarkan tutorial medium
    """
    raw_array_of_data = parser(line,";")
    array_of_data = [data.strip() for data in raw_array_of_data]
    return array_of_data

def convert_array_data_to_real_values(nama_data, array_data):
    """
        Berdasarkan tutorial medium
    """
    arr_cpy = array_data[:]

    if nama_data == "user.csv":
        for i in range(5):
            if (i==0):
                arr_cpy[i] = int(arr_cpy[i])
    elif nama_data == "gadget.csv":
        for i in range(6):
            if (i==3):
                arr_cpy[i] = int(arr_cpy[i])
            elif (i==5):
                arr_cpy[i] = int(arr_cpy[i])

    elif nama_data == "consumable.csv":
        for i in range(5):
            if (i==3):
                arr_cpy[i] = int(arr_cpy[i])
    elif nama_data == "consumable_history.csv":
        for i in range(4):
            if (i == 0):
                arr_cpy[i] = int(arr_cpy[i])
            elif (i==1):
                arr_cpy[i] = int(arr_cpy[i])
            elif (i==4):
                arr_cpy[i] = int(arr_cpy[i])
    elif nama_data == "gadget_borrow_history.csv":
        for i in range(6):
            if (i==0):
                arr_cpy[i] = int(arr_cpy[i])
            if (i==1):
                arr_cpy[i] = int(arr_cpy[i])
            if (i==4):
                arr_cpy[i] = int(arr_cpy[i])
    elif nama_data == "gadget_return_history.csv":
        for i in range(3):
            if (i==0):
                arr_cpy[i] = int(arr_cpy[i])
            if (i==1):
                arr_cpy[i] = int(arr_cpy[i])

    
    
    return arr_cpy

def buka_data(nama_data):
    """
        I.S Nama file csv yang akan dipakai
        O.S Isi dari file csv dalam bentuk 2 array: 1 array header, 1 array isi csv.
        Tujuan dari dibuatnya fungsi ini adalah untuk memendekkan fitur load data atau F14
    """
    f = open("{}".format(nama_data),"r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]

    raw_header = lines.pop(0)
    header = convert_line_to_data(raw_header)
    datas = []

    for line in lines:
        array_of_data = convert_line_to_data(line)
        real_values = convert_array_data_to_real_values(nama_data, array_of_data)
        datas.append(real_values)

    return header, datas

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

def convert_datas_to_string(header, body):
    """
        Berdasarkan medium, berfungsi untuk save data
    """
    string_data = ";".join(header) + "\n"
    for arr_data in body:
        arr_data_all_string = [str(var) for var in arr_data]
        string_data += ";".join(arr_data_all_string)
        string_data += "\n"
    return string_data

def ayo_ambil_sebaris(array_data, pencari, kolom_pencari):
    '''
        I.S array_data : list
            pencari : bebas
            kolom_pencari : indeks kolom yang akan dilihat isinya
        O.S list
        Fungsi ini berfungsi untuk mereturn satu baris entri pada array_data yang memiliki kolom berisi sama dengan pencari
    '''
    for line in array_data:
        if line[kolom_pencari] == pencari:
            return line
    return

def ayo_ambil_sebagian(array_data, pencari, kolom_pencari, kolom_dicari):
    '''
        I.S array_data : list
            pencari : bebas
            kolom_pencari : indeks kolom yang akan dilihat isinya
            kolom_dicari : 
        O.S bebas
        Jika fungsi sebelumnya mengembalikan satu baris entri, fungsi ini hanya mengembalikan isi dari kolom tertentu
    '''
    for line in array_data: 
        if line[kolom_pencari] == pencari:
            return line[kolom_dicari]
    return 

def ayo_hapus_sebaris(array_data, pencari, kolom_pencari):
	"""
		Fungsi digunakan untuk menghapus 1 baris data array_data
	"""
	for line in array_data:
		if line[kolom_pencari] == pencari:
			array_data.remove(line)

def id_to_name_gadget(iD):
    '''
        Berfungsi untuk mentranslate id gadget ke nama gadget
    '''
    return ayo_ambil_sebagian(data_gadget_global,iD,0,1)

def id_to_name_consum(iD):
    return ayo_ambil_sebagian(data_consumable_global,iD,0,1)

def id_to_name_user(iD):
    return ayo_ambil_sebagian(data_pengguna_global,iD,0,2)
    
def idPinjam_to_nama_gadget_id(iD):
    nama_peminjam = ayo_ambil_sebagian(data_gadget_borrow_history_global, iD, 0, 1)
    nama_gadget = ayo_ambil_sebagian(data_gadget_borrow_history_global, iD, 0, 2)

    return nama_peminjam, nama_gadget

def modify_datas(array_data, pencari, kolom_pencari, kolom_dicari, value):
	"""
		Fungsi untuk mengubah nilai kolom tertentu pada array_data
	"""
	for line in array_data:
		if line[kolom_pencari] == pencari:
			line[kolom_dicari] = value
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

# FUNGSI FUNGSI KETENTUAN

def register():
    """
        F01
        Penerapannya cukup mirip dengan tutorial medium
        Langkah kerja:
        1. Prosedur akan menyiapkan index baru untuk pengguna baru, 
        2. Prosedur meminta nama pengguna baru
        3. Prosedur meminta username untuk pengguna baru
        4. Prosedur memvalidasi ketersediaan username
        5.1. Jika username sudah terpakai, prosedur akan meminta username lain
        5.2. Jika belum, Prosedur akan lanjut ke meminta password yang akan digunakan pengguna baru
        6. Prosedur meminta alamat pengguna baru
        7. Prosedur menyimpan data-data tadi ke sebuah array yang memiliki urutan elemen sesuai dengan user.csv
        8. Entri untuk pengguna baru dimasukkan ke array data user yang ada
        9. Prosedur memberitahu bahwa proses regristrasi telah berhasil.
    """
    
    new_user_id = data_pengguna_global[-1][0] + 1
    new_user_nama = input("Masukkan nama: ")
    new_user_username =input("Masukkan username: ")
    while cek(new_user_username, data_pengguna_global, 1):
        print("Nama username tersebut sudah ada. Pilih username lain!")
        new_user_username = input("Masukkan username:")
    new_user_password = input("Masukkan password: ")
    new_user_alamat = input("Masukkan alamat: ")

    
    new_user = [new_user_id, new_user_username, new_user_nama, new_user_alamat, new_user_password, 'user']

    
    data_pengguna_global.append(new_user)
    print("User {} telah berhasil register ke dalam Kantong Ajaib.".format(new_user_username))

def login():
    """
        F02

    """
    
    username = ''
    
    while (username != "keluar"):
        username = input("Masukkan username:\n>>")

        password = input("Masukkan password:\n>>")
        
        if (username == 'keluar'):
            continue
        elif cek(username,data_pengguna_global,1):
            clrs()
            temp = ayo_ambil_sebaris(data_pengguna_global, username, 1)
            if temp[4] != password:
                pass
            elif ayo_ambil_sebagian(data_pengguna_global, username, 1, 5) == 'admin':
                print('Halo admin {}! Selamat datang di Kantong Ajaib.'.format(username))
                return ayo_ambil_sebaris(data_pengguna_global, username,1), 'admin'
            elif ayo_ambil_sebagian(data_pengguna_global, username, 1, 5) == 'user':
                print('Halo {}! Selamat datang di Kantong Ajaib.'.format(username))
                return ayo_ambil_sebaris(data_pengguna_global, username,1), 'pengguna'
        print("username tidak terdaftar atau password salah!")
        print("masukkan keluar pada username untuk batal")
    return

def searchByRarity():
    TabRarity = ["C", "B", "A", "S"]
    l = len(data_gadget_global)

    rarityPencarian = (input('Masukan rarity: '))
    if rarityPencarian in TabRarity:
        print('Hasil pencarian: ')
        found = 0
        n = 0
        
        while (n<l):
            if (data_gadget_global[n][4] == rarityPencarian):
                found += 1
                print()
                print('Nama: ', data_gadget_global[n][1])
                print('Deskripsi: ', data_gadget_global[n][2])
                print('Jumlah: ', data_gadget_global[n][3])
                print('Rarity: ', data_gadget_global[n][4])
                print('Tahun Ditemukan: ', data_gadget_global[n][5])
                n += 1
            else:
                n += 1

    if found == 0:
        print('Tidak ada barang dengan rarity ', rarityPencarian)

def searchByYear():
    tahun = int(input("Masukan tahun: "))
    kategori = input("Masukan kategori: ")
    found = 0
    l = len(data_gadget_global)
    n = 0

    while (n<l):
        if (kategori=='='):
            if (data_gadget_global[n][5]==tahun):
                found += 1
                print()
                print('Nama: ', data_gadget_global[n][1])
                print('Deskripsi: ', data_gadget_global[n][2])
                print('Jumlah: ', data_gadget_global[n][3])
                print('Rarity: ', data_gadget_global[n][4])
                print('Tahun Ditemukan: ', data_gadget_global[n][5])
                n = n+1
            else:
                n = n+1
        elif (kategori=='>'):
            if (data_gadget_global[n][5]>tahun):
                found += 1
                print()
                print('Nama: ', data_gadget_global[n][1])
                print('Deskripsi: ', data_gadget_global[n][2])
                print('Jumlah: ', data_gadget_global[n][3])
                print('Rarity: ', data_gadget_global[n][4])
                print('Tahun Ditemukan: ', data_gadget_global[n][5])
                n = n+1
            else:
                n = n+1
        elif (kategori=='<'):
            if (data_gadget_global[n][5]<tahun):
                found += 1
                print()
                print('Nama: ', data_gadget_global[n][1])
                print('Deskripsi: ', data_gadget_global[n][2])
                print('Jumlah: ', data_gadget_global[n][3])
                print('Rarity: ', data_gadget_global[n][4])
                print('Tahun Ditemukan: ', data_gadget_global[n][5])
                n = n+1
            else:
                n = n+1
        elif (kategori=='>='):
            if (data_gadget_global[n][5]>=tahun):
                found += 1
                print()
                print('Nama: ', data_gadget_global[n][1])
                print('Deskripsi: ', data_gadget_global[n][2])
                print('Jumlah: ', data_gadget_global[n][3])
                print('Rarity: ', data_gadget_global[n][4])
                print('Tahun Ditemukan: ', data_gadget_global[n][5])
                n = n+1
            else:
                n = n+1
        elif (kategori=='<='):
            if (data_gadget_global[n][5]<=tahun):
                found += 1
                print()
                print('Nama: ', data_gadget_global[n][1])
                print('Deskripsi: ', data_gadget_global[n][2])
                print('Jumlah: ', data_gadget_global[n][3])
                print('Rarity: ', data_gadget_global[n][4])
                print('Tahun Ditemukan: ', data_gadget_global[n][5])
                n = n+1
            else:
                n = n+1
    if found == 0:
        print('Tidak ada gadget yang ditemukan')
   
def tambahitem(): #fungsi untuk menambahkan item baru (ADMIN)
    bisa_tambahitem = True
    TabRarity = ["C", "B", "A", "S"] #Rarity bernilai True hanya jika berupa character C/ B/ A/ S
    id_item = input("Masukkan ID: ") #input nama ID
    if (id_item[0] == 'G') and (len(id_item)!= 1): #id diproses pada list gadget jika berawalan huruf G dan berakhiran kode nomor tertentu
        if cek(id_item, data_gadget_global, 0): #mengonfirmasi ID jika sudah terdaftar tidak akan diproses lagi
            print("\nGagal menambahkan item karena ID sudah ada")
        else:#menginput data item gadget baru secara keseluruhan
            new_gadget_id = id_item
            new_gadget_name = input("Masukkan Nama: ")
            new_gadget_deskripsi = input("Masukkan Deskripsi: ")
            new_gadget_jumlah = int(input("Masukkan Jumlah: "))
            new_gadget_rarity = input("Masukkan Rarity: ")
            new_gadget_tahun = input("Masukkan tahun ditemukan: ")
            if (new_gadget_jumlah <=0): #jumlah item valid hanya jika positif
                bisa_tambahitem = False
                print("\nInput jumlah tidak valid!\n")
            if new_gadget_rarity not in TabRarity: #rarity valid jika berupa character pada TabRarity
                bisa_tambahitem = False
                print("\nInput rarity tidak valid!\n")
            if bisa_tambahitem: #memasukkan data gadget baru kedalam list data_gadget_global
                new_gadget = [new_gadget_id, new_gadget_name, new_gadget_deskripsi, new_gadget_jumlah, new_gadget_rarity, new_gadget_tahun]
                data_gadget_global.append(new_gadget)
                print("\nItem telah berhasil ditambahkan ke database \n")
    elif (id_item[0] == 'C') and (len(id_item) != 1): #jika nama item berawalan huruf C maka diproses sebagai consumable
        if cek(id_item, data_consumable_global, 0): #mengonfirmasi ID jika sudah terdaftar tidak akan diproses lagi
            print("\n Gagal menambahkan item karena ID sudah ada")
        else:#menginput data item consumable baru secara keseluruhan
            new_consumable_id = id_item
            new_consumable_name = input("Masukkan Nama: ")
            new_consumable_deskripsi = input("Masukkan Deskripsi: ")
            new_consumable_jumlah = int(input("Masukkan Jumlah: "))
            new_consumable_rarity = input("Masukkan Rarity: ")
            if (new_consumable_jumlah <=0): #jumlah item valid hanya jika bernilai positif
                bisa_tambahitem = False
                print("\nInput jumlah tidak valid!\n")
            if new_consumable_rarity not in TabRarity:
                bisa_tambahitem = False #rarity valid hanya jika berupa character pada TabRarity
                print("\nInput rarity tidak valid!\n")
            elif bisa_tambahitem: #memasukan data item consumable baru kedalam list data_consumable_global
                new_consumable = [new_consumable_id, new_consumable_name, new_consumable_deskripsi, new_consumable_jumlah, new_consumable_rarity]
                data_consumable_global.append(new_consumable)
                print("\nItem telah berhasil ditambahkan ke database \n")
    else:
        print("Gagal menambahkan item karena ID tidak valid") #mengembalikan pesan error jika item baru bukan gadget atau consumable

def hapusitem():
	id_item = input('Masukkan ID Item: ') #input ID item
	if (id_item[0] == "G"): #jika id berawalan huruf G akan diproses sebagai gadget
		if cek(id_item, data_gadget_global, 0): #mengonfirmasi id gadget ada pada list
			deskripsi_item = ayo_ambil_sebagian(data_gadget_global,id_item, 0, 1) #mengambil data string berupa deskripsi gadget dari ID tersebut
			print('Apakah anda yakin ingin menghapus {} '.format(deskripsi_item),end="")
			selector = input("(Y/N)?")
			if (selector == "Y"): #proses penghapusan item dijalankan jika memilih selector Y
				ayo_hapus_sebaris(data_gadget_global, id_item, 0) #menghapus item pada list gadget
				print('\n Item telah berhasil dihapus dari database.\n')
			else:
				print('')
		else: #jika id tidak ada pada list gadget
			print('Tidak ada item dengan ID tersebut')
	elif (id_item[0] == 'C'): #jika id berawalan huruf C akan diproses sebagai consumable
		if cek(id_item, data_consumable_global, 0): #mengonfirmasi id consumable ada pada list
			deskripsi_item = ayo_ambil_sebagian(data_consumable_global,id_item, 0, 1) #mengambil data string berupa deskripsi consumable dari ID tersebut
			print('Apakah anda yakin ingin menghapus {} '.format(deskripsi_item),end="")
			selector = input("(Y/N)?") #proses penghapusan item dijalankan jika memilih selector Y
			if (selector == "Y"):
				ayo_hapus_sebaris(data_consumable_global, id_item, 0) #menghapus item pada list consumable
				print('\n Item telah berhasil dihapus dari database.\n')
			else:
				print('')
		else: #jika id tidak ada pada list consumable
			print('Tidak ada item dengan ID tersebut') #
	else: #jika id item bukan merupakan gadget atau consumable
		print('Tidak ada item dengan ID tersebut')

def ubahjumlah(): #fungsi untuk mengubah jumlah item (ADMIN)
	id_item = input("Masukan ID: ") #input ID item
	if cek(id_item, data_gadget_global, 0): # jika id berada pada list gadget.csv
		tambah_jumlah = int(input("Masukan Jumlah: "))  #jumlah item tambahan
		jumlah_lama = ayo_ambil_sebagian(data_gadget_global, id_item, 0, 3) #jumlah item sebelum penambahan
		new_jumlah = jumlah_lama + tambah_jumlah #jumlah akhir item
		deskripsi_item = ayo_ambil_sebagian(data_gadget_global,id_item, 0, 1) #mengambil string deskripsi item sesuai ID
		if (new_jumlah >= 0): #kondisi valid ketika jumlah akhir item pada data tidak negatif
			modify_datas(data_gadget_global, id_item, 0, 3, new_jumlah) #modifikasi kolom jumlah item
			if (tambah_jumlah > 0):
				print(str(tambah_jumlah) + ' {} berhasil ditambahkan. Stok sekarang : '.format(deskripsi_item) + str(new_jumlah))
			elif (tambah_jumlah <0):
				print(str((abs(tambah_jumlah))) + ' {} berhasil dibuang. Stok sekarang : '.format(deskripsi_item) + str(new_jumlah))
		else:
			print(str((abs(tambah_jumlah))) + ' {} gagal dibuang karena stok kurang. Stok sekarang : '.format(deskripsi_item) + str(jumlah_lama) + '( < {})'.format(abs(tambah_jumlah)))
	elif cek(id_item, data_consumable_global, 0): #jika id berada pada list consumable.csv
		tambah_jumlah = int(input("Masukan Jumlah: ")) #jumlah item tambahan
		jumlah_lama = ayo_ambil_sebagian(data_consumable_global, id_item, 0, 3) #jumlah item sebelum penambahan
		new_jumlah = jumlah_lama + tambah_jumlah #jumlah akhir item
		deskripsi_item = ayo_ambil_sebagian(data_consumable_global,id_item, 0, 1) #mengambil string deskripsi item sesuai ID
		if (new_jumlah >= 0): #kondisi valid ketika jumlah akhir item pada data tidak negatif
			modify_datas(data_consumable_global, id_item, 0, 3, new_jumlah) #modifikasi kolom jumlah item
			if (tambah_jumlah > 0):
				print(str(tambah_jumlah) + ' {} berhasil ditambahkan. Stok sekarang : '.format(deskripsi_item) + str(new_jumlah))
			elif (tambah_jumlah <0):
				print(str((abs(tambah_jumlah))) + ' {} berhasil dibuang. Stok sekarang : '.format(deskripsi_item) + str(new_jumlah))
		else:
			print(str((abs(tambah_jumlah))) + ' {} gagal dibuang karena stok kurang. Stok sekarang : '.format(deskripsi_item) + str(jumlah_lama) + '( < {})'.format(abs(tambah_jumlah)))
	else:
		print(' \nTidak ada item dengan ID tersebut! \n') #Input ID diproses hanya jika id berawalan huruf G atau C

def pinjam_gadget():
    input_id_item = input("Masukan ID: ")
    input_tanggal_pinjam = input("Tanggal peminjaman: ")
    input_jumlah_pinjam = int(input("Jumlah peminjaman: "))

    print()

    if cek(input_id_item,data_gadget_global,0) and validasi_tanggal(input_tanggal_pinjam): 

        id_peminjam = active_person[0]
        nama_gadget = ayo_ambil_sebagian(data_gadget_global, input_id_item, 0, 1)

        # Mengecek apakah user sudah pernah meminjam item tsb dan belum dikembalikan
        # Jika user belum mengembalikan, maka tidak bisa diproses karena item masih dipinjam
        if cek_user_masih_meminjam(id_peminjam,input_id_item): # Jika user sedang meminjam
            print("Item sedang dipinjam!")
        else: # Jika user tidak sedang meminjam
            jumlah_gadget = ayo_ambil_sebagian(data_gadget_global, input_id_item, 0, 3)
            if(jumlah_gadget < input_jumlah_pinjam): # Item yang ingin dipinjam > stok item
                print("Item tidak bisa dipinjam karena jumlah item tidak memenuhi!")
            else: # Jumlah item yang ingin dipinjam memenuhi
                jumlah_akhir = jumlah_gadget - input_jumlah_pinjam
                modify_datas(data_gadget_global, input_id_item, 0, 3, jumlah_akhir)
                if data_gadget_borrow_history_global == []:
                    data_gadget_borrow_history_global.append([1,id_peminjam,input_id_item,input_tanggal_pinjam,input_jumlah_pinjam,'false'])
                else:
                    id = data_gadget_borrow_history_global[-1][0] + 1
                    data_gadget_borrow_history_global.append([id,id_peminjam,input_id_item,input_tanggal_pinjam,input_jumlah_pinjam,'false'])
    
                print("Item "+ str(nama_gadget)+" (x" + str(input_jumlah_pinjam) + ") berhasil dipinjam!")
            
    else: # Jika ID dan/atau tanggal tidak valid
        if (cek(input_id_item,data_gadget_global,0)==False) and (validasi_tanggal(input_tanggal_pinjam) == True):
            print("Tidak ada item dengan ID tersebut!")
        elif (cek(input_id_item,data_gadget_global,0)==True) and (validasi_tanggal(input_tanggal_pinjam) == False):
            print("Tanggal peminjaman tidak sesuai!")
        else:
            print("ID item dan tanggal peminjaman tidak sesuai!")

def kembalikan_gadget():
    id_peminjam = active_person[0]

    # Membuat array of array dari data histori pinjam dari user
    data_pinjam = []
    for baris in data_gadget_borrow_history_global:
        if (baris[1] == id_peminjam) and (baris[5] == 'false'):
            data_pinjam.append(baris)

    if data_pinjam != []: # Jika ada item yang dipinjam

        for i in range (len(data_pinjam)):
            print(i+1,". ",id_to_name_gadget(data_pinjam[i][2]))

        nomor_pinjam = int(input("Masukkan nomor peminjaman:"))
        tanggal_pengembalian = input("Tanggal pengembalian:")

        print()

        if ( 1<= nomor_pinjam <= len(data_pinjam) and validasi_tanggal(tanggal_pengembalian) ): # validasi input pilihan yang dimasukkan dan tanggal
            indeks_data_pinjam = nomor_pinjam - 1 
            id_gadget_kembali = data_pinjam[indeks_data_pinjam][2] # id gadget yang ingin dikembalikan
            jumlah_gadget_kembali = data_pinjam[indeks_data_pinjam][4] # jumlah gadget yang ingin dikembalikan


            # Mengembalikan gadget yang dipinjam
            jumlah_gadget_sebelum = ayo_ambil_sebagian(data_gadget_global,id_gadget_kembali,0,3)
            jumlah_gadget = jumlah_gadget_sebelum + jumlah_gadget_kembali
            modify_datas(data_gadget_global, id_gadget_kembali, 0, 3, jumlah_gadget)

            id_riwayat_peminjaman = data_pinjam[indeks_data_pinjam][0]

            # Untuk gadget borrow history
            # Karena sudah dikembalikan maka is_returned menjadi true
            for baris in data_gadget_borrow_history_global:
                if (baris[0] == id_riwayat_peminjaman):
                    baris[5] = 'true'
    
            # Untuk data gadget return history
            if data_gadget_return_history_global == []: 
                data_gadget_return_history_global.append([1,id_riwayat_peminjaman,tanggal_pengembalian])
            else: # data_gadget_return_history_global != []
                id = data_gadget_return_history_global[-1][0] + 1
                data_gadget_return_history_global.append([id,id_riwayat_peminjaman,tanggal_pengembalian])

            print("Item " + id_to_name_gadget(id_gadget_kembali) + " (x" + str(jumlah_gadget_kembali) + ") telah dikembalikan")
        
        else: # Jika input nomor peminjaman dan/atau tanggal tidak valid
            if (nomor_pinjam < 1 or nomor_pinjam > len(data_pinjam)) and (validasi_tanggal(tanggal_pengembalian) == True):
                print("Nomor peminjaman tidak valid")
            elif (1<= nomor_pinjam <= len(data_pinjam)) and (validasi_tanggal(tanggal_pengembalian) == False):
                print("Tanggal tidak sesuai")
            else:
                print("Nomor peminjaman dan tanggal peminjaman tidak sesuai")

    else: # data_gadget == [] atau tidak ada item yang sedang dipinjam
        print("Tidak ada gadget yang sedang dipinjam")

def minta_consumable():
    input_id_item = input("Masukan ID Item: ")
    input_jumlah_minta = int(input("Jumlah: "))
    input_tanggal_minta = input("Tanggal permintaan: ")

    print()

    if cek(input_id_item,data_consumable_global,0) and validasi_tanggal(input_tanggal_minta):

        jumlah_consumable = ayo_ambil_sebagian(data_consumable_global, input_id_item, 0, 3)
        nama_consumable = ayo_ambil_sebagian(data_consumable_global, input_id_item, 0, 1)
        id_peminjam = active_person[0]

        if(jumlah_consumable < input_jumlah_minta): # Jika jumlah item yang diminta melebihi stok item
            print("Item tidak mencukupi!")
        else: # Jika jumlah item yang diminta <= stok item
            jumlah_akhir = jumlah_consumable - input_jumlah_minta
            modify_datas(data_consumable_global, input_id_item, 0, 3, jumlah_akhir)

            if data_consumable_history_global == []:
                data_consumable_history_global.append([1,id_peminjam,input_id_item,input_tanggal_minta,input_jumlah_minta])
            else:
                id = data_consumable_history_global[-1][0] + 1
                data_consumable_history_global.append([id,id_peminjam,input_id_item,input_tanggal_minta,input_jumlah_minta])                    
            
            print("Item "+ str(nama_consumable)+" (x" + str(input_jumlah_minta) + ") telah berhasil diambil!")
        
    else: # Jika ID consumable dan/atau tanggal tidak valid
        if (cek(input_id_item,data_consumable_global,0)==False) and (validasi_tanggal(input_tanggal_minta) == True):
            print("Tidak ada item dengan ID tersebut!")
        elif (cek(input_id_item,data_consumable_global,0)==True) and (validasi_tanggal(input_tanggal_minta) == False):
            print("Tanggal permintaan tidak sesuai!")
        else:
            print("ID item dan tanggal permintaan tidak sesuai")
    
def help():
    if mode == "admin":
        print("========================HELP========================")
        print("register         - untuk melakukan registrasi user baru")
        print("carirarity       - untuk melakukan pencarian gadget berdasarkan rarity")
        print("caritahun        - untuk melakukan pencarian gadget berdasarkan tahun")
        print("tambahitem       - untuk melakukan penambahan item ke dalam inventory")
        print("hapusitem        - untuk melakukan penghapusan item pada database")
        print("ubahjumlah       - untuk melakukan perubahan jumlah gadget dan consumable")
        print("riwayatpinjam    - untuk melihat riwayat peminjaman gadget")
        print("riwayatkembali   - untuk melihat riwayat pengembalian gadget")
        print("riwayatambil     - untuk melihat riwayat pengebalian consumable")
        print("save             - untuk melakukan penyimpanan data ke dalam file")
        print("help             - untuk memberikan panduan penggunaan sistem")
        print("exit             - untuk keluar dari aplikasi")
    elif mode == "pengguna":
        print("========================HELP========================")
        print("carirarity       - untuk melakukan pencarian gadget berdasarkan rarity")
        print("caritahun        - untuk melakukan pencarian gadget berdasarkan tahun")
        print("pinjam           - untuk melakukan peminjaman gadget")
        print("kembalikan       - untuk melakukan pengembalian gadget secara seutuhnya")
        print("minta            - untuk melakukan permintaan consumable yang tersedia")
        print("save             - untuk melakukan penyimpanan data ke dalam file")
        print("help             - untuk memberikan panduan penggunaan sistem")
        print("exit             - untuk keluar dari aplikasi")

def loading():
    """
        F15
        Fungsi ini akan membuka semua file untuk program ini dengan nama yang sesuai
        dan menyimpannya dalam bentuk array yang selanjutnya akan dipakai selama program berjalan.
        langkah kerja:
        1. Prosedur akan menyimpan lokasi program untuk dipakai oleh fitur save
        2. Prosedur akan mengubah folder kerja program sesuai nama folder yang dimasukkan pada argparse
        3. prosedur membuat variabel global untuk setiap file csv
        4. Prosedur membuka file csv dan disimpan ke variabel global tadi untuk dipakai fitur-fitur lain
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("nama_folder", help="Folder tempat file yang dibutuhkan", type=str)
    args = parser.parse_args()

    global lokasi_program
    global folder_file

    lokasi_program = os.getcwd()
    folder_file = os.path.join(lokasi_program, args.nama_folder)

    try:
        os.chdir(folder_file)
    except:
        print("Tidak dapat menemukan Folder!")
        quit()
    
    
    global header_data_pengguna_global, data_pengguna_global
    global header_data_consumable_global, data_consumable_global
    global header_data_consumable_history_global, data_consumable_history_global
    global header_data_gadget_global, data_gadget_global
    global header_data_gadget_borrow_history_global, data_gadget_borrow_history_global
    global header_data_gadget_return_history_global, data_gadget_return_history_global
    
    header_data_pengguna_global, data_pengguna_global = buka_data("user.csv")
    header_data_consumable_global, data_consumable_global = buka_data("consumable.csv")
    header_data_consumable_history_global, data_consumable_history_global = buka_data("consumable_history.csv")
    header_data_gadget_global, data_gadget_global = buka_data("gadget.csv")
    header_data_gadget_borrow_history_global, data_gadget_borrow_history_global = buka_data("gadget_borrow_history.csv")
    header_data_gadget_return_history_global, data_gadget_return_history_global = buka_data("gadget_return_history.csv")
    
def save():
    """
        F15

    """
    nama_folder = input('Masukkan nama folder penyimpanan: ')
    lokasi_save = os.path.join(lokasi_program, nama_folder )

    print("Saving...")

    try: os.makedirs(lokasi_save)
    # try dan except ini berfungsi untuk melihat apakah folder sudah ada atau belum
    # kalau sudah ada akan lanjut, jika belum akan dibuat foldernya
    except: pass

    os.chdir(lokasi_save)

    datas_as_string_user = convert_datas_to_string(header_data_pengguna_global, data_pengguna_global)
    datas_as_string_consumable = convert_datas_to_string(header_data_consumable_global, data_consumable_global)
    datas_as_string_consumable_history = convert_datas_to_string(header_data_consumable_history_global, data_consumable_history_global)
    datas_as_string_gadget = convert_datas_to_string(header_data_gadget_global, data_gadget_global)
    datas_as_string_gadget_borrow_history = convert_datas_to_string(header_data_gadget_borrow_history_global, data_gadget_borrow_history_global)
    datas_as_string_gadget_return_history = convert_datas_to_string(header_data_gadget_return_history_global, data_gadget_return_history_global)

    f = open("user.csv", "w")
    f.write(datas_as_string_user)
    f.close()

    f = open("consumable.csv", "w")
    f.write(datas_as_string_consumable)
    f.close()
    
    f = open("consumable_history.csv", "w")
    f.write(datas_as_string_consumable_history)
    f.close()

    f = open("gadget.csv", "w")
    f.write(datas_as_string_gadget)
    f.close()

    f = open("gadget_borrow_history.csv", "w")
    f.write(datas_as_string_gadget_borrow_history)
    f.close()

    f = open("gadget_return_history.csv", "w")
    f.write(datas_as_string_gadget_return_history)
    f.close()

    
    print("Data telah disimpan pada folder {}!".format(nama_folder))

def exit():
    """
        F17
    """
    confirm = input('Apakah Anda mau menyimpan file yang sudah diubah? (Y/N)')
    while not confirm in ['Y', 'y', 'N', 'n']:
        print("Masukkan tidak valid!")
        confirm = input('Apakah Anda mau menyimpan file yang sudah diubah? (Y/N)')
          
    if confirm.lower() == 'y':
        save()

def lihat_history_return():
    from datetime import datetime
    
    all_dates = []

    for entry in data_gadget_return_history_global:
        if entry[2] in all_dates:
            pass
        else:
            all_dates.append(entry[2])
    
    
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
                print('Nama Pengambil         : {}'.format(id_to_name_user(useriD)))
                print('Nama Gadget            : {}'.format(id_to_name_gadget(gadgetiD)))
                print('Tanggal Pengembalian   : {}'.format(data_gadget_return_history_global_sorted[i][2]))
                print()
            break 
        else:
            for i in range(banyak_entri-1,banyak_entri-6,-1):
                useriD, gadgetiD = idPinjam_to_nama_gadget_id(data_gadget_return_history_global_sorted[i][1])
                print('ID Pengembalian        : {}'.format(data_gadget_return_history_global_sorted[i][0]))
                print('Nama Pengambil         : {}'.format(id_to_name_user(useriD)))
                print('Nama Gadget            : {}'.format(id_to_name_gadget(gadgetiD)))
                print('Tanggal Pengembalian   : {}'.format(data_gadget_return_history_global_sorted[i][2]))
                print()
            banyak_entri -= 5

            masukan = input('Tampilkan yang lain?(Y/N)')
            while not masukan in ['Y','y','N','n']:
                print('Masukkan tidak valid')
                masukan = input('Tampilkan yang lain?(Y/N)')
                    
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

            masukan = input('Tampilkan yang lain?(Y/N)')
            while not masukan in ['Y','y','N','n']:
                print('Masukkan tidak valid')
                masukan = input('Tampilkan yang lain?(Y/N)')
                    
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

            masukan = input('Tampilkan yang lain?(Y/N)')
            while not masukan in ['Y','y','N','n']:
                print('Masukkan tidak valid')
                masukan = input('Tampilkan yang lain?(Y/N')
                    
            if masukan.lower() == 'y':continue
            else: break

def main():
    clrs()
    print("Loading...")
    loading()

    print('Data User            :', data_pengguna_global)
    print()
    print('Data gadget          :', data_gadget_global)
    print()
    print('Data consumable      :', data_consumable_global)
    print()
    print('Data histori pinjam  :', data_gadget_borrow_history_global)
    print()
    print('Data histori kembali :', data_gadget_return_history_global)
    print()
    print('Data histori ambil   :', data_consumable_history_global)
    
    print('Selamat Datang di "Kantong Ajaib!"')
    masukan = ""

    

    while masukan != "exit":
        print(  "Main Menu:\n\
                 login -> Masuk ke dalam kantong ajaib\n\
                 exit -> Pergi dari gerbang kantong ajaib")
        masukan = input('>>')

        if masukan == 'login':
            global active_person, mode
            active_person, mode = login() # admin atau pengguna active_person, 
            
            if mode == "admin":
                masukan_admin = input('>>')
                while masukan_admin != "exit":

                    if masukan_admin == 'register':
                        register()
                    elif masukan_admin == 'help':
                        help()
                    elif masukan_admin == 'save':
                        save()
                    elif masukan_admin == 'riwayatpinjam':
                        lihat_history_borrow()
                    elif masukan_admin == 'riwayatkembali':
                        lihat_history_return()
                    elif masukan_admin == 'riwayatambil':
                        lihat_history_consum()
                    elif masukan_admin == 'tambahitem':
                        tambahitem()
                    elif masukan_admin == 'carirarity':
                        searchByRarity()
                    elif masukan_admin == 'caritahun':
                        searchByYear()
                    elif masukan_admin == 'hapusitem':
                        hapusitem()
                    elif masukan_admin == 'ubahjumlah':
                        ubahjumlah()
                    else:
                        print("masukan tidak valid")
                    masukan_admin = input ('>>')

            elif mode == "pengguna":
                masukan_pengguna = input('>>')
                while masukan_pengguna != "exit":
                    if masukan_pengguna == 'minta':
                        minta_consumable()
                    elif masukan_pengguna == 'save':
                        save()
                    elif masukan_pengguna == 'carirarity':
                        searchByRarity()
                    elif masukan_pengguna == 'caritahun':
                        searchByYear()
                    elif masukan_pengguna == 'pinjam':
                        pinjam_gadget()
                    elif masukan_pengguna == 'kembalikan':
                        kembalikan_gadget()
                    elif masukan_pengguna == 'help':
                        help()
                    else:
                        print("masukan tidak valid")
                    
                    masukan_pengguna = input('>>')


        elif masukan == 'exit':
            exit()
            quit()
            
            
        
        else: print('Fungsi tidak valid!')
            
            
                       
    
                    
        
    
    

if __name__ == "__main__":
    main()

    
