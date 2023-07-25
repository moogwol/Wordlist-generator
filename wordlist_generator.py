import random
import datetime
import sys
import argparse



class Randomiser:
    def __init__(self):
        self.swap_dict = self.initialise_dict()

    def initialise_dict(self):
        dict = {}
        dict['A'] = ['4', '^']
        dict['C'] = '('
        dict['E'] = ['3', '£']
        dict['G'] = '6'
        dict['I'] = ['!', '1']
        dict['O'] = '0'
        dict['S'] = ['5', '$']
        dict['T'] = '7'
        dict['Z'] = '2'
        return dict

    def mode(self):
        # return a randomise mode
        choices = ['upper', 'lower', 'swap']
        return random.choice(choices)

    def generate_random_number(self):
        # choose the length of the number
        random_number = ''
        num_length = random.choice([1, 2, 3, 4, 5])

        # loop through numbers 0...9 and add them to the random number string
        num_choices = list(range(0, 10))
        for i in range(num_length):
            num = random.choice(num_choices)
            random_number += str(num)
        return random_number

    def randomise_letter(self, letter):
        # return a randomised version of a given letter
        dict = self.swap_dict
        letter = letter.upper()
        mode = self.mode()
        result = ''
        if letter in dict and mode == 'swap':
            result = (self.swap_dict[letter])
        else:
            if mode == 'upper':
               result = (letter)
            else:
                result = (letter.lower())
        return random.choice(result) # if the result is a dictionary it will choose one randon option from it

    def randomise_word(self, word):
        number = str(self.generate_random_number())
        new_word = ''
        for letter in word:
            new_letter = self.randomise_letter(letter)
            new_word = new_word + new_letter
        return new_word + number

    def generate_wordlist(self, seed, number):
        # Take a seed word and output the specified number of variations to a .txt file
        f = open(f"{seed}.txt", "a")
        for i in range(number):
            word = self.randomise_word(seed) + "\n"
            f.write(word)
        f.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='generates password mutations from a seed word and outputs them to a .txt file')
    parser.add_argument("--seed", help="the seed word to be mutated", default="password")
    parser.add_argument("--number", help="the number of mutations", default=5, type=int)
    args = parser.parse_args()

    Randomiser().generate_wordlist(args.seed, args.number)