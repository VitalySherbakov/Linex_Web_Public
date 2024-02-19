versionscript=1.014
echo "Установка и Работа Linex Web Public SV (Щ.В) (v $versionscript)"
distributivelinex=$(uname -a)
numberversionlinex=$(uname -a)
dirhome="${PWD}"
dirsource="Linex_Web_Public"
scriptrun=$(basename -- "$0")

function function_python(){
    apt update -y
    sudo apt-get install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libnl-3-dev libnl-genl-3-dev pkg-config libsqlite3-dev libpcre3-dev libffi-dev curl libreadline-dev ethtool libbz2-dev libtool autoconf -y
	apt update -y
    wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz
	tar -xf Python-3.8.0.tgz
	rm -r Python-3.8.0.tgz
	chmod -R 777 "Python-3.8.0/"
	cd Python-3.8.0
	./configure --enable-optimizations
	make -j $(nproc)
	sudo make altinstall
	apt update -y
    wget -O get-pip.py https://bootstrap.pypa.io/get-pip.py
    sudo python3.8 get-pip.py
	pip install --upgrade pip
	python3.8 --version
	python3.8 -m pip install requests
	python3.8 -m pip install alive-progress
	python3.8 -m pip install tqdm
	python3.8 -m pip install py7zr
    python3.8 -m pip install pylzma
	python3.8 -m pip install rarfile
    python3.8 -m pip install urllib3==1.26.7
    cd ..
    rm -r Python-3.8.0
}

function function_core6(){
    # Core 6
    wget https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
    sudo dpkg -i packages-microsoft-prod.deb
    sudo apt-get update -y
    sudo apt-get install -y apt-transport-https
    sudo apt-get update -y
    sudo apt-get install -y dotnet-sdk-6.0
    sudo apt-get install -y aspnetcore-runtime-6.0
    rm -r packages-microsoft-prod.deb
}

function function_nginx(){
    # nginx
    sudo apt install nginx -y
    sudo ufw app list
    sudo ufw allow 'Nginx HTTP'
    sudo ufw allow 22
    sudo ufw allow 80
    sudo ufw allow 443
    sudo ufw enable
    sudo ufw status
}

function function_projects(){
    # projects
    mkdir projects
    sudo chmod -R 777 projects
}

function function_pack2(){
    # Установка Пакетов
    echo "Обновление..."
    apt update -y
    echo "Загрузка Пакетов 1..."
    apt install sudo -y
    apt install ssh -y
    apt install curl -y
    apt install wget -y
    apt install git -y
    apt install rar -y
    apt install zip -y
    apt install p7zip-full -y
	apt install unrar-free -y
    apt update -y
    echo "Загрузка Пакетов 2..."
    function_python
    function_core6
    function_nginx
    function_projects
    echo "-----Конец Установки Пакетов-----"
	echo "Авто Выход с Скрипта"
	echo "Повторно Войдите в Скрипт Командой"
	echo "bash ./$dirsource/$scriptrun"
	exit
}

function access_linex(){
	# Ubuntu полный доступ к папке
	nameuser=$USER
	chmod -R 777 "$dirsource/"
}
function auto_remove_program(){
    # Автоудаление Программы
    rm -rf "$dirsource"
}
# -----------------------------------------------------

function main(){
    # Основное Меню
    echo "Команда: pack (Установка необходимых пакетов)"
    echo "Команда: run (Запуск Скрипта)"
    echo "Команда: remove (Авто Удаление Программы)"
    echo "Команда: exit (Выход)"
    echo "Введите Команду:"
    read command
    if [ "$command" == "remove" ]; then
        echo "Вы Уверены в Удалении Программы Y/N"
        read command2
        if [ "$command2" == "y" ]; then
            access_linex
            auto_remove_program
            echo "Программа $dirsource Удалена!"
            exit
        fi
        if [ "$command2" == "Y" ]; then
            access_linex
            auto_remove_program
            echo "Программа $dirsource Удалена!"
            exit
        fi
	fi
    if [ "$command" == "pack" ]; then
        access_linex
		function_pack2
	fi
    if [ "$command" == "run" ]; then
        python3.8 "./$dirsource/LinexWeb.py" "$1"
	fi
    if [ "$command" == "exit" ]; then
		#break
        exit
	fi
}

while true
do
    current_time=$(date +%d.%m.%Y\ %T) # тикущая дата
    echo "-------------------------$current_time--------------------------"
    echo "Платформа: $distributivelinex"
    echo "Версия: $numberversionlinex"
    access_linex
    main "$distributivelinex"
    #if [ "$distributivelinex" == "Ubuntu" ]; then
        #access_linex
        #main "$distributivelinex"
    #fi
    read -p "Нажмите Enter, чтобы продолжить"
done