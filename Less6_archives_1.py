from zipfile import ZipFile, ZipInfo
import os.path


def crawl (dir_adress='.'):
    Dirs = []
    Files = []
    result = []
    for root, dirs, files in os.walk(dir_adress):
        Dirs += [root]
        for filename in files:
            Files += [root + '\\' + filename]
    result.append(Files)
    result.append(Dirs)

    return result


def selection1(Name, extension):
    """ Function for searching Zipfile  for files with specified extension
        and write them to a new archive """
    with ZipFile(Name, 'a') as result:              # создаем архив для записи результатов, присваиваем ему имя
        files = crawl('.')[0]
        for filename in files:
            if filename.find('.' + extension) != -1:        # И если в нем есть файл с требуемым расширением
                result.write(filename)        # Заносим его в  архив по его относительному пути
