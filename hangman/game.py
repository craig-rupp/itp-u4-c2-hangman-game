from hangman.exceptions import *

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    pass


def _mask_word(word):
    pass


def _uncover_word(answer_word, masked_word, character):
    if answer_word == '' or masked_word == '':
        raise InvalidWordException('You must enter both words')
    if len(character) > 1:
        raise InvalidGuessedLetterException('One only please')
    if len(answer_word) != len(masked_word):
        raise InvalidWordException('Same length for first two please')
    
    rt_string = ''
    for idx, val in enumerate(answer_word):
        if val == character:
            rt_string += val
        else:
            rt_string += '*'
    return rt_string
# print(_uncover_word('Python', '******', 'y'))

def guess_letter(game, letter):
    pass


def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [],
        'remaining_misses': number_of_guesses,
    }

    return game
