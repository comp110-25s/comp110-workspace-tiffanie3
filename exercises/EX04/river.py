"""File to define River class."""

__author__ = "730471301"

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    """Creates class River with attributes day, bears, and fish."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for fish in range(0, num_fish):
            self.fish.append(Fish())
        for bear in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks the age of each fish, fish surviving to next day are <=3."""
        surviving_fish = []
        for fish in self.fish:
            if fish.age <= 3:
                surviving_fish.append(fish)
        self.fish = surviving_fish

        """Checks the age of each bear, bear surviving to next day are <=5."""
        surviving_bears = []
        for bear in self.bears:
            if bear.age <= 5:
                surviving_bears.append(bear)
        self.bears = surviving_bears

    def bears_eating(self):
        """Each bear eats 3 fish if there are more than 5 fish in the river."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(num_fish=3)

    def check_hunger(self):
        """Bears that starve (hunger score <0) do not survive to the next day."""
        surviving_bears = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)
        self.bears = surviving_bears

    def remove_fish(self, amount: int):
        """Fish that are eaten are removed, starting from index 0."""
        idx: int = 0
        while idx < amount:
            self.fish.pop(0)
            idx = idx + 1

    def repopulate_fish(self):
        """Add 4 new fish for each pair of adult fish."""
        adult_fish: int = len(self.fish)
        baby_fish_to_add: int = (adult_fish // 2) * 4
        total_fish = self.fish
        for _ in range(baby_fish_to_add):
            total_fish.append(Fish())
        self.fish = total_fish

    def repopulate_bears(self):
        """Add 1 new bear for each pair of adult bears."""
        adult_bears: int = len(self.bears)
        baby_bears_to_add: int = adult_bears // 2
        total_bears = self.bears
        for _ in range(baby_bears_to_add):
            total_bears.append(Bear())
        self.bears = total_bears

    def view_river(self):
        """Tells you how many fish and bears on each day."""
        x: str = str(self.day)
        y: str = str(len(self.fish))
        z: str = str(len(self.bears))
        print(
            "~~~ Day " + x + " ~~~ \nFish population: " + y + " \nBear population: " + z
        )

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Runs one_river_day 7x for a week."""
        for _ in range(7):
            self.one_river_day()
