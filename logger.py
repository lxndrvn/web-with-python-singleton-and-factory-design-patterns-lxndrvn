import datetime
import time


class Logger(object):
    class __Logger:
        def __init__(self):
            self.log_file = "logfile_" + datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + ".txt"

        def log(self, msg):
            with open(self.log_file, "a+") as log_file:
                log_file.write(msg + '\n')

    instance = None

    def __init__(self):
        if not Logger.instance:
            Logger.instance = Logger.__Logger()
        self.log_file = Logger.instance.log_file

    @staticmethod
    def log(msg):
        Logger.instance.log(msg)


def main():
    print('Creating logger...')
    logger = Logger()

    print('Name of first logfile:')
    print(logger.log_file)

    message = input("Let's log something: ")
    logger.log(message)

    print('Sleeping...')
    time.sleep(5)

    print('Creating logger again!')
    logger = Logger()

    print('Name of logfile:')
    print(logger.log_file)
    print('...still the same.')

    message = input("Let's log something: ")
    logger.log(message)

    print('Contents of logfile:')
    with open(logger.log_file, 'r') as logfile:
        print(logfile.read())

if __name__ == '__main__':
    main()

