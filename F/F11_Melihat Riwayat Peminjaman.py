def riwayatpinjam(user, gadget, gadget_borrow_history):
    
    def id_to_user(ID):
        for line in user:
            if line[0] == ID:
               return line[2]

    def id_to_gadget(ID):
        for line in gadget:
            if line[0] == ID:
                return line[1]


    from datetime import datetime

    listDate = []
    for entry in gadget_borrow_history:
        if entry[3] in listDate:
            pass
        else:
            listDate.append(entry[3])
    
    listDate.sort()

    gadget_borrow_historysort = []
    for date in listDate:
        for entry in gadget_borrow_history:
            if entry[3] == date: gadget_borrow_historysort.append(entry)

    numofentry = len(gadget_borrow_historysort)
    gadget_borrow_historysort.reverse()
    for index in range(1, numofentry + 1):
        print("ID Peminjaman        :{}".format(gadget_borrow_historysort[index -1][0]))
        print("Nama Pengambil       :{}".format(id_to_user(gadget_borrow_historysort[index -1][1])))
        print("Nama Gadget          :{}".format(id_to_gadget(gadget_borrow_historysort[index -1][2])))
        print("Tanggal Peminjaman   :{}".format(gadget_borrow_historysort[index -1][3]))
        print("Jumlah               :{}".format(gadget_borrow_historysort[index -1][4]))
        print()

        if index %5 == 0:
            if input("Tampilkan yang lain?(Y/N)").lower() == 'y':
                print()
                continue
            else: 
                break

