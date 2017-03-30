from logger import Logger


class Toy(object):
    def __init__(self):
        self.logger = Logger()

    def prepare(self):
        pass

    def make(self):
        pass

    def package(self):
        pass


class Boat(Toy):
    def prepare(self):
        self.logger.log("Preparing boat..")

    def make(self):
        self.logger.log("Making boat..")

    def package(self):
        self.logger.log("Packaging boat..")


class Racecar(Toy):
    def prepare(self):
        self.logger.log("Preparing racecar..")

    def make(self):
        self.logger.log("Making racecar..")

    def package(self):
        self.logger.log("Packaging racecar..")


class Spaceship(Toy):
    def prepare(self):
        self.logger.log("Preparing spaceship..")

    def make(self):
        self.logger.log("Making spaceship..")

    def package(self):
        self.logger.log("Packaging spaceship..")


class ToyFactory(object):
    @staticmethod
    def make_toy(toy_name):
        if toy_name == 'boat':
            return Boat()

        if toy_name == 'racecar':
            return Racecar()

        if toy_name == 'spaceship':
            return Spaceship()

        else:
            raise NameError("No such toy!")


def main():
    logger = Logger()
    print('Logging in ' + logger.log_file)
    toy_name = input("Choose a toy! Boat, Racecar or Spaceship: ")
    toy = ToyFactory().make_toy(toy_name.lower())
    toy.prepare()
    toy.make()
    toy.package()
    logger.log("Goodbye!")


if __name__ == '__main__':
    main()
