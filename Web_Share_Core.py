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
        """Чтение Файла Полностью
            method -> 1 - читает полностью файл
            method -> 2 - читает построчно файл
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