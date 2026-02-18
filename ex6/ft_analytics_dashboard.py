class Player():
    def __init__(self, player_name, player_score, status, achievement_count):
        self.player_name = player_name
        self.player_score = player_score
        self.status = status
        self.achievement_count = achievement_count
        self.achievements = set()


def get_score(player):
    return player.player_score

def ft_analytics_dashboard():
    """this is a function"""
    print("=== Game Analytics Dashboard ===\n")
    print("=== List Comprehension Examples ===")

    alice = Player("alice", 2700, "active", 6)
    bob = Player("bob", 2100, "inactive", 5)
    charlie = Player("charlie", 1200, "inactive", 2)
    diana = Player("diana", 2800, "active", 8)

    old_list = [alice, bob, charlie, diana]
    high_scores = [x.player_name for x in old_list if x.player_score > 2000]
    scores_doubled = [(x.player_score  * 2)for x in old_list]
    active_players = [x.player_name for x in old_list if x.status == "active"]

    print(f"High scorers (>2000): {high_scores}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {active_players}\n")

    print("=== Dict Comprehension Examples ===")

    categories = ["high", "medium", "low"]
    score_dict = {alice.player_name : alice.player_score, bob.player_name : bob.player_score, charlie.player_name : charlie.player_score, diana.player_name : diana.player_score}
    player_score_categories = {c : sum(1 for score in score_dict.values() if ("high" if score > 2000 else "medium" if score > 1000 else "low") == c) for c in categories}

    achievements = {p.player_name : p.achievement_count for p in old_list}

    print(f"Player scores: {score_dict}")
    print(f"Score categories: {player_score_categories}")
    print(f"Achievement counts: {achievements}")

    print("\n=== Set Comprehension Examples ===")

    alice.achievements = {"level_10", "level_20", "dragon_slayer", "magician", "mage", "first_kill"}
    bob.achievements = {"level_10", "gold_stealer", "musician", "boss_slayer", "pirate" }
    charlie.achievements = {"first kill", "first_death"}
    diana.achievements = {"level_10", "level_20", "level_30", "dragon_slayer", "knight", "pirate", "mage", "first_kill"}
    achievement_list = [alice.achievements, bob.achievements, charlie.achievements, diana.achievements]
    region_dict = {"north" : "active", "east": "active", "west" : "inactive", "south" : "inactive", "central": "active"}

    player_set = {alice.player_name, bob.player_name, charlie.player_name, diana.player_name}
    achievement_set = {achievement for player_achievements in achievement_list for achievement in player_achievements}
    active_regions = {region for region, status in region_dict.items() if status == "active"}
    print(player_set)
    print(achievement_set)
    print(active_regions)

    print("\n=== Combined Analysis ===")
    player_count = len(old_list)
    total_unique_achievements = len(achievement_set)
    average_score = (sum(player.player_score for player in old_list) / player_count)

    top_player = max(old_list, key=get_score)
    print(f"Total players: {player_count}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Average score: {average_score}")
    print(f"Top performer: {top_player.player_name} ({top_player.player_score} points, {top_player.achievement_count} achievements)")

if __name__ == '__main__':
    ft_analytics_dashboard()



# check si chaque score est superieur a 2000, si le score l'est, alors categoriser en high


# besoin d'un dict avec le nom de chaque joueur en cle et leur
 # score en valeur

 # list comprehension = appliquer une expression a chaque item d'une list/tuple/range
 # ex : newlist = [x for x in fruits if "a" in x]