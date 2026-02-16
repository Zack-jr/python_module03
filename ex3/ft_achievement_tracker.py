class Player():
    def __init__(self, name):
        self.name = name
        self.achievements = set()


def ft_achievement_tracker():
    print("=== Achievement Tracker System ===\n")

    Alice = Player("alice")
    Bob = Player("bob")
    Charlie = Player("charlie")
    Alice.achievements = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
    Bob.achievements = {"first_kill", "level_10", "boss_slayer", "collector"}
    Charlie.achievements = {"level_10", "treasure_hunter", "boss_slayer", "speed_demon", "perfectionist"}

    print(f"Player {Alice.name} achievements: {Alice.achievements}")
    print(f"Player {Bob.name} achievements: {Bob.achievements}")
    print(f"Player {Charlie.name} achievements: {Charlie.achievements}\n")

    print("=== Achievement Analyctics ===")

    unique_achievements = Alice.achievements.union(Bob.achievements, Charlie.achievements)
    common_achievements = Alice.achievements.intersection(Bob.achievements, Charlie.achievements)

    rare_alice = Alice.achievements.difference(Bob.achievements, Charlie.achievements)
    rare_bob = Bob.achievements.difference(Alice.achievements, Charlie.achievements)
    rare_charlie = Charlie.achievements.difference(Alice.achievements, Bob.achievements)
    rare_achievements = rare_alice.union(rare_bob, rare_charlie)

    print(f"All unique achievements: {unique_achievements}")
    print(f"Total unique achievements: {len(unique_achievements)}\n")

    print(f"Common to all players: {common_achievements}")
    print(f"Rare achievements (1 player): {rare_achievements}\n")

    print(f"Alice vs Bob common: {Alice.achievements.intersection(Bob.achievements)}")
    print(f"Alice unique: {Alice.achievements.difference(Bob.achievements)}")
    print(f"Bob unique: {Bob.achievements.difference(Alice.achievements)}")
if __name__ == '__main__':
    ft_achievement_tracker()




# creer des joueurs qui auront des achievements dans un set


# set = unordered tuple without duplicate values