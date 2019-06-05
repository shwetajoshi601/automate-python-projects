stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total+=v
        print(str(v) + ' ' + k)
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, dragonLoot):
    for item in dragonLoot:
        # if the item is not present in the inventory, consider the value as 0 and add 1 for the item
        inventory[item] = inventory.get(item, 0) + 1
    return inventory

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
displayInventory(stuff)
stuff = addToInventory(stuff, dragonLoot)
print('-----------------------------------')
displayInventory(stuff)