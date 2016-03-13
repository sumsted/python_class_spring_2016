from guess import guess

MIN = 0
MAX = 999
MESSAGE = 'Great Choice!'


def linear_search():
    for i in range(MAX):
        response = guess(i, MESSAGE)
        if response == 'correct':
            print('code is: ', i)
            break


if __name__ == '__main__':
    linear_search()
