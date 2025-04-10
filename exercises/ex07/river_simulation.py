"""Simulate a river"""

__author__ = "730471301"


from exercises.ex07.river import River

my_river: River = River(30, 5)

my_river.view_river()

print(my_river.check_ages)
