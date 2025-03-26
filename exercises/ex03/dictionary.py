__author__ = "730471301"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """when given a dictionary dict[key,value], return dict[value,key]"""
    inverted_dictionary: dict[str, str] = {}
    for key in dictionary:
        value: str = dictionary[key]
        if value in inverted_dictionary:
            raise KeyError()
        else:
            inverted_dictionary[value] = key
    print(inverted_dictionary)
    return inverted_dictionary


def count(list: list[str]) -> dict[str, int]:
    """counts the number of times a str appears in a given list, returns dictionary of counts for each str"""
    dictionary_of_counts: dict[str, int] = {}
    idx: int = 0
    while idx < len(list):
        item: str = list[idx]
        if item in dictionary_of_counts:
            dictionary_of_counts[item] += 1
        else:
            dictionary_of_counts[item] = 1
        idx += 1
    print(dictionary_of_counts)
    return dictionary_of_counts


def favorite_color(sample: dict[str, str]) -> str:
    """returns the most popular color from a dictionary with of names and favorite colors"""
    color_list: list[str] = []
    for name in sample:
        color_list.append(sample[name])
    dictionary_color: dict[str, int] = count(color_list)
    idx: int = 0
    while idx < len(dictionary_color):
        for color in dictionary_color:
            color_popular: int = dictionary_color[color_list[idx]]
            if dictionary_color[color] > color_popular:
                print(color)
                return color
            idx += 1
