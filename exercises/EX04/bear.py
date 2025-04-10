"""File to define Bear class."""


class Bear:
    """Creates Bear class with attributes age and hunger_score."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initiates Bear at age 0 and hunger 0."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self):
        """Each day, Bear ages by 1 and gets hungrier by 1."""
        self.age = self.age + 1
        self.hunger_score -= 1

    def eat(self, num_fish: int):
        """When Bear eats, hunger score increases by 1."""
        self.hunger_score += num_fish
