import os,sys,json, datetime
from Web_Share_Core import Web_Core, Web_Projects, Web_Nginx_Core, Project_Nginx
from typing import Literal

dir_path = os.path.dirname(os.path.realpath(__file__))

# Константы
dir_projects: Literal["projects"] = "projects"
dir_projects_downloads: Literal["projects_downloads"] = "projects_downloads"
file_project: Literal["Projects.json"]="Projects.json"
# Зависимости
app = Web_Core()
proj_setting = Web_Projects(f"{dir_path}/{file_project}")
proj_nginx = Web_Nginx_Core()

platform_name=sys.argv[1] #Получить Платформу для доступа
print(f"---------------------------------------------------")
print(f"Платформа: {platform_name}")
print(f"Папка: {dir_path}")

def Main():
    # Создание Папок для Проектов
    dir_projectnew=f"{dir_path}/{dir_projects}"
    dir_projects_downloadsnew=f"{dir_path}/{dir_projects_downloads}"
    if os.path.exists(dir_projectnew)==False:
        os.mkdir(dir_projectnew)
    if os.path.exists(dir_projects_downloadsnew)==False:
        os.mkdir(dir_projects_downloadsnew)
    # Меню
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
        print(f"3) Удалить Проекты")
        print(f"4) Установить IP Адресс (Ubuntu, Debian)")
        print(f"5) Скачать Проект и Опубликовать")
        print(f"6) Зарегестрировать Протокол HTTPS")
        print(f"7) Очистить Консоль")
        print(f"8) Выход из Скрипта")
        result = app.InputWhile("Номер Выбора: ")
        if result=="1":
            res, data, err=app.ReadJson(f"{dir_path}/{file_project}")
            if res==True:
                print("--------------Проекты--------------")
                for i,li in enumerate(data):
                    i=i+1
                    print(f'{i}) Проект: {li["Name"]}')
                    print(f'{i}) Папка: {li["Dir_Project"]}')
                    print(f'{i}) Запуск: {li["File_Project"]}')
                print("-----------------------------------")
            else:
                print(err)
        if result=="2":
            res, data, err=app.ReadJson(f"{dir_path}/{file_project}")
            if res==True:
                print("--------------Сервисы--------------")
                for i,li in enumerate(data):
                    i=i+1
                    print(f'{i}) Сервис: {li["ServiceFile"]}')
                print("-----------------------------------")
            else:
                print(err)
        if result=="3":
            res, data, err=app.ReadJson(f"{dir_path}/{file_project}")
            if res==True:
                print("--------------Проекты--------------")
                for i,li in enumerate(data):
                    i=i+1
                    print(f'{i}) Проект: {li["Name"]}')
                    print(f'{i}) Папка: {li["Dir_Project"]}')
                    print(f'{i}) Запуск: {li["File_Project"]}')
                print("-----------------------------------")
                nameproject = app.InputWhile("Имя Проекта: ")
                resdel = app.InputWhile("Вы Уверены Удалении Y/N: ")
                if resdel.lower()=="y":
                    # ------------Адреса----------------------
                    sites_available_file = f'/etc/nginx/sites-available/{li["NginxFile"]}'
                    sites_enabled_file= f'/etc/nginx/sites-enabled/{li["NginxFile"]}'
                    systemd_service_file = f'/etc/systemd/system/{li["ServiceFile"]}'
                    # -----------Удаление Перезаписи------------
                    if os.path.exists(sites_available_file)==True:
                        # Если есть удалить для Перезаписи
                        os.remove(sites_available_file)
                    # Удаляем Nginx Файл
                    if os.path.exists(sites_enabled_file)==True:
                        # Если есть удалить для Перезаписи
                        os.remove(sites_enabled_file)
                    # Создание Сервиса для Запуска Проекта
                    if os.path.exists(systemd_service_file)==True:
                        # Если есть удалить для Перезаписи
                        os.system(f'sudo systemctl stop {li["ServiceFile"]}')
                        os.remove(systemd_service_file)
                    # Чистка Хоста
                    proj_nginx.LinexHost_Del(li["IP"],li["HostWeb"])
                    # Удаление Проекта
                    dir_peoject_del = li["Dir_Project"]
                    if os.path.exists(dir_peoject_del):
                        #os.remove(dir_peoject_del)
                        os.system(f'rm -rf "{dir_peoject_del}"')
                        # Удаляем Записи в проектах
                        res2, err=proj_setting.DelName(li["Name"])
                        if res2==True:
                            print(f'Запись {li["Name"]} Удалена!')
                        print(f'Проект {li["Name"]} Удален!')
            else:
                print(err)
        if result=="4":
            interface = app.InputWhile("Интерфейс enp0s3: ")
            ipmashen = app.InputWhile("IP Машыны: ")
            iprouter = app.InputWhile("IP Роутер: ")
            contentip=[
                f"auto {interface}\n",
                "",
                f"iface {interface} inet static\n",
                f"  address {ipmashen}\n"
                f"  gateway {iprouter}\n"
                ]
            resultnewadd = app.InputWhile("Добавить дополнительные IP Y/N: ")
            if resultnewadd.lower()=="y":
                resultcounts = app.InputWhile("Количество Адресов: ")
                contsips=int(resultcounts)
                for li in range(0,contsips):
                    interfacenew = app.InputWhile(f"{li}) Интерфейс enp0s3: ")
                    ipmashennew = app.InputWhile(f"{li}) IP Машыны: ")
                    iprouternew = app.InputWhile(f"{li}) IP Роутер: ")
                    contentipnew=[
                        f"iface {interfacenew} inet static\n"
                        f"  address {ipmashennew}\n"
                        f"  gateway {iprouternew}\n"
                        ]
                    contentip+=contentipnew
            app.WriteFile("/etc/network/interfaces",contentip)
            os.system("systemctl restart NetworkManager")
            os.system("systemctl restart networking.service")
            print("Сеть Перезагружена!")
        if result=="5":
            nameproject = app.InputWhile("Имя Проекта: ")
            arhiveproject = app.InputWhile("Имя Файл Архива: ")
            filerunproject = app.InputWhile("Запускаймый Файл: ")
            ipproject = app.InputWhile("IP Машины: ")
            hostproject = app.InputWhile("Хост Сайта: ")
            portproject = app.InputWhile("Порт Трансляции: ")
            hostrunproject = app.InputWhile("Хост или IP Проекта: ")
            urlproject = app.InputWhile("Ccылка На Проект: ")
            # Путь куда Загружать Проект и куда распаковывать
            path_download = f"{dir_path}/{dir_projects_downloads}/{arhiveproject}.7z"
            path_project = f"{dir_path}/{dir_projects}/{nameproject}"
            # Удаление придыдущего проекта
            if os.path.exists(path_project)==True:
                os.remove(path_project)
            # Загрузка
            result_down=app.DownloadFile(urlproject, path_download)
            if result_down==True:
                # Распаковка
                command = f'7z x "{path_download}" -o{path_project}'
                os.system(command)
                # Даем Полный Доступ папке с проектами
                os.system(f'chmod -R 777 "{dir_path}/{dir_projects}/"')
                # Удаляем Скаченый Архив
                if os.path.exists(path_download):
                    os.remove(path_download)
                project={
                    "Name": nameproject, 
                    "NginxFile": f"{nameproject}", 
                    "Dir_Project": path_project,
                    "File_Project": filerunproject,
                    "HostWeb": hostproject,
                    "HostRun": hostrunproject,
                    "IP" : ipproject,
                    "Port": portproject,
                    "Core": "core6", 
                    "ServiceFile": f"{nameproject}.service"
                }
                resadd, err=proj_setting.Add(project)
                if resadd==True:
                    print(f"Проект {nameproject} Загружен!")
                    project_nginx = Project_Nginx(
                        nameproject=project["Name"],
                        dir_path=dir_path,
                        dir_project=project["Dir_Project"],
                        file_project=project["File_Project"],
                        core=project["Core"],
                        nginx_file=project["NginxFile"],
                        service_file=project["ServiceFile"],
                        ip=project["IP"],
                        host=project["HostWeb"],
                        hostrun=project["HostRun"],
                        port=project["Port"]
                    )
                    proj_nginx.CreateSettingProject(project_nginx)
                else:
                    print(f"Или Ошыбка Проекта {nameproject}, или он уже есть!")
                    print(f"Ошыбка Проекта: {err}")
            else:
                print("Ошыбка Загрузки!")
        if result=="6":
            print("Регестрация HTTPS Сертификата")
            res, data, err=app.ReadJson(f"{dir_path}/{file_project}")
            if res==True:
                print("--------------Проекты--------------")
                for i,li in enumerate(data):
                    i=i+1
                    print(f'{i}) Проект: {li["Name"]}|{li["HostWeb"]}')
                print("-----------------------------------")
            else:
                print(err)
            hostweb = app.InputWhile("Хост Сайта: ")
            os.system(f"sudo systemctl stop nginx")
            os.system(f"sudo certbot --nginx -d {hostweb}")
            os.system("sudo systemctl start nginx")
            os.system("sudo systemctl restart nginx")
        if result=="7":
            os.system("clear")
        if result=="8":
            break
        elif result!="1" and result!="2" and result!="3" and result!="4" and result!="5" and result!="6" and result!="7" and result!="8":
            print(f"Не Верная {result} Команда!")
        app.Pause()

if __name__ == "__main__":
    Main()