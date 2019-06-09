# Установка и настройка Anaconda

1. Установить Anaconda https://www.anaconda.com/distribution/#download-section

2. Проверить в cmd:
```bash
conda -v
```

3. Если нет, прописать в cmd : 
```bash
export PATH=~/anaconda3/bin:$PATH
```

	

4. Создать виртуальное окружение для программы:

```bash
conda create -n Название_окружения python=3.7 anaconda
```

5. Активаровать окружение: 

```bash
source activate Название_окружения
```

6. Установить Git: 

```bash
sudo apt-get install git
```

7. Клонировать программу: 
```bash
git clone https://github.com/zoohan955/OCLDiplome.git
```
# Установка и настройка OpenCL

1.Установить pyopencl(В окружении Anaconda):

	conda config --add channels conda-forge 
	conda install pyopencl[gpu] + nvidia driver/ conda install pocl [cpu]


2. Установить Opencl Drivers (intel):
 ```bash 
add-apt-repository ppa:intel-opencl/intel-opencl
apt-get update
apt-get install intel-opencl
```
3. Установить Opencl Drivers (nvidia):
    
	https://www.nvidia.ru/Download/index.aspx?lang=ru

# Запуск приложения из командной строки

```bash 
source activate Название_окружения
```

```bash 
cd /Путь к клонированному приложению
```

```bash 
python UI2.py
```


