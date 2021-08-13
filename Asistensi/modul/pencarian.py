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
