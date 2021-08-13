def register():
    f = open("user.csv", 'r')
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]

    def convert_id_to_value(array_data):
        copy_arr = array_data[:]
        for i in range(6):
            if i == 0:
                copy_arr[i] = int(copy_arr[i])
        return copy_arr

    def convert_line_to_data(line):
        raw_array_data = line.split(";")
        array_of_data = [data.strip() for data in raw_array_data]
        return array_of_data
        # array_of_data = []
        # for line in lines:
        #     new_array = []
        #     kata = ''
        #     for ch in line:
        #         if ch == ' ' and kata != '':
        #             new_array.append(kata)
        #             kata = ''
        #         else:
        #             kata += ch
        #     if kata != '':
        #         new_array.append(kata)
        #     array_of_data.append(new_array)
        # return array_of_data


    raw_header = lines.pop(0)
    header = convert_line_to_data(raw_header)

    data = []
    for line in lines:
        array_of_data = convert_line_to_data(line)
        print(array_of_data)
        id_data = convert_id_to_value(array_of_data)
        data.append(id_data)

    def convert_data_to_string():
        string_data = ",".join(header) + "\n"
        for arr_data in data:
            arr_data_all_string = [str(var) for var in arr_data]
            string_data += ",".join(arr_data_all_string)
            string_data += "\n"
        return string_data

    print(">>> register\n")
    new_user_idx = data[-1][0] + 1
    new_name = input("Masukkan nama: ")
    new_username = input("Masukkan username: ")
    new_password = input("Masukkan password: ")
    new_address = input("Masukkan alamat: ")
    new_role = "user"
    new_user = [new_user_idx, new_username, new_name, new_address, new_password, new_role]

    data.append(new_user)

    data_as_string = convert_data_to_string()
    f = open("user.csv", "w")
    f.write(data_as_string)
    f.close()

    print("\nUser " + new_username + " telah berhasil register ke dalam Kantong Ajaib.\n")

register()