"""File to define Bear class."""


class Bear:
    age: int
    hunger_score: int

    def __init__(self):
        self.age = 0
        hunger_score = 0
        return None

    def one_day(self):
        self.age = self.age + 1
        return None
