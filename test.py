from tkinter import *
from tkinter import filedialog
from Read_Settings import *


  
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

def byOpenForm():

    settings_path = "settings.ini"
    crudConfig(settings_path)

    settingsParams = getSettings('settings.ini')
    query_file_txt.insert(0, settingsParams.get("Path", "query_file"))
    answer_file_txt.insert(0, settingsParams.get("Path", "answer_file"))
  
  
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

byOpenForm()



window.mainloop()
