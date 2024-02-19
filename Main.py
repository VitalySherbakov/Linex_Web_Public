import subprocess

result="CompletedProcess(args=['ip', 'route'], returncode=0, stdout='default via 192.168.134.1 dev enp0s3 proto dhcp metric 100 \n192.168.134.0/24 dev enp0s3 proto kernel scope link src 192.168.134.101 metric 100 \n', stderr='')"
if result.returncode == 0:
    stdout_lines = result.stdout.splitlines()
    for line in stdout_lines:
        print(line)
else:
    print("Ошибка выполнения команды")