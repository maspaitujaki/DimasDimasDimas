import argparse
import os
import time


# FUNGSI FUNGSI TAMBAHAN

def clrs():
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
    # elif nama_data == "consumable_history.csv":
    #     for i in range(4):
    elif nama_data == "gadget_borrow_history":
        for i in range(5):
            if (i==4):
                arr_cpy[i] = int(arr_cpy[i])
    # elif nama_data == "gadget_return_history":
    #     for i in range(4):
    
    
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

def ayo_ambil_sebagian(array_data, pencari, kolom_pencari, kolom_dicari):
    for line in array_data: 
        if line[kolom_pencari] == pencari:
            return line[kolom_dicari]
    return 

def ayo_ambil_sebaris(array_data, pencari, kolom_pencari):
    for line in array_data:
        if line[kolom_pencari] == pencari:
            return line
    return

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
        elif cek(username,data_pengguna_global,1) and cek(password, data_pengguna_global, 4):
            clrs()
            if ayo_ambil_sebagian(data_pengguna_global, username, 1, 5) == 'admin':
                print('Halo admin {}! Selamat datang di Kantong Ajaib.'.format(username))
                return ayo_ambil_sebaris(data_pengguna_global, username,1), 'admin'
            elif ayo_ambil_sebagian(data_pengguna_global, username, 1, 5) == 'user':
                print('Halo {}! Selamat datang di Kantong Ajaib.'.format(username))
                return ayo_ambil_sebaris(data_pengguna_global, username,1), 'pengguna'
        print("username tidak terdaftar atau password salah!")
        print("masukkan keluar pada username untuk batal")
    return
        


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
    
    os.chdir(folder_file)
    
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






def main():
    clrs()
    print("Loading...")
    loading()

    print('Selamat Datang di "Kantong Ajaib!"')
    masukan = ""

    print(data_consumable_global)
    print(data_consumable_history_global)
    print(data_gadget_borrow_history_global)
    print(data_gadget_global)
    print(data_gadget_return_history_global)
    print(data_pengguna_global)

    while masukan != "exit":
        print(  "Main Menu:\n\
                 login -> Masuk ke dalam kantong ajaib\n\
                 exit -> Pergi dari gerbang kantong ajaib")
        masukan = input('>>')

        if masukan == 'login':
            global active_person
            active_person, mode = login() # admin atau pengguna active_person, 
            
            if mode == "admin":
                masukan_admin = input('>>')
                while masukan_admin != "exit":

                    if masukan_admin == 'register':
                        register()
                    elif masukan_admin == 'help':
                        print("here is some help")
                    elif masukan_admin == 'save':
                        save()
                    elif masukan_admin == 'akusiapa':
                        print(header_data_pengguna_global)
                        print(active_person)
                    else:
                        print("masukan tidak valid")
                    masukan_admin = input ('>>')

            elif mode == "pengguna":
                masukan_pengguna = input('>>')
                while masukan_pengguna != "exit":
                    if masukan_pengguna == 'akusiapa':
                        print(header_data_pengguna_global)
                        print(active_person)
                    masukan_pengguna = input('>>')


        elif masukan == 'exit':
            exit()
            
            
        
        else: print('Fungsi tidak valid! Masukkan help untuk pentunjuk.')
            
            
                       
    
                    
        
    
    

if __name__ == "__main__":
    main()

    
