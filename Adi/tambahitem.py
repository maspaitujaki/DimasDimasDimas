def tambahitem():
    TabId = []
    bisa_tambahitem = True
    TabRarity = ["C", "B", "A", "S"]
    id_item = input("Masukkan ID: "+ "\n")
    TabId.append(id_item)
    if (id_item[0] == 'G'):
        if cek(TabId[0], data_gadget_global, 0):
            TabId = []
            print("\n Gagal menambahkan item karena ID sudah ada")
        else:
            new_gadget_id = TabId[0]
            new_gadget_name = input("Masukkan Nama: "+ "\n")
            new_gadget_deskripsi = input("Masukkan Deskripsi: "+ "\n")
            new_gadget_jumlah = input("Masukkan Jumlah: "+ "\n")
            new_gadget_rarity = input("Masukkan Rarity: "+ "\n")
            new_gadget_tahun = input("Masukkan tahun ditemukan: "+ "\n")
            if new_gadget_rarity not in TabRarity:
                TabId = []
                bisa_tambahitem = False
                print("\n Input rarity tidak valid!\n")
            elif bisa_tambahitem:
                TabId = []
                new_gadget = [new_gadget_id, new_gadget_name, new_gadget_deskripsi, new_gadget_jumlah, new_gadget_rarity, new_gadget_tahun]
                data_gadget_global.append(new_gadget)
                print("\n Item telah berhasil ditambahkan ke databese \n")
    elif (id_item[0] == 'C'):
        if cek(TabId[0], data_consumable_global, 0):
            TabId = []
            print("\n Gagal menambahkan item karena ID sudah ada")
        else:
            new_consumable_id = TabId[0]
            new_consumable_name = input("Masukkan Nama: "+ "\n")
            new_consumable_deskripsi = input("Masukkan Deskripsi: "+ "\n")
            new_consumable_jumlah = input("Masukkan Jumlah: "+ "\n")
            new_consumable_rarity = input("Masukkan Rarity: "+ "\n")
            if new_consumable_rarity not in TabRarity:
                TabId = []
                bisa_tambahitem = False
                print("\n Input rarity tidak valid!\n")
            elif bisa_tambahitem:
                TabId = []
                new_consumable = [new_consumable_id, new_consumable_name, new_consumable_deskripsi, new_consumable_jumlah, new_consumable_rarity]
                data_consumable_global.append(new_consumable)
                print("\n Item telah berhasil ditambahkan ke databese \n")
    else:
        TabId = []
        print("Gagal menambahkan item karena ID tidak valid")