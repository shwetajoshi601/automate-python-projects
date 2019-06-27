#!python3

import shutil, os, re

# regex for date
datePattern = re.compile(r"""^(.*?)    # all text before the date
       ((0|1)?\d)-                     # one or two digits for the month
       ((0|1|2|3)?\d)-                 # one or two digits for the day
       ((19|20)\d\d)                   # four digits for the year
       (.*?)$                          # all text after the date
     """, re.VERBOSE)

# absolute path of the directory
path = r'J:\STUDIES\GITHUB\automate-python-projects\9-Organizing Files\1.Renaming Files to Eur style dates\test'
# loop over the files in the directory
for amerFilename in os.listdir(path):
    # check if the filename matches the regex
    mo = datePattern.search(amerFilename)
    # if no date in filename
    if mo == None:
        continue
    
    # store the parts of the regex for forming European style pattern
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # form the european fileName
    eurFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # form the absolute file paths
    amerFilePath = os.path.join(path, amerFilename)
    eurFilePath = os.path.join(path, eurFilename)

    # rename the files
    print('Renaming %s to %s' % (amerFilename, eurFilename))
    # shutil.move(amerFilename, eurFilename) # uncomment after testing