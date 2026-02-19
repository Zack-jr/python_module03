class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.player_inventory = dict()


def analytics(player_inventory):
    """returns analytics from player inventories"""

    inventory_value = 0
    item_count = 0

    for name in player_inventory:
        data = player_inventory[name]
        item_count += data.get("quantity")
        total_item_value = data["value"] * data["quantity"]
        inventory_value += total_item_value

    return inventory_value, item_count


def find_rarest_items(inventory1, inventory2):
    """find rarest item in both the inventories"""
    rarity_order = ["rare", "uncommon", "common"]
    rarest_found = []

    for rarity in rarity_order:
        for p in [inventory1, inventory2]:
            for item in p.keys():
                if p[item].get("rarity") == rarity:
                    rarest_found.append(item)
        if len(rarest_found) > 0:
            break
    print("Rarest items:", end=" ")
    print(*rarest_found, sep=", ")


def ft_inventory_system():
    """principal function in my program"""
    print("=== Player Inventory System ===\n")
    Alice = Player("Alice")
    Bob = Player("Bob")

    Alice.player_inventory["sword"] = {
        "rarity": "rare",
        "type": "weapon",
        "quantity": 1,
        "value": 500,
    }
    Alice.player_inventory["potion"] = {
        "rarity": "common",
        "type": "consumable",
        "quantity": 5,
        "value": 50,
    }
    Alice.player_inventory["shield"] = {
        "rarity": "uncommon",
        "type": "armor",
        "quantity": 1,
        "value": 200,
    }
    Bob.player_inventory["potion"] = {
        "rarity": "common",
        "type": "consumable",
        "quantity": 0,
        "value": 50,
    }
    Bob.player_inventory["magic_ring"] = {
        "rarity": "rare",
        "type": "accessory",
        "quantity": 1,
        "value": 600,
    }

    inventory_value = 0
    total_items = 0
    print("=== Alice's Inventory ===")
    for name in Alice.player_inventory:
        data = Alice.player_inventory[name]
        total_items += data["quantity"]
        total_item_value = data["value"] * data["quantity"]
        inventory_value += total_item_value
        print(f"{name} ({data['type']}, {data['rarity']}): "
              f"{data['quantity']}x @ {data['value']} "
              f"gold each = {total_item_value} gold")

    print(f"\nInventory value: {inventory_value} gold")
    print(f"Item count: {total_items} items")
    print(f"Categories: {Alice.player_inventory['sword']['type']}"
          f"({Alice.player_inventory['sword']['quantity']}), "
          f"{Alice.player_inventory['potion']['type']}"
          f"({Alice.player_inventory['potion']['quantity']}), "
          f"{Alice.player_inventory['shield']['type']}"
          f"({Alice.player_inventory['shield']['quantity']})\n")

    print("=== Transaction: Alice gives Bob 2 potions ===")
    Alice.player_inventory["potion"].update({"quantity": 3})
    Bob.player_inventory["potion"].update({"quantity": 2})
    print("Transaction successful!\n")

    print("=== Updated Inventories ===")
    print(f"Alice potions: {Alice.player_inventory['potion']['quantity']}")
    print(f"Bob potions: {Bob.player_inventory['potion']['quantity']}\n")

    alice_inventory_value, alice_item_count = analytics(Alice.player_inventory)
    bob_inventory_value, bob_item_count = analytics(Bob.player_inventory)

    print("=== Inventory Analytics ===")
    if bob_inventory_value == alice_inventory_value:
        print(
            f"Most valuable players: Alice ({alice_inventory_value} gold) "
            f"and Bob ({bob_inventory_value} gold)"
        )
    elif bob_inventory_value > alice_inventory_value:
        print(f"Most valuable player: Bob ({bob_inventory_value} gold)")
    else:
        print(f"Most valuable player: Alice ({alice_inventory_value} gold)")
    if bob_item_count == alice_item_count:
        print(f"Most items: Alice ({alice_item_count} "
              f"and Bob ({bob_item_count}))")
    elif bob_item_count > alice_item_count:
        print(f"Most items: Bob ({bob_item_count}) items")
    else:
        print(f"Most items: Alice ({alice_item_count} items)")
    find_rarest_items(Alice.player_inventory, Bob.player_inventory)


if __name__ == "__main__":
    ft_inventory_system()

# dict = list of keys and values
# keys() = get the keys of a dictionnary
# values() = get the values of a dictionnary
# items = get the keys and values of a dictionnary
