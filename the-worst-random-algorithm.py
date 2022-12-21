# Joshua Jerred 12-21-2022
# Rock Paper Scissors Tournament
# For if you ever need an algorithm to get a 'random item' from a list of items, but you require a big O of O(Yes)

import random

# Tournament -> Match -> Round

class Player:
    def __init__(self, name):
        self.name = name
        self.choice = None
        self.matches_won = 0
        self.rounds_won = 0
        self.score = 0
        self.choices = ['Rock', 'Paper', 'Scissors']

    def __str__(self):
        return self.name

    def choose(self)->str:
        self.choice = random.choice(self.choices)
        return self.choice

class Match:
    """Best of 3 match between two players."""
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
        self.player1.rounds_won = 0
        self.player2.rounds_won = 0
        self.winner = None
        self.loser = None

    def play(self):
        while self.player1.rounds_won < 2 and self.player2.rounds_won < 2:
            self.player1.choose()
            self.player2.choose()
            self._round()
        if self.player1.rounds_won == 2:
            self.winner = self.player1
            self.loser = self.player2
        elif self.player2.rounds_won == 2:
            self.winner = self.player2
            self.loser = self.player1
        else:
            print("Something went wrong", self.player1.rounds_won, self.player2.rounds_won)
        self.winner.matches_won += 1
        return self.winner

    def _round(self):
        round_winner = None
        while round_winner is None:
            if self.player1.choice == self.player2.choice:
                self.winner = None
                self.player1.choose()
                self.player2.choose()
            elif self.player1.choice == "Rock" and self.player2.choice == "Scissors":
                round_winner = self.player1
            elif self.player1.choice == "Paper" and self.player2.choice == "Rock":
                round_winner = self.player1
            elif self.player1.choice == "Scissors" and self.player2.choice == "Paper":
                round_winner = self.player1
            else:
                round_winner = self.player2
            
        round_winner.rounds_won += 1
        round_winner.score += 1

class Tournament:
    """Pass in a list of player names."""
    def __init__(self, players: list):
        self.players = [Player(player) for player in players]
        self.total_players = len(self.players)
        if self.total_players % 2 != 0:
            raise ValueError("Must have an even number of players.")
        self.winner = None
        self.total_rounds = 0

    def play(self):
        """Play the tournament."""
        #print("Tournament started with " + str(self.total_players) + " players:")
        #for player in self.players: print(str(player) + " ", end=' ')
        #print()
        while len(self.players) > 1:
            self.tournament_round()
            #print("Round " + str(self.total_rounds) + " complete. Players remaining: " + str(len(self.players)))
            #for player in self.players: print(str(player) + " ", end=' ')

        #print()
        #print("After " + str(self.total_rounds) + " rounds, the winner of the tournament is: " + str(self.players[0]) + " with a score of " + str(self.players[0].score) + "!")
        return self.players[0].name

    def tournament_round(self):
        """Round robin tournament."""
        self.total_rounds += 1
        new_players = []

        if len(self.players) % 2 != 0:
            """Find the player with the highest score and give them a bye.
               If there are multiple players with the same score, pick one at random."""
            i = 0
            high_score = 0
            for player in self.players:
                if player.score > high_score:
                    high_score = player.score
                i += 1
            
            high_score_players_index = []
            for player_index in range(len(self.players)):
                if self.players[player_index].score == high_score:
                    high_score_players_index.append(player_index)
            
            bye_player_index = random.choice(high_score_players_index)
            new_players.append(self.players.pop(bye_player_index))
            #print("Player: " + new_players[0].name + " has been given a bye.")
            #new_players.append(self.players.pop(high_score_index)) # add player with the highest score (Or the first one if there is a tie)



        while len(self.players) > 0:
            player1 = self.players.pop(0)
            player2 = self.players.pop(0)
            match = Match(player1, player2)
            winner = match.play()
            new_players.append(winner)
            total_rounds = match.player1.rounds_won + match.player2.rounds_won
            #print("After " + str(total_rounds) + " rounds, " + str(match.winner) + " won the match. " + str(match.loser) + " has been eliminated.")

        self.players = new_players


def main():
    word_list = []
    with open("/usr/share/dict/words") as f:
        for line in f:
            word_list.append(line.strip())
    random.shuffle(word_list)

    if len(word_list) % 2 != 0:
        word_list.pop()
    tournament = Tournament(word_list)
    print(tournament.play())


main()
