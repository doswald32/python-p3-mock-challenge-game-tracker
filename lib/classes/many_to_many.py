
class Game:

    all = []

    def __init__(self, title):
        self.title = title
        Game.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not hasattr(self, 'title') and isinstance(value, str) and len(value) > 0:
            self._title = value
        else:
            raise Exception("title must be a string with at least one character.")
    
    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        no_dupes = []
        for result in Result.all:
            if result.game == self:
                if result.player not in no_dupes:
                    no_dupes.append(result.player)
        return no_dupes

    def average_score(self, player):
        scores_total = 0
        games_played = 0
        for result in Result.all:
            if result.player == player:
                scores_total += result.score
                games_played += 1
        avg_score = scores_total / games_played
        return avg_score

class Player:

    all = []

    def __init__(self, username):
        self.username = username
        Player.all.append(self)

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._username = value
        else: 
            raise Exception("value must be a string with 2-16 characters.")

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return [result.game for result in Result.all if result.player == self]

    def played_game(self, game):
        for result in Result.all:
            if result.player == self and result.game.title == game.title:
                return True
        return False
            

    def num_times_played(self, game):
        pass

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        if not hasattr(self, 'score') and isinstance(value, int) and 1 <= value <= 5000:
            self._score = value
        else:
            raise Exception("score must be an interger between 1-5000.")
        
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, value):
        if not hasattr(self, 'player') and isinstance(value, Player):
            self._player = value
        else:
            raise Exception("player must be of class Player.")
        
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, value):
        if not hasattr(self, 'game') and isinstance(value, Game):
            self._game = value
        else: 
            raise Exception("game must be of class Game.")

