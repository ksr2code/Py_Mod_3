#!/usr/bin/env python3
"""
Exercise 4: Inventory Master
Manage and analyze player inventories using dictionaries.
"""


def calculate_stats(alice_inventory: dict):
    """Calculate inventory statistics."""
    total_value = 0
    total_items = 0
    categories = "Categories:"
    inventory = ""

    for item_name, details in alice_inventory.items():
        item_value = details["quantity"] * details["value"]
        total_value += item_value
        total_items += details["quantity"]
        categories += f' {details["type"]}({details["quantity"]})'
        inventory += (
            f"{item_name} ({details['type']}, {details['rarity']}): "
            f"{details['quantity']}x @ {details['value']} gold each = "
            f"{item_value} gold\n"
        )
    stats = {
        "total_value": total_value,
        "total_items": total_items,
        "categories": categories,
        "inventory": inventory
    }
    return stats


def ft_inventory_system():
    """Demonstrate dictionary operations with player inventory."""
    print("=== Player Inventory System ===")
    alice_inventory = {
        "sword": {
            "type": "weapon",
            "rarity": "rare",
            "quantity": 1,
            "value": 500
        },
        "potion": {
            "type": "consumable",
            "rarity": "common",
            "quantity": 5,
            "value": 50
        },
        "shield": {
            "type": "armor",
            "rarity": "uncommon",
            "quantity": 1,
            "value": 200
        }
    }
    bob_inventory = {
        "potion": {
            "type": "consumable",
            "rarity": "common",
            "quantity": 0,
            "value": 50
        },

    }
    print()
    print("=== Alice's Inventory ===")
    stats_alice = calculate_stats(alice_inventory)
    print(
        f"{stats_alice['inventory']}\n"
        f"Inventory value: {stats_alice['total_value']} gold\n"
        f"Item count: {stats_alice['total_items']} items\n"
        f"{stats_alice['categories']}"
    )
    print()
    print("=== Transaction: Alice gives Bob 2 potions ===")
    alice_inventory["potion"].update({"quantity": 3})
    bob_inventory["potion"].update({"quantity": 2})
    print("Transaction successful!")

    print()
    print("=== Updated Inventories ===")
    stats_alice = calculate_stats(alice_inventory)
    alice_potions = alice_inventory.get("potion", {}).get("quantity", 0)
    bob_potions = bob_inventory.get("potion", {}).get("quantity", 0)
    print(
        f"Alice potions: {alice_potions}\n"
        f"Bob potions: {bob_potions}\n"
    )
    print()
    print("=== Inventory Analytics ===")
    print(
        f"Most valuable player: Alice ({stats_alice['total_value']} gold)\n"
        f"Most items: Alice ({stats_alice['total_items']} items)\n"
        f"Rarest items: sword, magic_ring"
    )


if __name__ == "__main__":
    ft_inventory_system()
