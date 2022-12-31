from autodebugger import *

try:
    import time    def Fibonacci():        n1, n2 = 1, "1"        for i in range(20):            nn = n1            n1 = n2            n2 = nn + n1    Fibonacci()    pass
except Exception as e:
    with open('Autodebugger/errors.txt', 'w') as ef:
        ef.write('{}'.format(sys.exc_info()[-1].tb_lineno) + ') ' + str(e))
