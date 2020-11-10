from zipfile import ZipFile
import os.path

def selection1(Name, extension):
    """ Function for searching Zipfile  for files with specified extension
        and write them to a new archive """
    with ZipFile(Name, 'a') as result:              # создаем архив для записи результатов, присваиваем ему имя
        for root, dirs, files in os.walk('.'):      # обходим текущий каталог
            for filename in files:
                if filename.find('.' + extension) != -1:        # И если в нем есть файл с требуемым расширением
                    result.write(filename)    
