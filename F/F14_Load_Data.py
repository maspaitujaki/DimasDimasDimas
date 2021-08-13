import argparse
parser = argparse.ArgumentParser()
parser.add_argument("nama_folder", type=str, help="this is the file that we want to save")
args = parser.parse_args()


def open_file():
    user_raw = open("user.csv", "r")
    user_lines = user_raw.readlines()
    user_raw.close()
    user = [user_line.replace("\n", "") for user_line in user_lines]
    user.pop(0)

    gadget_raw = open("gadget.csv", "r")
    gadget_lines = gadget_raw.readlines()
    gadget_raw.close()
    gadget = [gadget_line.replace("\n", "") for gadget_line in gadget_lines]
    gadget.pop(0)

    consumable_raw = open("consumable.csv", "r")
    consumable_lines = consumable_raw.readlines()
    consumable_raw.close()
    consumable = [consumable_line.replace("\n", "") for consumable_line in consumable_lines]
    consumable.pop(0)

    consumable_history_raw = open("consumable_history.csv", "r")
    consumable_history_lines = consumable_history_raw.readlines()
    consumable_history_raw.close()
    consumable_history = [consumable_history_line.replace("\n", "") for consumable_history_line in consumable_history_lines]
    consumable_history.pop(0)

    gadget_borrow_history_raw = open("gadget_borrow_history.csv", "r")
    gadget_borrow_history_lines = gadget_borrow_history_raw.readlines()
    gadget_borrow_history_raw.close()
    gadget_borrow_history = [gadget_borrow_history_line.replace("\n", "") for gadget_borrow_history_line in gadget_borrow_history_lines]
    gadget_borrow_history.pop(0)

    gadget_return_history_raw = open("gadget_return_history.csv", "r")
    gadget_return_history_lines = gadget_return_history_raw.readlines()
    gadget_return_history_raw.close()
    gadget_return_history = [gadget_return_history_line.replace("\n", "") for gadget_return_history_line in gadget_return_history_lines]
    gadget_return_history.pop(0)



    


if args.nama_folder=="folder_csv":
    open_file()
    print("Loading", end='')
    for i in range(3):
        print(end=''+'.')
print()
print("Selamat Datang!")
    