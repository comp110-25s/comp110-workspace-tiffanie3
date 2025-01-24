"""Practice with decomposing a problem into smaller subproblems to plan a tea party"""

__author__ = "730471301"


def main_planner(guests: int) -> None:
    """entrypoint to tea party planning program"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    return None


def tea_bags(people: int) -> int:
    """computes # of tea bags based on # of guests"""
    return people * 2


def treats(people: int) -> int:
    """computes the # of treats needed based on the # of teas guests are expected to drink"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """computes the cost of the tea bags and the treats combined"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
