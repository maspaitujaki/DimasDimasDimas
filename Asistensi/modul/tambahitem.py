def tambahitem(): #fungsi untuk menambahkan item baru (ADMIN)
    bisa_tambahitem = True
    TabRarity = ["C", "B", "A", "S"] #Rarity bernilai True hanya jika berupa character C/ B/ A/ S
    id_item = input("Masukkan ID: "+ "\n") #input nama ID
    if (id_item[0] == 'G') and (len(id_item)!= 1): #id diproses pada list gadget jika berawalan huruf G dan berakhiran kode nomor tertentu
        if cek(id_item, data_gadget_global, 0): #mengonfirmasi ID jika sudah terdaftar tidak akan diproses lagi
            print("\n Gagal menambahkan item karena ID sudah ada")
        else:#menginput data item gadget baru secara keseluruhan
            new_gadget_id = id_item
            new_gadget_name = input("Masukkan Nama: "+ "\n")
            new_gadget_deskripsi = input("Masukkan Deskripsi: "+ "\n")
            new_gadget_jumlah = int(input("Masukkan Jumlah: "+ "\n"))
            new_gadget_rarity = input("Masukkan Rarity: "+ "\n")
            new_gadget_tahun = input("Masukkan tahun ditemukan: "+ "\n")
            if (new_gadget_jumlah <=0): #jumlah item valid hanya jika positif
                bisa_tambahitem = False
                print("\n Input jumlah tidak valid!\n")
            if new_gadget_rarity not in TabRarity: #rarity valid jika berupa character pada TabRarity
                bisa_tambahitem = False
                print("\n Input rarity tidak valid!\n")
            if bisa_tambahitem: #memasukkan data gadget baru kedalam list data_gadget_global
                new_gadget = [new_gadget_id, new_gadget_name, new_gadget_deskripsi, new_gadget_jumlah, new_gadget_rarity, new_gadget_tahun]
                data_gadget_global.append(new_gadget)
                print("\n Item telah berhasil ditambahkan ke databese \n")
    elif (id_item[0] == 'C') and (len(id_item) != 1): #jika nama item berawalan huruf C maka diproses sebagai consumable
        if cek(id_item, data_consumable_global, 0): #mengonfirmasi ID jika sudah terdaftar tidak akan diproses lagi
            print("\n Gagal menambahkan item karena ID sudah ada")
        else:#menginput data item consumable baru secara keseluruhan
            new_consumable_id = id_item
            new_consumable_name = input("Masukkan Nama: "+ "\n")
            new_consumable_deskripsi = input("Masukkan Deskripsi: "+ "\n")
            new_consumable_jumlah = int(input("Masukkan Jumlah: "+ "\n"))
            new_consumable_rarity = input("Masukkan Rarity: "+ "\n")
            if (new_consumable_jumlah <=0): #jumlah item valid hanya jika bernilai positif
                bisa_tambahitem = False
                print("\n Input jumlah tidak valid!\n")
            if new_consumable_rarity not in TabRarity:
                bisa_tambahitem = False #rarity valid hanya jika berupa character pada TabRarity
                print("\n Input rarity tidak valid!\n")
            elif bisa_tambahitem: #memasukan data item consumable baru kedalam list data_consumable_global
                new_consumable = [new_consumable_id, new_consumable_name, new_consumable_deskripsi, new_consumable_jumlah, new_consumable_rarity]
                data_consumable_global.append(new_consumable)
                print("\n Item telah berhasil ditambahkan ke databese \n")
    else:
        print("Gagal menambahkan item karena ID tidak valid") #mengembalikan pesan error jika item baru bukan gadget atau consumable