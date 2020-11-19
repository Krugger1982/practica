from PIL import Image, ImageDraw, ImageColor
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

def inserting_picture(imagename):
    """ Function for making in opened picture some changes """    
    draw = ImageDraw.Draw(imagename)                            # создаем из него  "холст" (объект ImageDraw)
    draw.rectangle([imagename.size[0]//2 - 25, imagename.size[1]//2 - 25, imagename.size[0]//2 + 26, imagename.size[1]//2 + 26])
    # рисуем внутри пустой квадрат (линии квадрата будут белые, а заливка - прозрачная)
    draw.multiline_text((imagename.size[0]//2 - 13, imagename.size[1]//2 - 13), text='Hello,\nWorld', fill='white', align="center")
    # и вставлям текст, цвет шрифта будет белый
    del draw
    # закрываем "холст"

def reformatting_pictures(extension1, extension2, path='.'):
    """ Function for searching current folder  for pictures with specified extension
        and save them with a new extension """
    files = crawl('.')[0]
    for filename in files:
        if filename.find('.' + extension1) != -1:           # И если в нем есть файл с требуемым расширением
            current = Image.open(filename)                  # Открываем файл 
            inserting_picture(current)
            current.save(filename [:len(filename) - len(extension1)] + extension2)        # сохраняем его с новым расширением
