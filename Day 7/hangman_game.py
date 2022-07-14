# Hangman Console Game

import random
import time

words = ['abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward', 'axiom', 'azure', 'bagpipes',
         'bandwagon', 'banjo', 'bayou', 'beekeeper', 'bikini', 'blitz', 'blizzard', 'boggle', 'bookworm', 'boxcar',
         'boxful', 'buckaroo', 'buffalo', 'buffoon', 'buxom', 'buzzard', 'buzzing', 'buzzwords', 'caliph', 'cobweb',
         'cockiness', 'croquet', 'crypt', 'curacao', 'cycle', 'daiquiri', 'dirndl', 'disavow', 'dizzying', 'duplex',
         'dwarves', 'embezzle', 'equip', 'espionage', 'euouae', 'exodus', 'faking', 'fishhook', 'fixable', 'fjord',
         'flapjack', 'flopping', 'fluffiness', 'flyby', 'foxglove', 'frazzled', 'frizzled', 'fuchsia', 'funny', 'gabby',
         'galaxy', 'galvanize', 'gazebo', 'giaour', 'gizmo', 'glowworm', 'glyph', 'gnarly', 'gnostic', 'gossip',
         'grogginess', 'haiku', 'haphazard', 'hyphen', 'iatrogenic', 'icebox', 'injury', 'ivory', 'ivy', 'jackpot',
         'jaundice', 'jawbreaker', 'jaywalk', 'jazziest', 'jazzy', 'jelly', 'jigsaw', 'jinx', 'jiujitsu', 'jockey',
         'jogging', 'joking', 'jovial', 'joyful', 'juicy', 'jukebox', 'jumbo', 'kayak', 'kazoo', 'keyhole', 'khaki',
         'kilobyte', 'kiosk', 'kitsch', 'kiwifruit', 'klutz', 'knapsack', 'larynx', 'lengths', 'lucky', 'luxury',
         'lymph', 'marquis', 'matrix', 'megahertz', 'microwave', 'mnemonic', 'mystify', 'naphtha', 'nightclub',
         'nowadays', 'numbskull', 'nymph', 'onyx', 'ovary', 'oxidize', 'oxygen', 'pajama', 'peekaboo', 'phlegm',
         'pixel', 'pizazz', 'pneumonia', 'polka', 'pshaw', 'psyche', 'puppy', 'puzzling', 'quartz', 'queue', 'quips',
         'quixotic', 'quiz', 'quizzes', 'quorum', 'razzmatazz', 'rhubarb', 'rhythm', 'rickshaw', 'schnapps', 'scratch',
         'shiv', 'snazzy', 'sphinx', 'spritz', 'squawk', 'staff', 'strength', 'strengths', 'stretch', 'stronghold',
         'stymied', 'subway', 'swivel', 'syndrome', 'thriftless', 'thumbscrew', 'topaz', 'transcript', 'transgress',
         'transplant', 'triphthong', 'twelfth', 'twelfths', 'unknown', 'unworthy', 'unzip', 'uptown', 'vaporize',
         'vixen', 'vodka', 'voodoo', 'vortex', 'voyeurism', 'walkway', 'waltz', 'wave', 'wavy', 'waxy', 'wellspring',
         'wheezy', 'whiskey', 'whizzing', 'whomever', 'wimpy', 'witchcraft', 'wizard', 'woozy', 'wristwatch', 'wyvern',
         'xylophone', 'yachtsman', 'yippee', 'yoked', 'youthful', 'yummy', 'zephyr', 'zigzag', 'zigzagging', 'zilch',
         'zipper', 'zodiac', 'zombie']

stages = ['''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========
''']
print("Welcome to the hangman game!")

hangman_word = random.choice(words)
# print(hangman_word)
length_of_word = len(hangman_word)

no_of_underscore = ''
for i in range(0, length_of_word):
    no_of_underscore = no_of_underscore + '_'
print(stages[6])
print(f"There are {length_of_word} letters in word.")
print(no_of_underscore)

level = len(stages) - 2
while True:
    user_input = input("Guess any letter from A to Z :").lower()
    # print(user_input)
    position = None
    index = []
    if user_input in hangman_word:
        for i in range(0, length_of_word):
            if hangman_word[i] == user_input:
                index.append(i)
        # print(index)
        for j in index:
            no_of_underscore = no_of_underscore[:j] + user_input + no_of_underscore[j + 1:]
    else:
        if level > 0:
            # print(stages[level])
            print(stages[level])
            level = level - 1
        elif level == 0:
            print(stages[level])
            print(f"Game Over!\nYou hanged a man.\nThe word was {hangman_word}.\nBetter luck next time.")
            time.sleep(5)
            break
    print(no_of_underscore)
    if '_' not in no_of_underscore:
        print(f"\nThe word given was {no_of_underscore}.\nYou have won the game")
        time.sleep(5)
        break