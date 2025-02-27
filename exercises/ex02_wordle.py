"""Wordle - practice with while loops"""

__author__ = "730471301"

"""Part 1: contains_char"""


def contains_char(word: str, letter: str) -> bool:
    """determines if a letter (one character) is in word"""
    # lets player know that the letter needs to be 1 character
    assert len(letter) == 1, f"len('{letter}') is not 1"
    # beginning at the start of the word, this while loop keeps comparing letter to characters in word until the index = the length of word
    # it either finds the letter in the word and return True or doesn't and it returns False
    index: int = 0
    while index < len(word):
        if word[index] == letter:
            return True
        index = index + 1
    return False


"""Part 2: emojified"""


def emojified(guess: str, secret: str) -> str:
    """returns a string of colored squares based on the correctness/positioning of letters in guess and secret"""
    # lets player know that the length of the word for guess must be the same as the word for secret
    assert len(guess) == len(secret), "Guess must be same length as secret"
    # we define some variables, which are the type string, initializing them as colored boxes
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    # we start with an empty string. I want to add an emoji for each letter as we iterate through the while loop onto this empty string
    emojis: str = ""
    # we start indexing at 0
    index: int = 0
    # this while loop will continue until we reach the end of the word, when the index # is equal to the length of secret
    while index < len(secret):
        # if the letter at a position in the word guess matches the letter at the same position in secret, I will add a green box to the string called emojis
        if guess[index] == secret[index]:
            emojis = emojis + GREEN_BOX
        # if not, I will add a yellow box if the word contains the letter in a different position or a white box if the letter is not in the word
        else:
            if contains_char(word=secret, letter=guess[index]) == True:
                emojis = emojis + YELLOW_BOX
            if contains_char(word=secret, letter=guess[index]) == False:
                emojis = emojis + WHITE_BOX
        # increases the index by one so we can look at the letter to the right of the letter we just looked at
        index = index + 1
    # after we reach the end of the word, the following line will return my full string of colored boxes
    return emojis


"""Part 3: input_guess"""


def input_guess(n: int) -> str:
    # when you use the input_guess function, you need to specify how many letters, n, that you want in your word
    """inputs word of n length"""
    # this prompts the player to put in a word of length n, and saves the string as variable input_word
    input_word: str = input(f"Enter a {n} character word:")
    # this while loop says that if the length of the word the player chooses is not n, then they need to try again
    while len(input_word) != n:
        input_word = input(f"That wasn't {n} chars! Try again:")
    # if the word put in by the player matches the length n, then the function returns the word the player put in as a string
    return input_word


"""Part 4: main"""


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    # this function will combine all of my previous functions to make my wordle game when called
    # here, I'm defining the first turn playing as integer 1, and defining n as the length of the secret word, which the player will guess
    turn: int = 1
    n = len(secret)
    # the following while loop will continue until the player runs out of turns (reaches 6 turns) or guesses the secret word correctly
    while turn <= 6:
        # this prints which turn the player is on
        print(f"=== Turn {turn}/6 ===")
        # guess is defined as the word that the player guesses, which uses function input_guess to make sure it is the same length n as the secret word, otherwise it will tell the player to try again
        guess: str = input_guess(n)
        # then, the function emojified will return a string of colored boxes which tell the player which letters in the word they guessed are in the correct position (green box), in the word but in a different position (yellow box), or just not in the secret word at all (white box)
        print(emojified(guess=guess, secret=secret))
        # if the guessed word matches the secret word, then the printed statement lets the player know that they have won the game
        if secret == guess:
            return print(f"You won in {turn}/6 turns!")
        # if the player did not win the game, then they get to try again on their next turn
        turn = turn + 1
    # once the player reaches 6 turns, they have run out of turns and this printed statement lets them know to try again tomorrow
    return print("X/6 - Sorry, try again tomorrow!")


# this part makes the program a module that you can import
"""make it a module"""
if __name__ == "__main__":
    main(secret="codes")

""""Part 5: style and documentation"""
# see annotations above

"""Part 6: Type safety"""
# ok
