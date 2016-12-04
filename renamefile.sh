#!/usr/bin/env python

folder = "/media/sun/A4FE1C5EFE1C2AD6/EJBCA/tigerca-6.2.0"

import os # glob is unnecessary

replaceFrom = 'ejbca'
replaceWith = 'tigerca'

for root, dirs,filenames in os.walk(folder):
    for filename in filenames:
        fullpath = os.path.join(root, filename)
        filename_split = os.path.splitext(fullpath) # filename and extensionname (extension in [1])
        filename_zero, fileext = filename_split

        if replaceFrom in filename:

            filename = filename.replace(replaceFrom, replaceWith)
            newFullPath = os.path.join(root, filename)
            print fullpath
            print newFullPath
            os.rename(fullpath, newFullPath)
