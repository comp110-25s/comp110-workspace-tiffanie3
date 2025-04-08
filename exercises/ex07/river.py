"""File to define River class."""

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        surviving_fish: list[Fish] = []
        for Fish in self.fish:
            if Fish.age <= 3:
                surviving_fish.append(Fish)
        self.fish = surviving_fish

        surviving_bears: list[Bear] = []
        for Bear in self.bears:
            if Bear.age <= 5:
                surviving_bears.append(Bear)
        self.bears = surviving_bears
        return None

    def bears_eating(self):
        return None

    def check_hunger(self):
        return None

    def remove_fish(self, amount: int):
        idx: int = 0
        while idx < amount:
            self.fish.pop(0)
            idx = idx + 1
        return None

    def repopulate_fish(self):
        return None

    def repopulate_bears(self):
        return None

    def view_river(self):
        x: str = str(self.day)
        y: str = str(len(self.fish))
        z: str = str(len(self.bears))
        print(
            "~~~ Day "
            + x
            + " ~~~"
            + "\nFish population: "
            + y
            + " \nBear population: "
            + z
        )
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
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
        for _ in range(7):
            self.one_river_day()
