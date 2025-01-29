from hospital_field_names import field_names
from hospital_menu import menu
data_file = 'framework_data.dat'
dict_data = {}  # local data structure
'''
menu_file = 'hospital_menu.cfg'
field_names_file = 'hospital_field_names.py'
fp_field_name = open(field_names_file, 'r')
field_names = eval(fp_field_name.read())
'''


def load_data():
    fp_data = open(data_file, 'r')
    data = eval(fp_data.read())
    for unique_id in data:
        dict_data[unique_id] = data[unique_id]


def save_to_file():
    fp_data = open(data_file, 'w')
    fp_data.write(str(dict_data))
    fp_data.close()
    return 1


def generate_id():
    if len(list(dict_data.keys())) == 0:
        new_id = '2025HK2PY1000001'
    else:
        new_id = '2025HK2PY'+str(int(list(dict_data.keys())[(len(list(dict_data.keys()))) - 1][9:]) + 1)
    return new_id


def save_data():
    new_unique_id = generate_id()
    dict_data[new_unique_id] = {}
    for counter in range(len(field_names) - 1):
        dict_data[new_unique_id][field_names[counter + 1]] = input(f'Enter {field_names[counter + 1]}: ')
    if save_to_file():
        print('Data saved...!')
    else:
        print('Error..!')


def show_data():
    for counter in range(len(field_names)):
        print(f'{field_names[counter]:<20}', end = '')
    print()
    line = '-' * len(field_names) * 20
    print(line)
    for unique_id in dict_data:
        print(f'{unique_id:<20}', end = '')
        for counter in range(len(field_names) - 1):
            print(f'{dict_data[unique_id][field_names[counter + 1]]:<20}', end = '')
        print()
    print(line)


def update_data():
    search_key = input(f'Enter {field_names[0]} to search: ')
    for unique_id in dict_data:
        if unique_id == search_key:
            print(f'{field_names[0]} Found..!')
            while True:
                for counter in range(len(field_names) - 1):
                    print(f'{counter + 1}. Update {field_names[counter + 1]}')
                print(f'{len(field_names)}. Back to menu')
                update_choice = int(input('Enter your choice: '))
                if update_choice == len(field_names):
                    break
                else:
                    dict_data[unique_id][field_names[update_choice]] = input(f'Enter updated {field_names[update_choice]}: ')
    save_to_file()


def delete_data():
    search_key = input(f'Enter {field_names[0]} to close: ')
    status = False
    for unique_id in dict_data:
        if unique_id == search_key:
            status = True

    if status:
        del dict_data[search_key]
    else:
        print(f'{field_names[0]}: {search_key} Not found...!')
    save_to_file()


load_data()
while True:
    # fp_menu = open(menu_file, 'r')
    # menu = fp_menu.read()
    print(menu)
    choice = int(input('Enter your choice: '))
    if choice == 1:
        save_data()
    elif choice == 2:
        show_data()
    elif choice == 3:
        update_data()
    elif choice == 4:
        delete_data()
    elif choice == 5:
        break
    else:
        print('Invalid choice..!')
