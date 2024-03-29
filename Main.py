import subprocess, os, sys
from Web_Share_Core import Web_Core, Web_Projects, Web_Nginx_Core
from typing import Literal

dir_path = os.path.dirname(os.path.realpath(__file__))

# Константы
dir_projects: Literal["projects"] = "projects"
dir_projects_downloads: Literal["projects_downloads"] = "projects_downloads"
file_project: Literal["Projects.json"]="Projects.json"

app=Web_Core()
setting=Web_Projects(file_project)
proj_nginx = Web_Nginx_Core()

# interface = app.InputWhile("Интерфейс enp0s3: ")
# ipmashen = app.InputWhile("IP Машыны: ")
# iprouter = app.InputWhile("IP Роутер: ")
# contentip=[
#     f"auto {interface}\n",
#     "",
#     f"iface {interface} inet static\n",
#     f"  address {ipmashen}\n"
#     f"  gateway {iprouter}\n"
#     ]
# resultnewadd = app.InputWhile("Добавить дополнительные IP Y/N: ")
# if resultnewadd.lower()=="y":
#     resultcounts = app.InputWhile("Количество Адресов: ")
#     contsips=int(resultcounts)
#     for li in range(0,contsips):
#         interfacenew = app.InputWhile(f"{li}) Интерфейс enp0s3: ")
#         ipmashennew = app.InputWhile(f"{li}) IP Машыны: ")
#         iprouternew = app.InputWhile(f"{li}) IP Роутер: ")
#         contentipnew=[
#             f"iface {interfacenew} inet static\n"
#             f"  address {ipmashennew}\n"
#             f"  gateway {iprouternew}\n"
#             ]
#         contentip+=contentipnew
# print(contentip)
# app.WriteFile("interfaces",contentip)


# nameproject = app.InputWhile("Имя Проекта: ")
# arhiveproject = app.InputWhile("Имя Файла Архива: ")
# path_download = f"{dir_path}\\{dir_projects_downloads}\\{arhiveproject}.7z"
# print(f"D: {path_download}")
# urlproject = app.InputWhile("Ccылка На Проект: ")
# result_down=app.DownloadFile(urlproject, path_download)
# if result_down==True:
#     command = f'7z x "{path_download}" -o{dir_path}\\{dir_projects}'
#     print(command)
#     #os.system(command)
#     print(f"Проект {nameproject} Загружен!")
# else:
#     print("Ошыбка Загрузки!")

# res, content , err=setting.Find("server2")
# res: bool=res
# tes=True
# if res==True:
#     print(f"R: {res}")
# else:
#     print(f"Err: {err}")

# dic={
#         "Name": "server2",
#         "NginxFile": "1",
#         "Dir_Project": "serverdir1",
#         "Core": "core6",
#         "ServiceFile": "server1.service"
#     }


# res, err=setting.Add(dic)
# if res==True:
#     print("Добавлен")
# else:
#     print("Уже есть!")

# res, err=setting.DelName("server2")
# if res==True:
#     print("Удален")
# else:
#     print(err)
#     print("Нету!")
# ip,host="192.168.134.200","vidoconferencia.hopto.org"
# #res=proj_nginx.LinexHost_Add(ip,host)
# res=proj_nginx.LinexHost_Del(ip,host)

# res = proj_nginx.LinexTor_Conf("HiddenServiceDir /var/lib/tor/hidden_service/","HiddenServiceDir /var/lib/tor/hidden_service/\n")
# res = proj_nginx.LinexTor_Conf("HiddenServicePort 80 127.0.0.1:80","HiddenServicePort 80 127.0.0.1:80\n")
# s=["localhost:5000","videoconferencial.hopto.org","127.0.0.1:80"]
# res=app.SetSplitText(s," ")
# print(f"|{res}|")

s=["1","2","3","4","5"]
d=["2","4", "6"]
for li in s:
    if li in d:
        print(li)