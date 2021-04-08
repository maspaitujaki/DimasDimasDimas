# 1. Buka File
f = open("korean_drama.csv","r")
print("ini f.read")
print()
print(f.read())
print()
f.close()

#f adalah variabel untuk menyimpan data file yang kita baca
# open( filename , mode ) adalah cara untuk membuka suatu file dengan nama 
#       filename . Mode adalah apa yang kita ingin lakukan ke file tersebut. 
# Ada beberapa mode yang perlu diingat:
# - r → artinya kita ingin membaca file tersebut, 
#       dengan kondisi file tersebut sudah ada. Bila file tidak ada akan error
# - w → artinya kita ingin menulis ke file terseubt
# - w+ → artinya kita selain ingin menulis, ingin membaca isi 
#       file tersebut juga, tidak akan memberikan error apabila file tidak ada
# - a → (append) artinya kita ingin menambahkan konten ke ujung file
# f.read() adalah cara untuk membaca keseluruhan file
# f.close() adalah cara untuk memberi tahu bahwa file 
#           tersebut tidak akan kita gunakan lagi. 
#           kenapa perlu f.close()? Karena misal program berjalan lama, 
#           file yang kita open akan dianggap tidak bisa digunakan oleh 
#           program lain bila tidak di close, maka jangan lupa untuk close() 
#           (jaga2 aja).


# 2. Pisahkan file jadi beberapa baris
f = open("korean_drama.csv","r")
lines = f.readlines()
f.close()
print("Ini File Jadi Baris")
print(lines)
print()
# ini akan menghasilkan tiap line tetapi terdapat new line

# 2.1 pisahkan file menjadi beberapa baris tanpa new line
f = open("korean_drama.csv","r")
raw_lines = f.readlines()
f.close()
lines = [raw_line.replace("\n","") for raw_line in raw_lines]
print("File jadi baris tanpa new Line")
for line in lines:
    print(line)
print()

# 3. Mengubah String Baris menjadi array of Data
f = open("korean_drama.csv","r")
raw_lines = f.readlines()
f.close()
lines = [raw_line.replace("\n","") for raw_line in raw_lines]
print("Baris diubah menjadi array of Data")
for line in lines:
    array_of_data = line.split(",")
    print(array_of_data)
print()

# Data masih berupa data kotor dimana no adalah str dan ada spasi di
# salah satu rating
# maka kita akan membersihkannya dengan strip untuk menghilangkan spasi

f = open("korean_drama.csv","r")
raw_lines = f.readlines()
f.close()
lines = [raw_line.replace("\n","") for raw_line in raw_lines]
print("data bersih dari spasi")
for line in lines:
    raw_array_of_data = line.split(",")
    array_of_data = [data.strip() for data in raw_array_of_data]
    print(array_of_data)
print()

# proses mengubah data menjadi array of data dapat menggunakan function
# def convert_line_to_data(line):
#   raw_array_of_data = line.split(",")
#   array_of_data = [data.strip() for data in raw_array_of_data]
#   return array_of_data

# print("Data bersih dari spasi juga namun, menggunakan function")
# for line in lines:
#     array_of_data = convert_line_to_data(line)
#     print(array_of_data)
# print()


# Selanjutnya adalah pengubahan data ke nilai sesungguhnya 
# contohnya pada kolom nomor sekarang adalah string
# akan kita ubah ke integer
# def convert_array_data_to_real_values(array_data):
#     arr_cpy = array_data[:]
#     for i in range(3):
#         if (i==1):
#             arr_cpy[i] = int(arr_cpy[i])
#         elif(i==2):
#             arr_cpy[i] = float(arr_cpy[i])
#     return arr_cpy

# Pada proses pengubahan akan terjadi kesalahan karena header tidak bisa convert tipe
# maka akan dilakukan pembuangan header dengan
# raw_header = lines.pop(0)



# maka kode lengkap sejauh ini adalah
f = open("korean_drama.csv","r")
raw_lines = f.readlines()
f.close()
lines = [raw_line.replace("\n","") for raw_line in raw_lines]

def convert_line_to_data(line):
  raw_array_of_data = line.split(",")
  array_of_data = [data.strip() for data in raw_array_of_data]
  return array_of_data

def convert_array_data_to_real_values(array_data):
    arr_cpy = array_data[:]
    for i in range(3):
        if (i==0):
            arr_cpy[i] = int(arr_cpy[i])
        elif(i==2):
            arr_cpy[i] = float(arr_cpy[i])
    return arr_cpy

raw_header = lines.pop(0)
header = convert_line_to_data(raw_header)
print("Ini adalah Header")
print(header)
print()
print("ini adalah data dengan tipe yang benar")
for line in lines:
    array_of_data = convert_line_to_data(line)
    real_values = convert_array_data_to_real_values(array_of_data)
    print(real_values)
print()

#  4. Modifikasi

#  pada titik ini yang kita lakukan hanya mengubah baris lalu print
#  untuk menyimpan data yang sudah benar kita dapat melakukannya dengan append
datas = []
for line in lines:
    array_of_data = convert_line_to_data(line)
    real_values = convert_array_data_to_real_values(array_of_data)
    datas.append(real_values)
print("pada titik ini kita sudah mengubah data dari csv menjadi array")
print(datas)
print()


def modify_datas(idx, col, value):
    if col == 0:
        return
    elif col == 1:
        if isinstance(value, int):
            datas[idx][col] = value
        else: return
    elif col == 2 :
        if isinstance(value, float):
            datas[idx][col] = value
        else: return

# ubah rating goblin jadi 5.5, jangan triggered ya :D
modify_datas(0, 2, 5)
print(datas)

# 5. Menyimpan File
# untuk menyimpan, kita perlu mengubah data kita yang tadinya
#  berbentuk array menjadi bentuk string dan newline
# kita membuat fungsi baru
def convert_datas_to_string():
    string_data = ",".join(header) + "\n"
    for arr_data in datas:
        arr_data_all_string = [str(var) for var in arr_data]
        string_data += ",". join(arr_data_all_string)
        string_data += "\n"
    return string_data

# langkah selanjutnya adalah menyimpan dengan open(namafile,"w")

datas_as_string = convert_datas_to_string()

f = open("korean_drama.csv","w")
f.write(datas_as_string)
f.close()

# misalkan kita ingin membuat entri baru pada datas
# maka kita meminta masukan untuk entri baru
new_drama_idx = datas[-1][0] + 1
new_drama_name = input("What is the drama name? \n>>")
new_drama_rating = float(input("What is your rating? \n>>"))
new_drama = [new_drama_idx, new_drama_name, new_drama_rating]

# setelah punya komponen untuk entri baru, kita masukkan ke datas
datas.append(new_drama)


# Skema di atas hanya dapat menambahkan satu persatu
# untuk menambahkan banyak sekaligus dapat dengan cara di bawah ini

new_drama_name = ""
new_dramas = []
new_drama_idx = datas[-1][0] + 1
while(new_drama_name != "stop"):
    new_drama_name = input("What is the drama name? \n >>")
    if (new_drama_name == "stop"):
        continue
    new_drama_rating = float(input("What is your rating? \n>>"))
    new_drama = [new_drama_idx, new_drama_name, new_drama_rating]
    new_dramas.append(new_drama)
    new_drama_idx += 1

datas += new_dramas

    
