import unittest
import random

class TestCase(unittest.TestCase):
    def test_1_crawl_and_del(self):
        path = os.getcwd()                      # определяем текущий каталог (точнее его путь)
        if not os.path.isdir('dir_1'):
            os.makedirs(path + '/dir_1')        # созлаем первый каталог
        path1 = path + '/dir_1'                        # переходим в только что созданный каталог
        for i in range(5):
            x = path1 + '/' + str(i+1) + '.txt'
            with open(x, 'wt', encoding='utf-8') as newfile:
                newfile.write(str(random.randint(1, 100000))+'\n')    # Создаем внутри каталога текстовые файлы и записываем в них рандомные числа


        #Получится такое дерево
        # dir_1 1.txt           
        #       2.txt
        #       3.txt
        #       4.txt
        #       5.txt
        #
        control_files = [ '1.py', '1.txt', '2.txt', '3.txt', '4.txt', '5.txt']
        control_dirs = ['dir_1']
        Control_list = []
        Control_list.append(control_files)
        Control_list.append(control_dirs)
        Test_lists = crawl(path)
        for i in range(len(Control_list[0])):
            self.assertEqual(Control_list[0][i],Test_lists[0][i])
        for i in range(len(Control_list[1])):
            self.assertEqual(Control_list[1][i],Test_lists[1][i])

        del_dir('dir_1')

    def test_2_crawl_and_del(self):
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
        #       1.txt           
        #       2.txt
        #       3.txt
        #       4.txt
        #       5.txt
        #       - dir_2.1
        #       - dir_2.2
        #           6.txt
        #
        control_files = [ '1.py', '1.txt', '2.txt', '3.txt', '4.txt', '5.txt', '6.txt']
        control_dirs = ['dir_1', 'dir_2.1', 'dir_2.2']
        Control_list = []
        Control_list.append(control_files)
        Control_list.append(control_dirs)
        Test_lists = crawl(path)
        for i in range(len(Control_list[0])):
            self.assertEqual(Control_list[0][i],Test_lists[0][i])
        for i in range(len(Control_list[1])):
            self.assertEqual(Control_list[1][i],Test_lists[1][i])

        del_dir('dir_1')
        # так как есть вложенные каталоги, ничего не должно удалиться
        Test_lists = crawl(path)
        # снова обойдем каталог
        # и проверим, что все осталось на месте

        for i in range(len(Control_list[0])):
            self.assertEqual(Control_list[0][i],Test_lists[0][i])
        for i in range(len(Control_list[1])):
            self.assertEqual(Control_list[1][i],Test_lists[1][i])
            
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
