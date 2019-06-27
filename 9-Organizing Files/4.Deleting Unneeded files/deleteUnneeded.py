#! python3
# deleteUnneeded.py - finds the files and folders that exceed size 100MB for deleting

import os

srcPath = r'J:\STUDIES\AWS'

# walk through th folder
for folderName, subFolders, fileNames in os.walk(srcPath):
    # iterate throught the folders
    for subFolder in subFolders:
        absFolder = os.path.abspath(os.path.join(folderName,subFolder))
        if(os.path.getsize(absFolder) > 100000000):
            print('Folder %s ' % (absFolder))
    # iterate through the files
    for fileName in fileNames:
        absFile = os.path.abspath(os.path.join(folderName, fileName))
        if(os.path.getsize(absFile) > 100000000):
            print('File %s ' % (absFile))