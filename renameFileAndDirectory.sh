#!/usr/bin/env python

folder = "/home/sun/Desktop/folder"

import os  # glob is unnecessary

replaceFrom = 'from'
replaceWith = 'with'

replaced = 1

def renameFolders(folder):
    global replaced
    for root, dirs, filenames in os.walk(folder):
        for dir in dirs:
            fullpath = os.path.join(root, dir)
            if replaceFrom in fullpath:
                newFullPath = fullpath.replace(replaceFrom, replaceWith)
                print("old: ", fullpath)
                print("new: ", newFullPath)
                os.rename(fullpath, newFullPath)
                replaced += 1


def renameFiles(folder):
    global replaced
    for root, dirs, filenames in os.walk(folder):
        for filename in filenames:
            fullpath = os.path.join(root, filename)
            if replaceFrom in filename:
                filename = filename.replace(replaceFrom, replaceWith)
                newFullPath = os.path.join(root, filename)
                print("old: ", fullpath)
                print("new: ", newFullPath)
                os.rename(fullpath, newFullPath)
                replaced += 1


if __name__ == '__main__':
    while replaced != 0:
        replaced = 0
        renameFolders(folder)
        renameFiles(folder)

