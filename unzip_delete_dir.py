import zipfile
import os
import shutil

def removedir(f):
    if os.path.isdir(f):
        for i in os.listdir(f):
            print(i)
            if os.path.isdir('%s/%s' % (f, i)):
                removedir('%s/%s' % (f, i))
            else:
                os.remove('%s/%s' % (f, i))
    os.rmdir(f)

if __name__ == '__main__':
    s = os.getcwd()
    print('current path is %s')
    file_list = os.listdir()# default is current dir
    for f in file_list:
        if zipfile.is_zipfile(f):
            zf = zipfile.ZipFile(f, 'r')
            zf.extractall()
    file_list = os.listdir()
    for f in file_list:
        post = f.split('.')[-1]
        if post == 'url' or post == 'html':
            os.remove(f)
        elif post == 'pptx':
            os.rename(f, '%s.pptx' % file_list.index(f))
        if os.path.isdir(f):
            removedir(f)
            #for i in os.listdir(f):
            #    os.remove('%s/%s' % (f, i))
            #os.rmdir(f)
            #shutil.move(f + '/*.pptx', './')
