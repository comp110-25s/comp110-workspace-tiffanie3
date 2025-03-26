__author__ = "730471301"

dictionary: dict[str, str] = {"a": "z", "b": "y", "c": "x"}


def invert(dictionary) -> dict[str, str]:
    """when given a dictionary dict[key,value], return dict[value,key]"""
    inverted_dictionary: dict[str, str] = {}
    found: bool == False
    for key in dictionary:
        if not found and value in inverted_dictionary:
            found == True
            raise KeyError("value:key already in dictionary")
        else:
            inverted_directory[value] = key
    print(inverted_dictionary)
    return inverted_dictionary
