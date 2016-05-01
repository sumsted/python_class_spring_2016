class Antman:
    def __init__(self, name):
        self.name = name
        self.is_small = True

    def go_small(self,level):
        print(self.name, 'going small')

        for i in range(1, level):
            print('in', i)


scott = Antman('Scott')

scott.go_small(5)

