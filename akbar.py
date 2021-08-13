import argparse
import os
import time


# FUNGSI FUNGSI TAMBAHAN

def clrs():
    os.system('cls')

def parser(dipisah, pemisah): # Setara dengan dipisah.split(pemisah)
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
    raw_array_of_data = parser(line,";")
    array_of_data = [data.strip() for data in raw_array_of_data]
    return array_of_data

def convert_array_data_to_real_values(nama_data, array_data):
    arr_cpy = array_data[:]

    if nama_data == "user.csv":
        for i in range(5):
            if (i==0):
                arr_cpy[i] = int(arr_cpy[i])
    elif nama_data == "gadget.csv":
        for i in range(6):
            if (i==3):
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
    for baris in data:
        if baris[kolom] == entri:
            return True
    return False

def convert_datas_to_string(header, body):
  string_data = ";".join(header) + "\n"
  for arr_data in body:
    arr_data_all_string = [str(var) for var in arr_data]
    string_data += ";".join(arr_data_all_string)
    string_data += "\n"
  return string_data

# FUNGSI FUNGSI KETENTUAN
# def register():

def login():
    
    username = ''
    
    while (username != "keluar"):
        username = input("Masukkan username:\n>>")

        password = input("Masukkan password:\n>>")
        
        if (username == 'keluar'):
            continue
        elif (username == 'admin') and (password == 'admin'):
            clrs()
            print('Selamat datang di Mode admin')
            return 'admin'
        elif cek(username,data_pengguna_global,1) and cek(password, data_pengguna_global, 4):
            clrs()
            print('Halo {}! Selamat datang di Kantong Ajaib.'.format(username))
            return 'pengguna'
        print("username tidak terdaftar atau password salah!")
        print("masukkan keluar pada username untuk batal")
    return
        

def loading():

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
    lokasi_save = os.path.join(lokasi_program, input('Masukkan nama folder penyimpanan: '))

    try: os.makedirs(lokasi_save)
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

def register():
    
    new_user_id = data_pengguna_global[-1][0] + 1
    new_user_nama = input("Masukkan nama: ")
    new_user_username =input("Masukkan username: ")
    while cek(new_user_username, data_pengguna_global, 1):
        print("Nama username tersebut sudah ada. Pilih username lain!")
        new_user_username = input("Masukkan username:")
    new_user_password = input("Masukkan password: ")
    new_user_alamat = input("Masukkan alamat: ")

    
    new_user = [new_user_id, new_user_username, new_user_nama, new_user_alamat, new_user_password]

    
    data_pengguna_global.append(new_user)
    print("User {} telah berhasil register ke dalam Kantong Ajaib.".format(new_user_username))
   
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
            mode = login() # admin atau pengguna
            
            if mode == "admin":
                masukan_admin = input('>>')
                while masukan_admin != "exit":
                    if masukan_admin == 'exit':
                        masukan_admin = 'exit'
                           
                        continue
                    elif masukan_admin == 'register':
                        register()
                    elif masukan_admin == 'help':
                        print("here is some help")
                    elif masukan_admin == 'save':
                        save()
                    else:
                        print("masukan tidak valid")
                    masukan_admin = input ('>>')

            elif mode == "pengguna":
                masukan_pengguna = input('>>')
                print ("masuk pak Rusli")

        elif masukan == 'exit':
            confirm = input('Apakah Anda mau menyimpan file yang sudah diubah? (Y/N)')
            
            while not confirm in ['Y', 'y', 'N', 'n']:
                print("Masukkan tidak valid!")
                confirm = input('Apakah Anda mau menyimpan file yang sudah diubah? (Y/N)')
            
            if confirm.lower() == 'y':
                save()
            
            else: pass
        
        else: print('Fungsi tidak valid! Masukkan help untuk pentunjuk.')
            
            
                       
    
                    
        
    
    

if __name__ == "__main__":
    main()

    
