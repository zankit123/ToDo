user_input = 'random'
data = []

def menu():
    print('Menu:')
    print('1, Add an item')
    print('2, Update an item')
    print('3, Mark as done')
    print('4, View items')
    print('5, Exit')

while user_input != '5':
    menu()
    user_input = input('Select your choice:')

    if user_input == '1':
        item = input('What item to be added? ')
        data.append(item)
        print('Added item', item)
    elif user_input == '2':
        old_item = input('Which item you want update? ')
        if old_item in data:
            new_item = input('Enter new item: ')
            data = list(map(lambda x: x.replace(old_item, new_item), data))
            print('Updated item:', new_item)
        else:
            print('This item is not exist in list')
    elif user_input == '3':
        item = input('What item to be marked as done? ')
        if item in data:
            data.remove(item)
            print('Removed item:', item)
        else:
            print('Item does not exist in the list')
    elif user_input == '4':
        print('List of to do items')
        for item in data:
            print(item)
    elif user_input == '5':
        print('Goodbye')
    else:
        print('Wrong input. Pls give input 1,2,3,4 or 5')
