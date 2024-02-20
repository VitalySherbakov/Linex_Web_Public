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
proj_setting = Web_Projects(file_project)
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
        if result=="4":
            nameproject = app.InputWhile("Имя Проекта: ")
            arhiveproject = app.InputWhile("Имя Файл Архива: ")
            hostproject = app.InputWhile("Хост Сайта или IP: ")
            portproject = app.InputWhile("Порт Трансляции: ")
            hostrunproject = app.InputWhile("Хост Запущеного Проекта или IP: ")
            path_download = f"{dir_path}/{dir_projects_downloads}/{arhiveproject}.7z"
            urlproject = app.InputWhile("Ccылка На Проект: ")
            result_down=app.DownloadFile(urlproject, path_download)
            if result_down==True:
                command = f'7z x "{path_download}" -o{dir_path}/{dir_projects}'
                os.system(command)
                project={
                    "Name": nameproject, 
                    "NginxFile": f"/etc/nginx/sites-available/{nameproject}", 
                    "Dir_Project": "serverdir", 
                    "Core": "core6", 
                    "ServiceFile": f"/etc/systemd/system/{nameproject}.service"
                }
                resadd, err=proj_setting.Add(project)
                if resadd==True:
                    print(f"Проект {nameproject} Загружен!")
                    project_nginx = Project_Nginx(
                        nameproject=nameproject,
                        dir_path=dir_path,
                        dir_projects=dir_projects,
                        core=project["Core"],
                        nginx_file=project["NginxFile"],
                        service_file=project["ServiceFile"],
                        host=hostproject,
                        hostrun=hostrunproject,
                        port=portproject
                    )
                    proj_nginx.CreateSettingProject(project_nginx)
                else:
                    print(f"Или Ошыбка Проекта {nameproject}, или он уже есть!")
                    print(f"Ошыбка Проекта: {err}")
            else:
                print("Ошыбка Загрузки!")
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