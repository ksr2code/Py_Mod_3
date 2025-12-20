#!/usr/bin/env python3
"""
Exercise 6: Data Alchemist
Transform data using comprehensions - Python's elegant magic spells!
"""


def ft_analytics_dashboard():
    """Demonstrate list, dict, and set comprehensions for game analytics."""
    players = {
        "alice": {"level": 42, "total_score": 15420, "sessions_played": 38,
                  "favorite_mode": "ranked", "achievements_count": 6},
        "bob": {"level": 28, "total_score": 9850, "sessions_played": 22,
                "favorite_mode": "competitive", "achievements_count": 4},
        "charlie": {"level": 51, "total_score": 22100, "sessions_played": 45,
                    "favorite_mode": "ranked", "achievements_count": 8},
        "diana": {"level": 19, "total_score": 7200, "sessions_played": 18,
                  "favorite_mode": "casual", "achievements_count": 3},
        "eve": {"level": 35, "total_score": 12500, "sessions_played": 30,
                "favorite_mode": "casual", "achievements_count": 5},
        "frank": {"level": 24, "total_score": 8900, "sessions_played": 25,
                  "favorite_mode": "competitive", "achievements_count": 4}
    }
    sessions = [
        {"player": "alice", "duration_minutes": 45, "score": 2800,
         "mode": "ranked", "completed": True},
        {"player": "bob", "duration_minutes": 30, "score": 1500,
         "mode": "competitive", "completed": True},
        {"player": "charlie", "duration_minutes": 60, "score": 3200,
         "mode": "ranked", "completed": False},
        {"player": "diana", "duration_minutes": 20, "score": 800,
         "mode": "casual", "completed": True},
        {"player": "eve", "duration_minutes": 50, "score": 2100,
         "mode": "casual", "completed": True},
        {"player": "frank", "duration_minutes": 35, "score": 1800,
         "mode": "competitive", "completed": False},
        {"player": "alice", "duration_minutes": 55, "score": 2900,
         "mode": "ranked", "completed": True},
        {"player": "bob", "duration_minutes": 40, "score": 1700,
         "mode": "competitive", "completed": True},
        {"player": "charlie", "duration_minutes": 70, "score": 3500,
         "mode": "ranked", "completed": True},
        {"player": "diana", "duration_minutes": 25, "score": 1000,
         "mode": "casual", "completed": False}
    ]
    achievements = [
        {"player": "alice", "achievement": "first_blood"},
        {"player": "alice", "achievement": "level_master"},
        {"player": "alice", "achievement": "speed_runner"},
        {"player": "bob", "achievement": "first_blood"},
        {"player": "bob", "achievement": "boss_hunter"},
        {"player": "charlie", "achievement": "level_master"},
        {"player": "charlie", "achievement": "boss_hunter"},
        {"player": "charlie", "achievement": "perfectionist"},
        {"player": "charlie", "achievement": "combo_king"},
        {"player": "diana", "achievement": "treasure_seeker"},
        {"player": "eve", "achievement": "explorer"},
        {"player": "eve", "achievement": "pixel_perfect"},
        {"player": "frank", "achievement": "speed_runner"}
    ]

    print("=== Game Analytics Dashboard ===")
    print()
    print("=== List Comprehension Examples ===")

    high_level_players = [
        name for name in players if players[name]["level"] >= 30]
    print("High-level players (30+):", high_level_players)
    all_scores = [session["score"] for session in sessions]
    print("All session scores:", all_scores)
    completed_sessions = [s for s in sessions if s["completed"]]
    print(f"Completed sessions: {len(completed_sessions)}/{len(sessions)}")
    high_scorers = [
        name for name in players if players[name]["total_score"] >= 10000]
    print("High scorers (>= 10000):", high_scorers)
    print()

    print("=== Dict Comprehension Examples ===")

    player_scores = {name: players[name]["total_score"] for name in players}
    print("Player scores:", player_scores)
    player_levels = {name: players[name]["level"] for name in players}
    print("Player levels:", player_levels)
    session_counts = {
        name: sum(1 for s in sessions if s["player"] == name)
        for name in players
    }
    print("Session counts:", session_counts)
    achievement_counts = {
        name: len([a for a in achievements if a["player"] == name])
        for name in players
    }
    print("Achievement counts:", achievement_counts)
    print()

    print("=== Set Comprehension Examples ===")

    active_players = {session["player"] for session in sessions}
    print("Active players:", sorted(active_players))
    unique_achievements = {a["achievement"] for a in achievements}
    print("Unique achievements:", sorted(unique_achievements))
    modes_played = {session["mode"] for session in sessions}
    print("Modes played:", sorted(modes_played))
    players_with_achievements = {a["player"] for a in achievements}
    print("Players with achievements:", sorted(players_with_achievements))
    print()

    print("=== Combined Analysis ===")

    active_high = [
        n for n in {s["player"]
                    for s in sessions} if players[n]["total_score"] >= 10000
    ]
    print(f"Active high scorers: {active_high}")

    players_socres = {n: players[n]["total_score"] for n in players}
    top_score = max(players_socres[n] for n in players_socres)
    top_player = [n for n in players if players[n]
                  ["total_score"] == top_score][0]
    print(f"Top player: {top_player} ({top_score} points)")

    elite = {
        n: {"score": players[n]["total_score"], "achievements": len(
            [a for a in achievements if a["player"] == n])}
        for n in players if players[n]["level"] >= 30
    }
    print(f"Elite players: {elite}")

    active_sum = sum(players[n]["total_score"]
                     for n in {s["player"] for s in sessions})
    print(f"Active total score: {active_sum}")


if __name__ == "__main__":
    ft_analytics_dashboard()
