import time

# this file is just a test file, if you are going to debug using your own file, go to debug_log.py and change the
# filename


def Fibonacci():
    n1, n2 = 1, "1"
    for i in range(20):

        nn = n1
        n1 = n2
        n2 = nn + n1


Fibonacci()

