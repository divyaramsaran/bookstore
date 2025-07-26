def addInventory (inventory) :
    book = input('Enter An Inventory To Add:')
    inventory.append(book)
    return inventory


def main() :
    inventory = ['Harry Potter', 'The Alchemist', 'Atomic Habits', 'Clean Code', 'Python Crash Course']
    harryWishList = {'Harry Potter', 'Deep Work', 'Clean Code'}
    bobWishList = {'Atomic Habits', 'Clean Code', 'The Pragmatic Programmer'}

    inventory = addInventory(inventory)
    print(inventory)

main()