inisiasi = input("Apakah sudah mempunyai akun?(y/n)\n>>> ")

if inisiasi == 'Y' or inisiasi == 'y':
    from Account.login import login
else:
    from Account.register import register
    from Account.login import login