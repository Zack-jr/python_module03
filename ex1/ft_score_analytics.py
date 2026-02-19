import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    ac = len(sys.argv)

    if ac == 1:
        print(
            "No scores provided. Usage:"
            " python3 ft_score_analytics.py <score1> <score2> ..."
        )
    else:
        try:
            list = [int(x) for x in sys.argv[1:]]
            players = ac - 1
            total_score = sum(list)
            high_score = max(list)
            low_score = min(list)
            range = high_score - low_score

            print(f"Scores processed: {list}")
            print(f"Total players: {ac - 1}")
            print(f"Total score: {total_score}")
            print(f"Average score: {total_score / players}")
            print(f"High score: {high_score}")
            print(f"Low score: {low_score}")
            print(f"Score range: {range}\n")
        except ValueError:
            print("Please provide valid inputs")
