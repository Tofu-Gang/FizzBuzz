from sys import exit

################################################################################

class FizzBuzz(object):

    def __init__(self, i: int):
        """

        """

        self._i = i

################################################################################

    def __str__(self):
        """

        :return:
        """

        if self._i % 3 == 0 and self._i % 5 == 0:
            return "fizz buzz"
        elif self._i % 3 == 0:
            return "fizz"
        elif self._i % 5 == 0:
            return "buzz"
        else:
            return str(self._i)

################################################################################

def ya_basic() -> str:
    """
    :return: The most basic fizz buzz I can think of. The string is made with
    the same format as iterator output.
    """

    fizzbuzz = "["

    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            fizzbuzz += "'fizz buzz'"
        elif i % 3 == 0:
            fizzbuzz += "'fizz'"
        elif i % 5 == 0:
            fizzbuzz += "'buzz'"
        else:
            fizzbuzz += "'" + str(i) + "'"
        fizzbuzz += ", "
    fizzbuzz = fizzbuzz[:-2]
    fizzbuzz += "]"

    return fizzbuzz

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

    print(ya_basic())
    # I think I can do an iterator:
    print([str(FizzBuzz(i)) for i in range(1, 101)])

    exit(0)

################################################################################