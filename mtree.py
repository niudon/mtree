#!/usr/bin/python2.7 

import os
path = '.'
sepra = '    '
prefix = ''

def showpath(path, index):
    lis = os.listdir(path)
    for fil in lis:
        filtmp = path + '/' + fil
        if os.path.isdir(filtmp):
            print index*sepra + '+ ' + fil
            showpath(filtmp, index + 1)
        else:
            print index*sepra + '- ' + fil

showpath('.', 0)

