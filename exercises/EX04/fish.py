"""File to define Fish class."""


class Fish:
    """Creates Fish class with attribute age."""

    age: int

    def __init__(self):
        """Initializes the age of Fish at 0."""
        self.age = 0

    def one_day(self):
        """For each day, Fish ages by 1."""
        self.age = self.age + 1
