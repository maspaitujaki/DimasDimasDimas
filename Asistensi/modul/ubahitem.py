def modify_datas(array_data, pencari, kolom_pencari, kolom_dicari, value):
	"""
		Fungsi untuk mengubah nilai kolom tertentu pada array_data
	"""
	for line in array_data:
		if line[kolom_pencari] == pencari:
			line[kolom_dicari] = value
	return

def ubahitem(): #fungsi untuk mengubah jumlah item (ADMIN)
	id_item = input("Masukan ID: ") #input ID item
	if cek(id_item, data_gadget_global, 0): # jika id berada pada list gadget.csv
		tambah_jumlah = int(input("Masukan Jumlah: "))  #jumlah item tambahan
		jumlah_lama = ayo_ambil_sebagian(data_gadget_global, id_item, 0, 3) #jumlah item sebelum penambahan
		new_jumlah = jumlah_lama + tambah_jumlah #jumlah akhir item
		deskripsi_item = ayo_ambil_sebagian(data_gadget_global,id_item, 0, 1) #mengambil string deskripsi item sesuai ID
		if (new_jumlah >= 0): #kondisi valid ketika jumlah akhir item pada data tidak negatif
			modify_datas(data_gadget_global, id_item, 0, 3, new_jumlah) #modifikasi kolom jumlah item
		else:
			print(str((abs(tambah_jumlah))) + ' {} gagal dibuang karena stok kurang. Stok sekarang : '.format(deskripsi_item) + str(jumlah_lama) + '( < {})'.format(abs(tambah_jumlah)))
	elif cek(id_item, data_consumable_global, 0): #jika id berada pada list consumable.csv
		tambah_jumlah = int(input("Masukan Jumlah: ")) #jumlah item tambahan
		jumlah_lama = ayo_ambil_sebagian(data_consumable_global, id_item, 0, 3) #jumlah item sebelum penambahan
		new_jumlah = jumlah_lama + tambah_jumlah #jumlah akhir item
		deskripsi_item = ayo_ambil_sebagian(data_consumable_global,id_item, 0, 1) #mengambil string deskripsi item sesuai ID
		if (new_jumlah >= 0): #kondisi valid ketika jumlah akhir item pada data tidak negatif
			modify_datas(data_consumable_global, id_item, 0, 3, new_jumlah) #modifikasi kolom jumlah item
		else:
			print(str((abs(tambah_jumlah))) + ' {} gagal dibuang karena stok kurang. Stok sekarang : '.format(deskripsi_item) + str(jumlah_lama) + '( < {})'.format(abs(tambah_jumlah)))
	else:
		print(' \nTidak ada item dengan ID tersebut! \n') #Input ID diproses hanya jika id berawalan huruf G atau C