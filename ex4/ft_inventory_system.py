#!/usr/bin/env python3
"""
Exercise 4: Inventory Master
Manage and analyze player inventories using dictionaries.
"""


def calculate_stats(inventory: dict) -> dict:
    """Calculate inventory statistics."""
    total_value = 0
    total_items = 0
    category_dict = {}
    inventory_str = ""

    for item_name, details in inventory.items():
        item_value = details["quantity"] * details["value"]
        total_value += item_value
        total_items += details["quantity"]

        category = details["type"]
        current = category_dict.get(category, 0)
        category_dict[category] = current + details["quantity"]

        inventory_str += (
            f"{item_name} ({details['type']}, {details['rarity']}): "
            f"{details['quantity']}x @ {details['value']} gold each = "
            f"{item_value} gold\n"
        )

    categories = "Categories:"
    first = True
    for cat, qty in category_dict.items():
        if not first:
            categories += ","
        categories += f" {cat}({qty})"
        first = False

    return {
        "total_value": total_value,
        "total_items": total_items,
        "categories": categories,
        "inventory": inventory_str
    }


def add_item(item_type: str, rarity: str, quantity: int, value: int) -> dict:
    """Create item details dictionary."""
    return {
        "type": item_type,
        "rarity": rarity,
        "quantity": quantity,
        "value": value
    }


def ft_inventory_system():
    """Demonstrate dictionary operations with player inventory."""
    bob_inventory = {}
    alice_inventory = {}
    bob_inventory["potion"] = add_item("consumable", "common", 0, 50)
    alice_inventory["sword"] = add_item("weapon", "rare", 1, 500)
    alice_inventory["potion"] = add_item("consumable", "common", 5, 50)
    alice_inventory["shield"] = add_item("armor", "uncommon", 1, 200)

    print("=== Player Inventory System ===")
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
    alice_potions = alice_inventory.get("potion", {}).get("quantity", 0)
    bob_potions = bob_inventory.get("potion", {}).get("quantity", 0)
    alice_inventory["potion"].update({"quantity": alice_potions - 2})
    bob_inventory["potion"].update({"quantity": bob_potions + 2})
    print("Transaction successful!")

    print()
    print("=== Updated Inventories ===")
    stats_alice = calculate_stats(alice_inventory)
    alice_potions = alice_inventory.get("potion", {}).get("quantity", 0)
    bob_potions = bob_inventory.get("potion", {}).get("quantity", 0)
    print(
        f"Alice potions: {alice_potions}\n"
        f"Bob potions: {bob_potions}"
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
