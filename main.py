from tkinter import *
from tkinter import filedialog
from read_settings import crudConfig, getSettings
from file_processing import *
from generator_core import coroutine, sleep, run
from SQL_Express import get_diskount_level_from_SQL
# import queue
# import time
import os.path
import glob

def query_file_btn_click():
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = filedialog.askdirectory()
    print(filename)
    query_file_txt.delete(0, END);
    query_file_txt.insert(0, filename);

def answer_file_btn_click():  
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = filedialog.askdirectory()
    print(filename)
    answer_file_txt.delete(0, END);
    answer_file_txt.insert(0, filename);

def save_settings():
    settings_path = "settings.ini"
    crudConfig(settings_path)

    settingsParams = getSettings('settings.ini')

    print(query_file_txt.get())

    settingsParams.set("Path", "query_file", query_file_txt.get())
    settingsParams.set("Path", "answer_file", answer_file_txt.get())

    with open(settings_path, "w") as config_file:
        settingsParams.write(config_file)

def get_settings():
    settings_path = "settings.ini"
    crudConfig(settings_path)

    settingsParams = getSettings('settings.ini')
    query_file_txt.insert(0, settingsParams.get("Path", "query_file"))
    answer_file_txt.insert(0, settingsParams.get("Path", "answer_file"))

def byOpenForm():
    get_settings()

@coroutine
def generator(name, timeout):

    # source_dir = "D:\Lazy\Pyton\Loyalty"
    # while glob.glob(os.path.join(source_dir, '*.*')):
    #     yield from sleep(timeout)
    while True:
        yield from sleep(timeout)
        print("Привет, {}!".format(name))

def run_generator():

    generator("me", 3)
    generator("you", 1)
    run()

def file_processing():

    dict_file_from_kass = get_dict_file_from_kass('D:/Users/LazyZMS/Pyton/GitHub/Loyalty/QUERY/Processing/ss000226.428') # Получаем словарь соответствий из файла с кассы
    print(dict_file_from_kass)

    card_number = dict_file_from_kass['CARDNO']
    # print(card_number)
    card_type = dict_file_from_kass['CARDTYPE']
    # print(card_type)

    discount_level = get_diskount_level_from_SQL(card_type, card_number) # Будем вытаскивать данные из соответствующей базы SQL
    print(discount_level)





window = Tk()
window.title("Добро пожаловать в приложение PythonRu")  
window.geometry('800x200')  
query_file_lbl = Label(window, text="Файлы запросов")
query_file_lbl.grid(column=0, row=0)  
query_file_txt = Entry(window,width=100)  
query_file_txt.grid(column=1, row=0)  
query_file_btn = Button(window, text="Клик!", command=query_file_btn_click)  
query_file_btn.grid(column=2, row=0)

answer_file_lbl = Label(window, text="Файлы ответов")
answer_file_lbl.grid(column=0, row=1)  
answer_file_txt = Entry(window,width=100)  
answer_file_txt.grid(column=1, row=1)  
answer_file_btn = Button(window, text="Клик!", command=answer_file_btn_click)  
answer_file_btn.grid(column=2, row=1)

save_settings_btn = Button(window, text="Save settings", command=save_settings)
save_settings_btn.grid(column=0, row=4)

run_btn = Button(window, text="Run Generator", command=run_generator)
run_btn.grid(column=1, row=4)

file_processing_btn = Button(window, text="Обработать файл", command=file_processing)
file_processing_btn.grid(column=0, row=5)


byOpenForm()
file_processing()

# window.mainloop()


