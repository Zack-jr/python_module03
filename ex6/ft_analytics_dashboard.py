class Player():
    def __init__(self, player_name, player_score, status, achievement_count):
        self.player_name = player_name
        self.player_score = player_score
        self.status = status
        self.achievement_count = achievement_count


def ft_analytics_dashboard():
    """this is a function"""
    print("=== Game Analytics Dashboard ===\n")
    print("=== List Comprehension Examples ===")

    alice = Player("alice", 2700, "active", 6)
    bob = Player("bob", 2100, "inactive", 8)
    charlie = Player("charlie", 1200, "inactive", 2)
    diana = Player("diana", 2800, "active", 10)

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

    print("=== Set Comprehension Examples ===")
    

if __name__ == '__main__':
    ft_analytics_dashboard()



# check si chaque score est superieur a 2000, si le score l'est, alors categoriser en high


# besoin d'un dict avec le nom de chaque joueur en cle et leur
 # score en valeur

 # list comprehension = appliquer une expression a chaque item d'une list/tuple/range
 # ex : newlist = [x for x in fruits if "a" in x]