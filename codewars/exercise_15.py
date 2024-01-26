class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives

    def guess(self, n):
        if self.lives <= 0:
            raise ValueError('No more lives. Game over!')

        if n == self.number:
            return True
        else:
            self.lives -= 1
            return False


if __name__ == '__main__':
    guesser = Guesser(10, 2)
    print(guesser.lives)
