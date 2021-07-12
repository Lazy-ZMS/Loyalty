# sample.py
from concurrency import coroutine, sleep, run
import shutil # Подключаем модуль
import glob
import os.path

@coroutine
def hello(name, timeout):
    while True:
        yield from sleep(timeout)
        print("Привет, {}!".format(name))

def copy_File_from_kass(timeout):
    while True:
        yield from sleep(timeout)
        source_dir = "D:\Lazy\Pyton\Loyalty"
        dest_dir = "D:\Lazy\Pyton\Loyalty\TEST"
        for filename in glob.glob(os.path.join(source_dir, '*.*')):
            shutil.copy(filename, dest_dir)
            

hello("Петров", 1)
##hello("Иванов", 3.0)
##hello("Мир", 5.0)
##copy_File_from_kass(0.5)
run()
