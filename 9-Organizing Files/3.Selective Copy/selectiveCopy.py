#! python3
# selectiveCopy.py - copies files with certain file extensions to another folder

import os, shutil

sourcePath = r'J:\STUDIES\AWS'
destPath = r'J:\STUDIES\GITHUB\AllPDFsAndJPG'

# walk through the folder
for folderName, subFolders, fileNames in os.walk(sourcePath):
    print('Scanning folder %s' % (folderName))
    # scan each file
    for fileName in fileNames:
        # if the extension is .jpg or .pdf
        if fileName.endswith('.jpg') or fileName.endswith('.pdf'):
            absPath = os.path.join(os.path.abspath(folderName), fileName)
            print('Copying %s to %s' % (absPath, os.path.abspath(destPath)))
            shutil.copy(absPath, os.path.abspath(destPath))
