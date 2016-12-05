folder = '/media/sun/Desktop/utilities/temp'

import os

listOfWords = ['letter', 'text', 'khoj']

for root, dirs,filenames in os.walk(folder):
    for dir in dirs:
        for word in listOfWords:
           if word in dir:
                print(word, ' in directory name : ', os.path.join(root, dir))

    for filename in filenames:
        fullpath = os.path.join(root, filename)

        for word in listOfWords:
            if word in filename:
                print( word, ' in filename : ', fullpath)

            if word in open(fullpath, encoding="ISO-8859-1").read():
                print( word, ' in filetext : ', fullpath)
