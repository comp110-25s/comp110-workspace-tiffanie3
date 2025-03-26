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
