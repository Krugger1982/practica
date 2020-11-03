import unittest
from unittest.mock import patch, Mock
import random



class Tests_For_files_and_Dirs(unittest.TestCase):

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

        
    def test_1_crawl_and_del(self):
        path = os.getcwd()                      # определяем текущий каталог (точнее его путь)
        Test_lists = crawl(path)
        control_files = ['files_and_dirs.py', 'files_and_dirs1.py', 'for lesson 4.docx', 'Patch.docx', '1.txt', '2.txt', '3.txt', '4.txt', '5.txt', '6.txt']
        control_dirs = ['dir_1', '__pycache__', 'dir_2.1', 'dir_2.2']
        Control_list = []
        Control_list.append(control_files)
        Control_list.append(control_dirs)
        for i in range(len(Control_list[0])):
            self.assertEqual(Control_list[0][i],Test_lists[0][i])
        for i in range(len(Control_list[1])):
            self.assertEqual(Control_list[1][i],Test_lists[1][i])



    @patch('files_and_dirs.os.remove')       # подменяем мeтод удаляющий файлы пустышкой
    @patch('files_and_dirs.os.rmdir')        # и подменяем метод, удаляющий каталоги пустышкой     
    def test_2_impossible_del(self, rmdir, remove):
        del_dir('dir_1')
        # так как есть вложенные каталоги, ничего не должно удалиться
        self.assertEqual(os.remove.call_count, 0)
        # проверка- метод os.remove не вызывался ни разу
        self.assertEqual(os.rmdir.call_count, 0)        
        # проверка- метод os.rmdir, не вызывался ни разу


    @patch('files_and_dirs.os.remove')       # подменяем мeтод удаляющий файлы пустышкой
    @patch('files_and_dirs.os.rmdir')        # и подменяем метод, удаляющий каталоги пустышкой   
    def test_3_possible_del_(self, rmdir, remove):
        path = os.getcwd() + '/dir_1'                       # заходим в каталог dir_1
        del_dir(path +'/dir_2.2')                           # вызываем удаоление вложенного каталога dir_2.2
        self.assertEqual(os.remove.call_count, 1)           # проверка- вызвано одно удаление файла
        self.assertEqual(os.rmdir.call_count, 1)            # проверка- вызвано одно удаление каталога

        
    def tearDown(self):                                                                     # В конце - уборка
        for root, dirs, files in os.walk(os.getcwd() + '/dir_1' +'/dir_2.2'):
            for file in files:
                os.remove(os.getcwd() + '/dir_1' +'/dir_2.2' + '/' + file)                  # удаляем файлы из каталога dir_2.2
        for root, dirs, files in os.walk(os.getcwd() + '/dir_1'):
            for file in files:          
                os.remove(os.getcwd() + '/dir_1' + '/' + file)                              # удаляем файлы из каталога dir_1
        os.rmdir(os.getcwd() + '/dir_1' + '/dir_2.1')                                       # удаляем пустой каталог dir_2.1
        os.rmdir(os.getcwd() + '/dir_1' + '/dir_2.2')                                       # удаляем пустой каталог dir_2.2
        os.rmdir(os.getcwd() + '/dir_1')                                                    # удаляем пустой каталог dir_1
        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
