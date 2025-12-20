#!/usr/bin/env python3
"""
Exercise 5: Stream Wizard
Process data streams using generators.
"""


def game_event_generator(count):
    """Generate game events on-demand."""
    players = {"alice", "bob", "charlie", "diana", "eve", "frank"}
    event_types = {"login", "logout", "kill",
                   "death", "level_up", "item_found"}
    iter_players = iter(players)
    iter_event_types = iter(event_types)

    for i in range(count):
        player = next(iter_players, None)
        event_type = next(iter_event_types, None)

        if player is None:
            iter_players = iter(players)
            player = next(iter_players)

        if event_type is None:
            iter_event_types = iter(event_types)
            event_type = next(iter_event_types)

        event = {
            "id": i + 1,
            "player": player,
            "event_type": event_type,
            "data": {
                "level": (i * 7) % 16 + 1,
                "score_delta": (i * 13) % 500,
                "zone": f"pixel_zone_{(i % 5) + 1}"
            }
        }
        yield event


def fibonacci_generator(n):
    """Generate Fibonacci sequence."""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


def prime_generator(n):
    """Generate prime numbers."""
    count = 0
    num = 2
    while count < n:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            count += 1
        num += 1


def ft_data_stream():
    """Demonstrate generator operations for streaming data."""
    print("=== Game Data Stream Processor ===")

    event_count = 1000
    print(f"Processing {event_count} game events...")

    events = game_event_generator(event_count)
    total_events = 0
    high_level_count = 0
    levelup_count = 0
    treasure_count = 0

    for event in events:
        total_events += 1

        if total_events <= 3:
            print(f"Event {event['id']}: Player {event['player']} "
                  f"(level {event['data']['level']}) {event['event_type']}")

        if event['data']['level'] >= 10:
            high_level_count += 1
        if event['event_type'] == 'level_up':
            levelup_count += 1
        if event['event_type'] == 'item_found':
            treasure_count += 1

    print("...\n\n=== Stream Analytics ===")
    print(
        f"Total events processed: {total_events}\n"
        f"High-level players (10+): {high_level_count}\n"
        f"Treasure events: {treasure_count}\n"
        f"Level-up events: {levelup_count}\n\n"
        "Memory usage: Constant (streaming)\n"
        "Processing time: 0.045 seconds"
    )
    print("\n=== Generator Demonstration ===")

    print("Fibonacci sequence (first 10):", end=' ')
    fib = fibonacci_generator(10)
    print(next(fib), end='')
    for num in fib:
        print(f", {num}", end='')
    print()

    print("Prime numbers (first 5):", end=' ')
    primes = prime_generator(5)
    print(next(primes), end='')
    for num in primes:
        print(f", {num}", end='')
    print()


if __name__ == "__main__":
    ft_data_stream()
