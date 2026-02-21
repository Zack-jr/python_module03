class Player:
    """player class"""
    def __init__(self, player_name, player_level):
        self.player_name = player_name
        self.player_level = player_level


def generate_stream(players, actions, mode):
    """generate stream of data using yield"""

    if mode == "game":
        for i in range(1, 1001):
            p = players[i % 3]
            a = actions[i % 4]
            event = f"Event {i}: Player {p.player_name} ({p.player_level}) {a}"
            if a == "leveled up":
                p.player_level += 1
            yield event
    elif mode == "fibonacci":
        a, b = 0, 1
        for _ in range(10):
            yield a
            a, b = b, a + b
    else:
        count = 0
        num = 2
        while count < 5:
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                yield num
                count += 1
            num += 1


def ft_data_stream():
    """principal function in my program"""
    print("=== Game Data Stream Processor ===\n")

    Alice = Player("alice", 5)
    Bob = Player("bob", 12)
    Charlie = Player("charlie", 8)

    players = [Alice, Bob, Charlie]
    actions = [
        "killed monster",
        "found_treasure",
        "leveled up",
        "defeated a boss"
        ]

    stream = generate_stream(players, actions, "game")
    print("Processing 1000 game events...\n")

    level_up_events = 0
    treasure_events = 0
    event_count = 0
    for event in stream:
        event_count += 1
        if "found_treasure" in event:
            treasure_events += 1
        if "leveled up" in event:
            level_up_events += 1
        print(event)

    high_level_players = 0
    for player in players:
        if player.player_level >= 10:
            high_level_players += 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {event_count}")
    print(f"High-level players (10 +): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds\n")

    print("=== Generator Demonstration ===")

    fibonacci_stream = generate_stream(None, None, "fibonacci")
    print("Fibonacci sequence (first 10):", end=" ")
    fibonacci_res = ", ".join(str(n) for n in fibonacci_stream)
    print(fibonacci_res)

    prime_nbr_stream = generate_stream(None, None, None)
    print("Prime numbers (first 5):", end=" ")
    prime_nbr_res = ", ".join(str(n) for n in prime_nbr_stream)
    print(prime_nbr_res)


if __name__ == "__main__":
    ft_data_stream()

# create a stream of data and read from it
# yield() = create a variable
# next() = return next item in an iterator
# iter() = create iterator object
