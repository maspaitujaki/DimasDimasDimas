def ayo_hapus_sebaris(array_data, pencari, kolom_pencari):
	"""
		Fungsi digunakan untuk menghapus 1 baris data array_data
	"""
	for line in array_data:
		if line[kolom_pencari] == pencari:
			array_data.remove(line)

def hapusitem():
	id_item = input('Masukkan ID Item : ') #input ID item
	if (id_item[0] == "G"): #jika id berawalan huruf G akan diproses sebagai gadget
		if cek(id_item, data_gadget_global, 0): #mengonfirmasi id gadget ada pada list
			deskripsi_item = ayo_ambil_sebagian(data_gadget_global,id_item, 0, 1) #mengambil data string berupa deskripsi gadget dari ID tersebut
			print('Apakah anda yakin ingin menghapus {}'.format(deskripsi_item))
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
			print('Apakah anda yakin ingin menghapus {}'.format(deskripsi_item))
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