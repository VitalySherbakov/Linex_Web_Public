import os,sys,json, datetime
from Web_Share_Core import Web_Core

dir_path = os.path.dirname(os.path.realpath(__file__))

app = Web_Core()

platform_name=sys.argv[1] #Получить Платформу для доступа
print(f"---------------------------------------------------")
print(f"Платформа: {platform_name}")
print(f"Папка: {dir_path}")

def Main():
    while True:
        res_router,ip_router,err_router = app.GetIP() 
        current_date = datetime.datetime.now()
        current_date_str = current_date.strftime("%d.%m.%Y %H:%M:%S")
        print(f"-------------------------{current_date_str}--------------------------")
        if res_router==True:
            print(f"IP Роутера: {ip_router}")
        else:
            print(err_router)
        ip_local = app.GetIP_Mashune()
        print(f"IP Linex: {ip_local}")   
        print(f"1) Список Проектов")
        print(f"2) Список Сервисов")
        print(f"3) Скачать Проект")
        print(f"4) Запуск Проекта Опубликовать")
        print(f"5) Очистить Консоль")
        print(f"6) Выход из Скрипта")
        result = app.InputWhile("Номер Выбора: ")
        if result=="1":
            pass
        if result=="2":
            pass
        if result=="3":
            pass
        if result=="4":
            pass 
        if result=="5":
            os.system("clear")
        if result=="6":
            break
        elif result!="1" and result!="2" and result!="3" and result!="4" and result!="5" and result!="6":
            print(f"Не Верная {result} Команда!")
        app.Pause()

if __name__ == "__main__":
    Main()