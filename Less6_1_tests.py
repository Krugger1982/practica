from zipfile import ZipFile
import os.path
import unittest
import random



class Tests_archives(unittest.TestCase):

    def setUp(self):
        path = os.getcwd()                      # определяем текущий каталог (точнее его путь)
        if not os.path.isdir('dir_1'):
            os.makedirs(path + '/dir_1')        # созлаем первый каталог
        path1 = path + '/dir_1'                        # переходим в только что созданный каталог
        for i in range(5):
            x = path1 + '/' + str(i+1) + '.txt'
            with open(x, 'wt', encoding='utf-8') as newfile:
                newfile.write(str(random.randint(1, 100000))+'\n')    # Создаем внутри каталога текстовые файлы и записываем в них рандомные числа
        if not os.path.isdir('dir_2.1'):
            os.makedirs(path1 + '/dir_2.1')       # создаем вложенный каталог
        if not os.path.isdir('dir_2.2'):
            os.makedirs(path1 + '/dir_2.2')       # создаем вложенный каталог
        path2 = path1 +'/dir_2.2'                       # переходим в  каталог dir_2.2
        with open(path2 + '/6.txt', 'wt', encoding='utf-8') as newfile:
            newfile.write(str(random.randint(1, 100000))+'\n')            # и создадим в каталоге dir_2.2  еще один файл    
        #Получится такое дерево
        # dir_1
        #   - 1.txt           
        #   - 2.txt
        #   - 3.txt
        #   - 4.txt
        #   - 5.txt
        #   dir_2.1
        #   dir_2.2
        #       - 6.txt
        
    def test_1(self):
                    
        result_names = ['dir_1/1.txt', 'dir_1/2.txt', 'dir_1/3.txt', 'dir_1/4.txt', 'dir_1/5.txt', 'dir_1/dir_2.2/6.txt']
        selection1('Example.zip', 'txt')
        with ZipFile('Example.zip') as archive:                          # Откроем полученный архив
            test_result_names = archive.namelist()
            self.assertCountEqual(test_result_names, result_names)      # Проверка - в списках одни и те же имена (возможо,в другом порядке)
        



    def tearDown(self):                                                                     # В конце - уборка
        for root, dirs, files in os.walk(os.getcwd() + '/dir_1' +'/dir_2.2'):
            for file in files:
                os.remove(os.getcwd() + '/dir_1' +'/dir_2.2' + '/' + file)                  # удаляем файлы из каталога dir_2.2
        for root, dirs, files in os.walk(os.getcwd() + '/dir_1'):
            for file in files:          
                os.remove(os.getcwd() + '/dir_1' + '/' + file)                              # удаляем файлы из каталога dir_1
        os.rmdir(os.getcwd() + '/dir_1' + '/dir_2.1')                                       # удаляем пустой каталог dir_2.1
        os.rmdir(os.getcwd() + '/dir_1' + '/dir_2.2')                                       # удаляем пустой каталог dir_2.2
        os.rmdir(os.getcwd() + '/dir_1')            
        os.remove('Example.zip')
                    
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
