#!/usr/bin/env python3
"""
Exercise 3: Achievement Hunter
Track and analyze player achievements using sets.
"""


def ft_achievement_tracker():
    """Demonstrate set operations for achievement tracking."""
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
               'perfectionist'}

    print("=== Achievement Tracker System ===\n")
    players = [('alice', alice), ('bob', bob), ('charlie', charlie)]
    for player, achievement in players:
        print(f"Player {player} achievements: {achievement}")

    print("\n=== Achievement Analytics ===")
    all_achievements = alice.union(bob).union(charlie)
    print(
        f"All unique achievements: {all_achievements}\n"
        f"Total unique achievements: {len(all_achievements)}\n"
    )

    common_achievements = alice.intersection(bob).intersection(charlie)
    print(f"Common to all players: {common_achievements}")

    rare_achievements = set()
    for achievement in all_achievements:
        count = 0
        for _, player_achievements in players:
            if achievement in player_achievements:
                count += 1
        if count == 1:
            rare_achievements = rare_achievements.union({achievement})
    print(f"Rare achievements (1 player): {rare_achievements}\n")

    print(
        f"Alice vs Bob common: {alice.intersection(bob)}\n"
        f"Alice unique: {alice.difference(bob)}\n"
        f"Bob unique: {bob.difference(alice)}"
    )


if __name__ == "__main__":
    ft_achievement_tracker()
