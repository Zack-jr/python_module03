class Player():
    def __init__(self, player_name, player_score, status):
        self.player_name = player_name
        self.player_score = player_score
        self.status = status



def ft_analytics_dashboard():
    print("=== Game Analytics Dashboard ===\n")
    print("=== List Comprehension Example ===")

    alice = Player("alice", 2700, "active")
    bob = Player("bob", 2100, "inactive")
    charlie = Player("charlie", 1200, "inactive")
    diana = Player("diana", 2800, "active")

    old_list = [alice, bob, charlie, diana]
    high_scores = [x.player_name for x in old_list if x.player_score > 2000]
    scores_doubled = [(x.player_score  * 2)for x in old_list]
    active_players = [x.player_name for x in old_list if x.status == "active"]

    print(f"High scorers (>2000): {high_scores}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {active_players}")


if __name__ == '__main__':
    ft_analytics_dashboard()






# besoin d'un dict avec le nom de chaque joueur en cle et leur
 # score en valeur

 # list comprehension = appliquer une expression a chaque item d'une list/tuple/range
 # ex : newlist = [x for x in fruits if "a" in x]