"""
    FILE:       chico_mp4_main.py
    ABOUT:      An implementation that evaluates an infix, prefix, or postfix notaition.

    NAME:       Melzar Jan E. Chico
    COURSE:     CMSC124 B
    DATE:       18 December 2021
    TASK:       Machine Problem 4 - Expressions
"""

from chico_mp4_1 import Converter
from chico_mp4_2 import Evaluator

def main():
    print('Machine Problem 4: Expressions')
    print('by Melzar Jan Chico - CMSC124B')
    userChoice = None

    while userChoice != '3':
        print('\nSelect between:\n\t[1] Convert Notation\n\t[2] Evaluate Notation\n\t[3] Exit')
        userChoice = input('Input selection: ')
        userExpInput = None

        # Branch if user chose to convert a notation to another
        if userChoice == '1':
            print('\n\tInput your strings. Type \'exit\' to go back.')
            print('\tYou can enter infix, prefix, or postfix notations.\n')
            userExpInput = input('\t(#1) Enter expression: ')

            while userExpInput != 'exit':
                try:
                    expToConv = Converter(userExpInput)
                    print()
                    expToConv.display()
                except Exception:
                    print(f'\n\tError: Invalid string input. Please try again.\n')


                userExpInput = input('\t(#1) Enter expression: ')

        # Branch is user chose to evaluate a notation
        elif userChoice == '2':
            print('\n\tInput your strings. Type \'exit\' to go back.')
            print('\tYou can enter infix, prefix, or postfix notations.\n')
            userExpInput = input('\t(#2) Enter expression: ')

            while userExpInput != 'exit':
                try:
                    expToEval = Evaluator(userExpInput)
                    print('\tAnswer: ' + str(expToEval.evaluate()) + '\n')
                except:
                    print(f'\n\tError: Invalid string input. Please try again.\n')

                userExpInput = input('\t(#2) Enter expression: ')

        # Branch if user chose to leave
        elif userChoice == '3':
            print()
            break

        # Branch if user entered an invalid choice
        else:
            print('\n\tError: Invalid choice. Please try again.')


main()