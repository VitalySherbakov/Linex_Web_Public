import subprocess
from Web_Share_Core import Web_Core

app=Web_Core()

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
print(contentip)
app.WriteFile("interfaces",contentip)