
class Game:

    all = []

    def __init__(self, title):
        self._title = title
        Game.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if isinstance((value, str) and len(value) > 0):
            self._title = value
        else:
            raise Exception("title must be a string with at least one character.")
    
    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return [player for player in Player.all if player.game == self]

    def average_score(self, player):
        pass

class Player:

    all = []

    def __init__(self, username):
        self._username = username
        Player.all.append(self)

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, value):
        if isinstance((value, str) and (2 <= len(str) <= 16)):
            self._username = value
        else: 
            raise Exception("value must be a string with 2-16 characters.")

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return [game for game in Game.all if game.player == self]

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
        self._player = player
        self._game = game
        self._score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        if isinstance((value, int) and 1 <= value <= 5000):
            self._score = value
        else:
            raise Exception("score must be an interger between 1-5000.")
        
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, value):
        if isinstance(value, Player):
            self._player = value
        else:
            raise Exception("player must be of class Player.")
        
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, value):
        if isinstance(value, Game):
            self_game = value
        else: 
            raise Exception("game must be of class Game.")

