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
        print(f"-------------------------Адреса--------------------------")
        app.GetIP_Mashune()
        print(f"---------------------------------------------------")
        print(f"1) Список Проектов")
        print(f"2) Список Сервисов")
        print(f"3) Установить IP Адресс (Ubuntu, Debian)")
        print(f"4) Скачать Проект")
        print(f"5) Запуск Проекта Опубликовать")
        print(f"6) Очистить Консоль")
        print(f"7) Выход из Скрипта")
        result = app.InputWhile("Номер Выбора: ")
        if result=="1":
            pass
        if result=="2":
            pass
        if result=="3":
            interface = app.InputWhile("Интерфейс enp0s3: ")
            ipmashen = app.InputWhile("IP Машыны: ")
            iprouter = app.InputWhile("IP Роутер: ")
            contentip=f"""
            auto {interface}
            
            iface {interface} inet static
                address {ipmashen}
                gateway {iprouter}
                """
            resultnewadd = app.InputWhile("Добавить дополнительные IP Y/N: ")
            if resultnewadd.lower()=="y":
                resultcounts = app.InputWhile("Количество Адресов: ")
                contsips=int(resultcounts)
                for li in range(0,contsips):
                    interfacenew = app.InputWhile(f"{li}) Интерфейс enp0s3: ")
                    ipmashennew = app.InputWhile(f"{li}) IP Машыны: ")
                    iprouternew = app.InputWhile(f"{li}) IP Роутер: ")
                    contentipnew=f"""
                    iface {interfacenew} inet static
                        address {ipmashennew}
                        gateway {iprouternew}
                        """
                    contentip+=contentipnew
            app.WriteFile("/etc/network/interfaces",contentip)
            os.system("systemctl restart NetworkManager")
            os.system("systemctl restart networking.service")
            print("Сеть Перезагружена!")
        if result=="4":
            pass 
        if result=="5":
            pass 
        if result=="6":
            os.system("clear")
        if result=="7":
            break
        elif result!="1" and result!="2" and result!="3" and result!="4" and result!="5" and result!="6" and result!="7":
            print(f"Не Верная {result} Команда!")
        app.Pause()

if __name__ == "__main__":
    Main()