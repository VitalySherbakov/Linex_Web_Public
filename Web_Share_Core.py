import os, sys, time, datetime, json, socket, subprocess, requests
import urllib.request
from alive_progress import alive_bar
from alive_progress.styles import showtime
from requests import get
import urllib.request

class Web_Core(object):
    """Публикация Сайта"""
    def __init__(self):
        pass
    def InputWhile(self, text: str)->str:
        """Ввод Данных Цыкловый"""
        Flag,Res=True,""
        while Flag:
            Res=input(text)
            if not Res.strip():
                print("Пустое Значение!")
            else:
                Flag=False
        return Res
    def GetIP_Mashune(self)->None:
        """Тикущий IP Машыны"""
        IPAddr = subprocess.run(["ip", "route"], capture_output=True, text=True)
        if IPAddr.returncode == 0:
            stdout_lines = IPAddr.stdout.splitlines()
            for line in stdout_lines:
                print(f"Адресс: {line}")
        else:
            print("Ошибка выполнения команды")
    def GetIP(self)->list:
        """Получить IP Внешний"""
        ip_res=[False,"",""]
        try:
            ip = get('https://api.ipify.org').content.decode('utf8')
            ip_res[1]=ip
            ip_res[0]=True
        except Exception as ex:
            ip_res[2]=f"ERROR: {ex}!"
        return ip_res
    def GetIP2(self)->list:
        """Получить IP Внешний 2"""
        ip_res=[False,"",""]
        try:
            ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
            ip_res[1]=ip
            ip_res[0]=True
        except Exception as ex:
            ip_res[2]=f"ERROR: {ex}!"
        return ip_res
    def ReadFileInfo(self, pathfile: str)->list:
        """Получить Данные о Файле"""
        res_file=[False,"","",""]
        if os.path.exists(pathfile)==True:
            try:
                res_file[1],res_file[2]=os.path.splitext(pathfile)
            except Exception as ex:
                res_file[3]=f"ERROR: {ex}!"
        else:
            res_file[3]=f"Нету файла {pathfile}!"
        return res_file
    def ReadJson(self, pathfile: str, encod="utf-8")->list:
        """Чтение JSON"""
        res_file=[False,None,""]
        if os.path.exists(pathfile)==True:
            try:
                with open(pathfile) as json_file:
                    data=json.load(json_file)
                    res_file[1]=data
                    res_file[0]=True
            except Exception as ex:
                res_file[2]=f"ERROR: {ex}!"
        else:
            res_file[2]=f"Нету файла {pathfile}!"
        return res_file
    def WriteJson(self, pathfile: str, content: dict, encod="utf-8")->list:
        """Запись JSON"""
        result=[False,""]
        try:
            with open(pathfile, "w", encoding=encod) as json_file:
                # Записываем данные в файл в формате JSON
                json.dump(content, json_file)
            result[0]=True
        except Exception as ex:
            result[1]=f"Ошыбка Записи: {ex}!"
        return result
    def WriteFile(self, pathfile: str, content: list, encod="utf-8")->list:
        """Запись Файла"""
        res_file=[False,None,""]
        contentnew=""
        try:
            for li in content:
                contentnew+=li
            with open(pathfile, "w", encoding=encod) as fi:
                fi.write(contentnew)
            res_file[1] = contentnew
            res_file[0] = True
        except Exception as ex:
            res_file[2]=f"ERROR: {ex}!"
        return res_file
    def ReadFile(self, pathfile: str, method: int, encod="utf-8")->list:
        """Чтение Файла Полностью\n
            method -> 1 - читает полностью файл\n
            method -> 2 - читает построчно файл\n
            method -> 3 - читает построчно исключая пустые строки файл
        """
        res_file=[False,None,""]
        if os.path.exists(pathfile)==True:
            try:
                with open(pathfile, "r", encoding=encod) as fi:
                    if method==1:
                        res_file[1] = fi.read()
                        res_file[0] = True
                    if method==2:
                        res_file[1] = fi.readlines()
                        res_file[0] = True
                    if method==3:
                        liststr = fi.readlines()
                        filtered_list = list(filter(None, liststr))
                        res_file[1] = filtered_list
                        res_file[0] = True
            except Exception as ex:
                res_file[2]=f"ERROR: {ex}!"
        else:
            res_file[2]=f"Нету файла {pathfile}!"
        return res_file
    def DownloadFile2(self, url: str, filepath: str, style="classic"):
        """Загрузить Файл 2"""
        Flag=False
        try:
            urllib.request.urlretrieve(url, filepath)
            # command=f'wget -O "{filepath}" "{url}"'
            # os.system(command)
            # response = requests.get(url, stream=True)
            # total_size = int(response.headers.get("content-length", 0))
            # block_size = 1024  # задайте размер блока загрузки по вашему усмотрению
            # with open(filepath, "wb") as f, alive_bar(total_size, bar=style) as bar:
            #     for data in response.iter_content(block_size):
            #         f.write(data)
            #         bar(len(data))
            Flag=True
        except Exception as ex:
            print(f"ERROR DOWNLOAD: {ex}!")
        return Flag
    def DownloadFile(self, url: str, filepath: str, style="classic"):
        """Загрузить Файл"""
        Flag=False
        try:
            #urllib.request.urlretrieve(url, filepath)
            # command=f'wget -O "{filepath}" "{url}"'
            # os.system(command)
            response = requests.get(url, stream=True)
            total_size = int(response.headers.get("content-length", 0))
            block_size = 1024  # задайте размер блока загрузки по вашему усмотрению
            with open(filepath, "wb") as f, alive_bar(total_size, bar=style) as bar:
                for data in response.iter_content(block_size):
                    f.write(data)
                    bar(len(data))
            Flag=True
        except Exception as ex:
            print(f"ERROR DOWNLOAD: {ex}!")
        return Flag
    def Pause(self)->None:
        """Пауза"""
        input("-------------------Enter-------------------")
    def PauseProcess(self)->None:
        """Пауза 2"""
        input("-------------Начать-------------")
    def PauseWrite(self, text: str):
        """Пауза 3"""
        input(f"-------------{text}-------------")


class Web_Projects(object):
    """Веб Проекты"""
    __PathProject: str="Projects.json"
    """Файл Проекта"""
    __App: Web_Core=None
    """Функционал"""
    def __init__(self, pathproject: str):
        """Веб Проекты"""
        self.__PathProject=pathproject
        self.__App=Web_Core()
    def FindBool(self, name_project: str, encod="utf-8")->list:
        """Поиск Проекта"""
        result=[False,""]
        try:
            res, data, err = self.__App.ReadJson(self.__PathProject, encod)
            if res==True and data!=None:
                found_items = [item for item in data if item["Name"] == name_project]
                if found_items:
                    result[0]=True
            else:
                result[1]=f"Ошыбка {self.__PathProject}: {err}!"
        except Exception as ex:
            result[1]=f"Ошыбка: {ex}!"
        return result
    def Find(self, name_project: str, encod="utf-8")->list:
        """Поиск Проекта"""
        result=[False,None,""]
        try:
            res, data, err = self.__App.ReadJson(self.__PathProject, encod)
            if res==True and data!=None:
                found_items = [item for item in data if item["Name"] == name_project]
                if found_items:
                    result[1]=found_items
                    result[0]=True
            else:
                result[2]=f"Ошыбка {self.__PathProject}: {err}!"
        except Exception as ex:
            result[2]=f"Ошыбка: {ex}!"
        return result
    def Add(self, content: dict, encod="utf-8")->list:
        """Добавить"""
        result=[False,""]
        try:
            name=content["Name"]
            res, err=self.FindBool(name, encod); 
            if res==False:
                res2, listing2, err2= self.__App.ReadJson(self.__PathProject, encod)
                if res2==True:
                    listing2: list=listing2
                    listing2.append(content)
                    self.__App.WriteJson(self.__PathProject,listing2, encod)
                    result[0]=True
                else:
                    result[1]=err2
            else:
                result[1]=err
        except Exception as ex:
            result[1]=f"Ошыбка: {ex}!"
        return result
    def Del(self, content: dict, encod="utf-8")->list:
        """Удалить"""
        result=[False,""]
        try:
            name=content["Name"]
            res, err=self.FindBool(name, encod); 
            if res==True:
                res2, listing2, err2= self.__App.ReadJson(self.__PathProject, encod)
                if res2==True:
                    listing2: list=listing2
                    for li in listing2:
                        if li["Name"]==name:
                            listing2.remove(li)
                            result[0]=True
                            break #Прерывание не продолжать крутить цыкл
                    self.__App.WriteJson(self.__PathProject,listing2, encod)
                else:
                    result[1]=err2
            else:
                result[1]=err
        except Exception as ex:
            result[1]=f"Ошыбка: {ex}!"
        return result
    
    def DelName(self, name: str, encod="utf-8")->list:
        """Удалить по Имени"""
        result=[False,""]
        try:
            res, err=self.FindBool(name, encod); 
            if res==True:
                res2, listing2, err2= self.__App.ReadJson(self.__PathProject, encod)
                if res2==True:
                    listing2: list=listing2
                    for li in listing2:
                        if li["Name"]==name:
                            listing2.remove(li)
                            result[0]=True
                            break #Прерывание не продолжать крутить цыкл
                    self.__App.WriteJson(self.__PathProject,listing2, encod)
                else:
                    result[1]=err2
            else:
                result[1]=err
        except Exception as ex:
            result[1]=f"Ошыбка: {ex}!"
        return result

class Project_Nginx(object):
    """Проект Nginx"""
    NameProject: str=""
    """Имя Проекта"""
    Dir_Path: str=""
    """Папка Самой Программы"""
    Dir_Project: str=""
    """Папка с Проектами"""
    File_Project: str=""
    """Файл Запуска Проекта"""
    Core: str="core6"
    """Ядро Проекта"""
    Nginx_File: str=""
    """Файл для Nginx"""
    Service_File: str=""
    """Файл Сервиса"""
    IP: str = "127.0.0.1"
    """IP Машыны для Хоста"""
    Host: str=""
    """Хост Проекта"""
    HostRun: str=""
    """Хост Запущен Проект"""
    Port: int=80
    """Порт"""
    def __init__(self, nameproject: str, dir_path: str, dir_project: str, file_project: str, core: str, nginx_file: str, service_file: str, ip: str, host: str, hostrun: str, port: int):
        self.NameProject=nameproject
        self.Dir_Path=dir_path
        self.Dir_Project=dir_project
        self.File_Project=file_project
        self.Core=core
        self.Nginx_File=nginx_file
        self.Service_File=service_file
        self.IP=ip
        self.Host=host
        self.HostRun=hostrun
        self.Port=port

class Web_Nginx_Core(object):
    """Веб Настройка Использование Ядра Запуска Nginx"""
    __App: Web_Core=None
    """Функционал"""
    def __init__(self):
        """Веб Проекты"""
        self.__App=Web_Core()
    def CreateSettingProject(self, project: Project_Nginx):
        """Создание Настройки Сайта"""
        # Выбор Настройки
        if project.Core=="core6":
            # Прописываем Файл для Nginx
            # -------------Доступы----------------------
            os.system(f'chmod -R 777 "/etc/nginx/sites-available/"')
            os.system(f'chmod -R 777 "/etc/nginx/sites-enabled/"')
            os.system(f'chmod -R 777 "/etc/systemd/system/"')
            # ------------Адреса----------------------
            sites_available_file = f"/etc/nginx/sites-available/{project.Nginx_File}"
            sites_enabled_file= f"/etc/nginx/sites-enabled/{project.Nginx_File}"
            systemd_service_file = f"/etc/systemd/system/{project.Service_File}"
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
                os.system(f"sudo systemctl stop {project.Service_File}")
                os.remove(systemd_service_file)
            # Создать Файл Nginx
            content_nginx=[
                "server {\n",
                f"   listen {project.Port};\n",
                f"   server_name {project.Host};\n",
                "\n",
                "   location / {\n",
                f"      proxy_pass {project.HostRun};\n",
                "       proxy_http_version 1.1;\n",
                "       proxy_set_header Upgrade $http_upgrade;\n",
                "       proxy_set_header Connection keep-alive;\n",
                "       proxy_set_header Host $host;\n",
                "       proxy_cache_bypass $http_upgrade;\n",
                "       proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;\n",
                "       proxy_set_header X-Forwarded-Proto $scheme;\n",
                "   }\n",
                "}\n"
                ]                 
            res2,content2, err2=self.__App.WriteFile(sites_available_file,content_nginx)
            if res2==True:
                os.system(f'sudo ln -s {sites_available_file} /etc/nginx/sites-enabled/')
                print(f"Настройки {project.NameProject} Сайта Созданы!")
            # Создать Файл Сервиса
            content_service=[
                '[Unit]\n',
                f'Description=Проект {project.NameProject}\n',
                '[Service]\n',
                f'WorkingDirectory={project.Dir_Project}\n',
                f'ExecStart=/usr/bin/dotnet "{project.Dir_Project}/{project.File_Project}"\n',
                'Restart=always\n',
                f'# Перезапустите службу через 10 секунд, если служба выйдет из строя.:\n',
                'RestartSec=10\n',
                'KillSignal=SIGINT\n',
                f'SyslogIdentifier={project.NameProject}\n',
                'User=www-data\n',
                'Environment=ASPNETCORE_ENVIRONMENT=Production\n',
                'Environment=DOTNET_PRINT_TELEMETRY_MESSAGE=false\n',
                '\n',
                '[Install]\n',
                'WantedBy=multi-user.target\n'
                ]
            res3,content3, err3=self.__App.WriteFile(systemd_service_file,content_service)
            if res3==True:
                os.system(f"sudo systemctl enable {project.NameProject}.service")
                os.system(f"sudo systemctl start {project.NameProject}.service")
                os.system(f"sudo systemctl restart {project.NameProject}.service")
                # os.system(f"sudo systemctl status {project.NameProject}.service")
                print(f"Настройки Сервиса {project.NameProject} Сайта Созданы!")
            # До Настройки 
            self.NginxConf("server_names_hash_bucket_size 64","	server_names_hash_bucket_size 64;\n")
            print("Nginx: /etc/nginx/nginx.conf")
            print("Nginx Раскоментен-> server_names_hash_bucket_size 64")
            # self.LinexHost_Del(project.IP, project.Host) #Удаление для перезаписи
            self.LinexHost_Add(project.IP, project.Host)
            print("Хост: /etc/hosts")
            print(f"Добавлен: {project.IP}|{project.Host}")
            print(f"Проект {project.NameProject} Запущен!")
            
    def NginxConf(self,findstr : str, correctstr: str)->bool:
        """Коректировать Раскоментить\n
        findstr - Строка без пустот \n
        correctstr - Замена на строку другую с пустотами полностью 
        """
        Flag=False
        pathfile="/etc/nginx/nginx.conf"
        res, lines, err=self.__App.ReadFile(pathfile, 2)
        if res==True:
            linesset=[]
            for li in lines:
                li=str(li)
                lifind=str(li.strip())
                if lifind.find(findstr)!= -1:
                    linesset.append(correctstr)
                else:
                    linesset.append(li)
            res2, contents2, err2=self.__App.WriteFile(pathfile, linesset)
            Flag=res2
        return Flag

    def LinexHost_Add(self, ip: str, host: str)->bool:
        """Прописать Хост"""
        Flag=False
        pathfile="/etc/hosts"
        res, lines, err=self.__App.ReadFile(pathfile, 2)
        if res==True:
            linesset=[]
            lines_without_empty = [line for line in lines if line.strip()==f"{ip} {host}"]
            # Прибавление если нету
            if len(lines_without_empty)==0:
                lines=[f"{ip} {host}\n"]+lines
            # Перезапись
            for li in lines:
                li=str(li)
                linesset.append(li)
            res2, contents2, err2=self.__App.WriteFile(pathfile, linesset)
            Flag=res2
        return Flag

    def LinexHost_Del(self, ip: str, host: str)->bool:
        """Удалить Хост"""
        Flag=False
        pathfile="/etc/hosts"
        res, lines, err=self.__App.ReadFile(pathfile, 2)
        if res==True:
            linesset=[]
            for li in lines:
                li=str(li)
                lifind=str(li.strip())
                if lifind.find(f"{ip} {host}")!= -1:
                    pass
                else:
                    linesset.append(li)
            res2, contents2, err2=self.__App.WriteFile(pathfile, linesset)
            Flag=res2
        return Flag