from zipfile import ZipFile
import os.path
import archive                 # Это тестируемая функция
import unittest
import random



class Tests_archives(unittest.TestCase):
        
    def test_1(self):
        test_names = []
        result_names = []
        for i in range(10):
            x = 'TestFile_' + str(i+1) + '.txt'
            with open(x, 'wt', encoding='utf-8') as a:                  # Создадим в текущем каталоге 10 текстовых файлов с рандомным содержимым и с расширением 'txt'
                for j in range(3):
                    a.write(str(random.randint(1, 100000))+'\n')
            test_names.append(x)                                        # И запишем их имена
            result_names.append(x)                                      # Эти имена должны быть и в итоговом архиве
        for i in range(5):
            x = 'TestFile_' + str(i+1) + '.odt'                         # Добавим еще 5 файлов с другим расширением
            with open(x, 'wt', encoding='utf-8') as a:
                for j in range(3):
                    a.write(str(random.randint(1, 100000))+'\n')        
            test_names.append(x)                                        # И также запишем их имена
            
        for root, dirs, files in os.walk('.'):                          # обойдем весь текущий каталог
            with ZipFile('Example.zip', 'a') as test_archive:
                for file_name in files:
                    if file_name != 'archive.cpython-39.pyc':
                        test_archive.write(file_name)                           # Забросим все что есть в текущем каталоге в архив
                    if file_name in test_names:                                 
                        os.remove(file_name)                                # и подчистим тестовые файлы (по именам)
                                                                        # в архиве будут лежать тестовые файлы и еще что-то (рабочие файлы)
        result = archive.selection('Example.zip', 'txt')
        with ZipFile(result) as test_result:                            # Откроем полученный архив
            test_result_names = test_result.namelist()
            self.assertCountEqual(test_result_names, result_names)      # Проверка - в списках одни и те же имена (возможо,в другом порядке)
            
        os.remove('Example.zip')                                        # В конце удалим тестовый архив
        os.remove(result)                                               # и  конечный архив
            
            
        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
