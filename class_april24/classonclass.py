class Daredevil:
    def __init__(self):
        self.name = 'daredevil'
        self.pointy_hat = True
        self.baton = True

    def attack(self):
        print('i\'m coming')

    def defend(self):
        print('stand back')

    def use_senses(self):
        print('ping ping ping')


class CaptainAmerica:
    def __init__(self):
        self.name = 'cap'
        self.pointy_hat = True
        self.shield = True

    def attack(self):
        print('i\'m coming')

    def defend(self):
        print('stand back')

    def lift_heavy_stuff(self):
        print('uuurrggg')


dd = Daredevil()
#
# print(dd.pointy_hat)
# dd.defend()
# dd.use_senses()

cap = CaptainAmerica()


# print(cap.pointy_hat)
# cap.attack()
# cap.lift_heavy_stuff()
# cap.use_senses()

def detect_villan_using_radar(hero):
    try:
        hero.use_senses()
    except AttributeError:
        print('%s, doesn\'t have this power' % hero.name)


detect_villan_using_radar(dd)

detect_villan_using_radar(cap)


# exceptions
try:
    x = 4/0
except:
    print('exception happened')


try:
    x = 4/0
except ZeroDivisionError:
    print('wat? divide by zero')
except Exception:
    print('some other exception happened')


try:
    x.do_something()
except ZeroDivisionError:
    print('wat? divide by zero')
except Exception:
    print('some other exception happened')


try:
    x.do_something()
except Exception as e:
    print('some exception happened')
    print(str(e))
