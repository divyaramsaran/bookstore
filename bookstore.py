def addInventory (inventory) :
    book = input('Enter An Inventory To Add:')
    inventory.append(book)
    return inventory

def removeInventory (inventory) :
    inventoryToRemove = input('Enter A Book To Remove')
    if (inventoryToRemove in inventory) :
        inventory.remove(inventoryToRemove)
        return inventory
    print('The Book You Entered Is Not Present In Inventory')
    return None


def questionsAndAnswers(inventory,harryWishList, bobWishList):
    print('Total Unique Books In Wishlists:', len(harryWishList.union(bobWishList)))
    print('Books In Both Wishlists:', harryWishList.intersection(bobWishList))
    print('Books In Harry\'s Wishlist But Not In Bob\'s:', harryWishList.difference(bobWishList))
    print('Books In Bob\'s Wishlist But Not In Harry\'s:', bobWishList.difference(harryWishList))
    print('Wishlists Combined:', harryWishList | bobWishList)
    print('Books That No Customer Wished:', set(inventory) - (harryWishList | bobWishList))


def main() :
    inventory = ['Harry Potter', 'The Alchemist', 'Atomic Habits', 'Clean Code', 'Python Crash Course']
    harryWishList = {'Harry Potter', 'Deep Work', 'Clean Code'}
    bobWishList = {'Atomic Habits', 'Clean Code', 'The Pragmatic Programmer'}
    
    print('Welcome to the Bookstore Inventory System')
    print('Current Inventory:', inventory)
    print('Harry\'s Wishlist:', harryWishList)
    print('Bob\'s Wishlist:', bobWishList)
    option = int(input('Choose an option: \n1. Add Inventory\n2. Remove Inventory\n3. Exit\n'))

    match option:
        case 1:
            inventory = addInventory(inventory)
            print('Updated Inventory:', inventory)
        case 2:
            inventory = removeInventory(inventory)
            print('Updated Inventory:', inventory)
        case _:
            print('Enter A Valid Option')
    questionsAndAnswers(inventory, harryWishList, bobWishList)

main()