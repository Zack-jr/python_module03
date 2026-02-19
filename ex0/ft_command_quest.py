import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    ac = len(sys.argv)
    if ac == 1:
        print("No arguments provided!")
        print(f"Program name = {sys.argv[0]}")
        print(f"Total arguments: {ac}")
    else:
        print(f"Program name: {sys.argv[0]}")
        print(f"Argument received: {ac - 1}")
        i = 1
        while i < ac:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
        print(f"Total arguments: {ac}")
