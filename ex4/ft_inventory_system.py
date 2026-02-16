class Player():
    def __init__(self, player_name):
        self.player_name = player_name
        self.player_inventory = dict()


def ft_inventory_system():
    print("=== Player Inventory System ===\n")
    Alice = Player("Alice")
    Bob = Player("Bob")

    players = [Alice, Bob]
    Alice.player_inventory["sword"] = {"rarity" : "rare", "type" : "weapon", "quantity" : 1, "value" : 500}
    Alice.player_inventory["potion"] = {"rarity" : "common", "type" : "consumable", "quantity" : 5, "value" : 50}
    Alice.player_inventory["shield"] = {"rarity" : "uncommon", "type" : "armor", "quantity" : 1, "value" : 200}
    Bob.player_inventory["potion"] = {"rarity" : "common", "type" : "consumable", "quantity" : 0, "value" : 50}
    Bob.player_inventory["magic ring"] = {"rarity" : "rare", "type" : "accessory", "quantity" : 1, "value" : 600}

    inventory_value = 0
    total_items = 0

    print("=== Alice's inventory ===")
    for name in Alice.player_inventory:
        data = Alice.player_inventory[name]
        total_items += data['quantity']
        total_item_value = data['value'] * data['quantity']
        inventory_value += total_item_value
        print(f"{name} ({data['type']}, {data['rarity']}): {data["quantity"]}x @ {data['value']} gold each = {total_item_value} gold")

    print(f"\nInventory value: {inventory_value} gold")
    print(f"Item count: {total_items} items")
    print(f"Categories: {Alice.player_inventory["sword"]["type"]}({Alice.player_inventory["sword"]["quantity"]}), {Alice.player_inventory["potion"]["type"]}({Alice.player_inventory["potion"]["quantity"]}), {Alice.player_inventory["shield"]["type"]}({Alice.player_inventory["shield"]["quantity"]})\n")

    print(f"=== Transaction: Alice gives Bob 2 potions")
    Alice.player_inventory["potion"]["quantity"] -= 2
    total_items -= 2
    Bob.player_inventory["potion"]["quantity"] += 2
    print("Transaction successful!\n")

    print("=== Updated Inventories ===")
    print(f"Alice potions: {Alice.player_inventory['potion']['quantity']}")
    print(f"Bob potions: {Bob.player_inventory['potion']['quantity']}\n")

    total_item_value = 0
    inventory_value = 0
    for name in Alice.player_inventory:
    
        data = Alice.player_inventory[name]
        total_item_value = data['value'] * data['quantity']
        inventory_value += total_item_value
    
    print("\n\n\n")

    for player in players:

        print(player.player_inventory)
        for item in player.player_inventory.values():
            print(item['rarity'])
    
    print("=== Inventory Analytics ===")
    print(f"Most valuable player: Alice ({inventory_value} gold)")
    print(f"Most items: Alice ({total_items})")
    print(f"Rarest items: , magic_ring")

         

if __name__ == '__main__':
    ft_inventory_system()
