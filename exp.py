def export_data():
    with open('phone_directory.txt', 'r') as file:
        print(file.read())

def exp_name():
    with open('phone_directory.txt', 'r') as file:
        directory_list = file.readlines()
        for i in directory_list:
            i = i.split(';')
            print(i[1], i[2])