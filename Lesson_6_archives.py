from zipfile import ZipFile
import os.path

def selection(Name, extension):
    with ZipFile('result.zip', 'a') as result:
        with ZipFile(Name) as archive:                                  # Открываем исходный архив
            list_ = archive.namelist()                                  # Срздадим оглавление исходного архива
            for file in list_:                                          
                if file.find('.' + extension) != -1 and '/' in file:    # пробежав по оглавлению найдем сперва  файлы c нужным расширением во вложенных каталогах
                    NewName = file.split('/')
                    archive.extract(file)                               # Для переноса в другой каталог их придется эксрактировать (извлечь) в текущий каталог
                    result.write(file, arcname=NewName[-1])             # Занесем их в результирующий архив (будет создан заново) с "отрезанным" путем
                    os.remove(file)                                     # и подчистим их в текущем каталоге
                elif file.find('.' + extension) != -1:                  # Затем поищем нужные файлы в корне исходного каталога
                    archive.extract(file)
                    result.write(file)
                    os.remove(file)                                     # И так же в конце подотрем в текущем каталоге
                    
            for file in reversed(list_):                                # Пробежимся по созданным в ходе извлечения каталогам и удалим их
                if '/' in file:
                    NewName = file.split('/')
                    for dirs in range(-2, -len(NewName)-1, -1):         # ... со всеми вложенными каталогами (снизу вверх)
                        if os.path.isdir(NewName[dirs]):
                            os.rmdir(NewName[dirs])
    return result.filename
