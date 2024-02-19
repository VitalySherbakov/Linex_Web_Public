import os, sys, time, datetime, json, socket, subprocess
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
    def GetIP_Mashune(self):
        """Тикущий IP Машыны"""
        IPAddr = subprocess.run(["ip", "route"], capture_output=True, text=True)
        if IPAddr.returncode == 0:
            stdout_lines = IPAddr.stdout.splitlines()
            for line in stdout_lines:
                print(line)
        else:
            print("Ошибка выполнения команды")
        return IPAddr
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
    def Pause(self)->None:
        """Пауза"""
        input("-------------------Enter-------------------")
    def PauseProcess(self)->None:
        """Пауза 2"""
        input("-------------Начать-------------")
    