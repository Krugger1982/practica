import os.path

def crawl (dir_adress='.'):
    Dirs = []
    Files = []
    result = []
    for root, dirs, files in os.walk(dir_adress):
        Dirs += dirs
        Files += files
    result.append(Files)
    result.append(Dirs)

    return result


def del_dir(dir_adress='.'):
    try:
        content = crawl (dir_adress)
        files = content[0]
        dirs = content[1]
        if len(dirs) == 0:
            for file in files:
                os.remove(dir_adress + '/' + file)
            os.rmdir(dir_adress)
    except OSError:
        return 
