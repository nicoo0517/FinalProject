# def test():
#     return "the function works"
import random
def letters():
    consonants =["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
    return random.sample(consonants, 5)
def letters2():
    vowels = ["a", "e", "i", "o", "u", "y"]
    return random.sample(vowels, 2)