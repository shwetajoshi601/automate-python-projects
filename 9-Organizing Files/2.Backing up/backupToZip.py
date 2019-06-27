#! python3

# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os

# function to backup the entire contents of folder into a zip file
def backupToZip(folder):
    # make sure the folder is an absolute path
    folder = os.path.abspath(folder)

    # find the filename for zip file based on what files exist in the folder
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        # non-existent filename
        if not os.path.exists(zipFilename):
            break
        # increment the number since the filename exists
        number += 1
    
    # create the zip file
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')
    # walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)
        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue   # don't backup the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()

# function call
backupToZip(r'J:\STUDIES\GITHUB\automate-python-projects\8-File IO')