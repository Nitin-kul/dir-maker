import os
import shutil

dir_l = input('enter directory location or name:')

if not os.path.exists(dir_l):
    os.mkdir(dir_l)
l = ['multy dir', 'rename', 'copy', 'copy dir', 'remove dir', 'remove file', 'show folder in dir']
for i in l:
    print(f"{l.index(i) + 1}. {i}")
ch = int(input('enter your choice:'))

match ch:
    case 1:
        r = int(input('enter directory range:'))
        dir = input("enter name of directories:")
        # mult dir maker
        for i in range(r):
            os.mkdir(f"{dir_l}/{dir}{i + 1}")

    case 2:
        # for rename
        dir = input('enter files or file name:')
        n_dir = input("enter new name of directories:")
        r = int(input('enter directory range:'))
        for i in range(r):
            os.rename(f'{dir_l}/{dir}{i + 1}', f"{dir_l}/{n_dir} {i + 1}")

    case 3:
        # for copy file
        f = input('enter file name for copy:')
        shutil.copy(f, f)

    case 4:
        # for copy dir
        d = input("enter directory name for copy:")
        shutil.copytree(d, d)

    case 5:
        # for remove dir
        d = input("enter directory dir name:")
        shutil.rmtree(d)


    case 6:
        # for remove file
        d = input("enter directory file name:")
        os.remove(f'{dir_l}/{d}')

    case _:
        folders = os.listdir(dir_l)
        for folder in folders:
            print(folder)
            print(os.listdir(f'{dir_l}/{folder}'))
