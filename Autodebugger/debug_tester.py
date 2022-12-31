from autodebugger import *

try:
    import time
except Exception as e:
    with open('Autodebugger/errors.txt', 'w') as ef:
        ef.write('{}'.format(sys.exc_info()[-1].tb_lineno) + ') ' + str(e))