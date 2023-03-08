"""
Используйте модуль multiprocessing, чтобы создать три отдельных процесса.
Заставьте каждый из них подождать случайное количество секунд между
нулем и единицей, вывести текущее время, а затем завершить работу.
"""

import multiprocessing
import time
import os


def whoami(what) -> String:
    print("Process %s says: %s" % (os.getpid(), what))
    os.system('date –u')

if __name__ == "__main__":
    whoami("I'm the main program")
    for n in range(4):
        p = multiprocessing.Process(target=whoami,
                                    args=("I'm function %s" % n,))
        p.start()
