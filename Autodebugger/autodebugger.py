import traceback
import os, sys
import time
import pyautogui
from Autodebugger.setupbugger import *


def startup():
    """
    :return: Startup the program with all the setups
    """
    print("[Booting up] ... ", end="")

    # try importing, and see errors
    try:
        import traceback
        import os, sys
        import time
        import pyautogui
    except ImportError as ie:
        print(f"Importation failed; try installing pyautogui")

    # Important setups stuff for the user
    print("(✔)")
    print(f"[Autodebugger({model['version']})], {model['Status']} --> For more - {model['Developer']} (✔)\n")
    print("Terms and Conditions will apply; read it on the page or setupbugger.py (✔)")# please read this

    print(f"Welcome pythoneer! For info/help/bugs, visit {model['Documentation']}\nStarting "
          f"auto-debugger ...\n")
    time.sleep(0.5)


def debug(filename: str, timeout=15):
    """
    :param filename: The filename to be auto-debugged
    :param timeout: The time waited for the program to check the debugging (optimized for better usage)
    :return:
    """
    # called the startup() function
    startup()

    # the variable for running the program
    run = True

    # start time -> use for recording performance
    stime = time.time()

    # still in development
    debugged_mem = ""

    # main while loop for running the program
    while run:
        # Auto saves the debugging file so it debugs the latest updated file
        pyautogui.hotkey('ctrl', 's')

        # still in development -> but works
        if debugged_mem != Debug(filename).comment_error():
            debugged = Debug(filename)
            print(debugged.comment_error())

        # print out the debugged errors
        debugged_mem = debugged.comment_error()

        # wait until timeout is done
        time.sleep(timeout)

        ptime = time.time() # use for recording performance


class Debug:
    # The main object for the program
    """
    if error found in code, please report the bug for better version
    if you want to be part of the development, contact the developer
    """
    def __init__(self, filename):
        """
        :param filename: the filename of the program to be debugged
        """
        # open the file to be debugged and take in the code
        with open(filename, "r") as rf:
            raw_data = rf.readlines()
            for i in range(len(raw_data)):
                raw_data[i] = raw_data[i]

            code = "".join(raw_data[:]) # turn code into string

        # still in development
        self.error_called = 0

        # initializing the variables
        self.filename = filename
        self.code = code

        # running the program's main function
        self.sort()

    def remove_spec_items(self, ls, item):
        """
        :param ls: the list with elements
        :param item: the item to be removed
        :return: the list with all the specified item removed
        """
        item_count = ls.count(item) # count the item
        # remove the item
        for i in range(item_count):
            ls.remove(item)

    def sort(self):
        """
        :return: run a modified code version of the program in a file and run it to see the errors
        """
        codes = self.code.split('\n') # splice the code
        self.remove_spec_items(codes, "") # remove unnecessary '' from the code: list

        # put in all collected datas to be run
        with open("Autodebugger/debug_tester.py", "w") as f:
            f.write("from autodebugger import *\n")
            f.write("\ntry:\n")
            indent = 0
            for line_num, line in enumerate(codes):
                if "    " in line:
                    indent = line.count("    ")
                if "print" in line:
                    f.write(f"{'    ' * indent}    pass\n")
                else:
                    f.write(f"    {line}\r")
                indent = 0
            f.write(
                "except Exception as e:\n    with open('Autodebugger/errors.txt', 'w') as ef:\n        ef.write('{}'.format(sys.exc_info()[-1].tb_lineno) + ') ' + str(e))\n")

        # the file name
        debug_tester_file = "Autodebugger/debug_tester.py"
        # run the sugar code file
        os.system(f"python {debug_tester_file}")

    def reset_errors(self):
        """
        :return: reset the errors file for performace and memory
        """
        with open("Autodebugger/errors.txt", "w") as we:
            we.write("")

    def comment_error(self):
        """
        :return: using the errors, print out the debugged message
        """
        with open("Autodebugger/errors.txt", "r") as re:
            error_data = re.readlines()
            if not error_data:
                return 0
            else:
                error_ = error_data[0]
                error_num = error_.split(")")[0]
                error = "".join(error_.split(")")[1:])

                self.reset_errors()

        return f"Error Captured --> {error}>"


if __name__ == "__main__":
    while True:
        Debug("test.py")
