from collections import Counter

class DataAnalyzer:
    def __init__(self):
        self.player_mentions = Counter()

    def analyze(self, text):
        # Check if "To Hit A Home Run" is in the text
        if "To Hit A Home Run" in text:
            return

        # Split the text into words
        words = text.split()

        # Assume that player names are capitalized
        # This is a simplification and may not work for all cases
        player_names = [word for word in words if word.istitle()]

        # Add the player names to our counter
        for player_name in player_names:
            self.player_mentions[player_name] += 1

    def compile_bets(self):
        # For simplicity, let's assume that we will bet on the 3 most mentioned players
        # Again, this is a simplification and may not work for all cases
        most_mentioned_players = self.player_mentions.most_common(3)

        # Compile the bet
        bet = [player for player, mentions in most_mentioned_players]

        return bet

