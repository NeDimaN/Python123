import os.path
import os


path = r'Test1.txt'
search_file = os.path.isfile(path)
if search_file is True:
    print(f'{path}({os.getcwd()})- последнее время доступа {os.path.getatime(path)} секунд')
else:
    print("Файл не существует")