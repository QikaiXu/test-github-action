import os

USER = os.getenv('USER')
print('-{}-'.format(USER[:8]))

a = input()
b = input()
print('a={}, b={}'.format(a, b))


