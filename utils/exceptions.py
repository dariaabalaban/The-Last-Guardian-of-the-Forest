class GameException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class InvalidCommandError(GameException):
    pass

class GameOverException(GameException):
    pass

