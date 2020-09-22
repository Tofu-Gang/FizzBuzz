from sys import exit

################################################################################

if __name__ == "__main__":
    """
    Players generally sit in a circle. The player designated to go first says 
    the number "1", and the players then count upwards in turn. However, any 
    number divisible by three is replaced by the word fizz and any number 
    divisible by five by the word buzz. Numbers divisible by 15 become fizz 
    buzz. A player who hesitates or makes a mistake is eliminated from the game.
    """

    print("--------")
    print("FizzBuzz")
    print("--------")

    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizz buzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

    exit(0)

################################################################################