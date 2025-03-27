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
    """counts the number of times a str appears in a given list, returns dictionary"""
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
    """returns the most popular color"""
    color_list: list[str] = []
    for name in sample:
        color_list.append(sample[name])
    dictionary_color: dict[str, int] = count(color_list)
    color_popular: str = ""
    color_count: int = 0
    for color in dictionary_color:
        if dictionary_color[color] > color_count:
            color_count = dictionary_color[color]
            color_popular = color
    return color_popular


def bin_len(word_list: list[str]) -> dict[int, set[str]]:
    idx: int = 0
    bin_dict: dict[int, set[str]] = {}
    while idx < len(word_list):
        word: str = word_list[idx]
        length: int = len(word)
        if length in bin_dict:
            bin_dict[length].add(word)
        else:
            bin_dict[length] = {word}
        idx += 1
    return bin_dict
