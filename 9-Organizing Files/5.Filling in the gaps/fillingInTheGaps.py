#! python3

import os, re, shutil

# function to fill gaps in file numbering
def fillGaps(folderPath, prefix):
    # find the absolute path
    folderPath = os.path.abspath(folderPath)

    # regex to match filenames with the prefix
                       #     spam        001   .txt
    regex = re.compile('^(' + prefix + ')(\d+)(\.[a-z]+)')

    # store the file numbers in a list
    numbers = []
    for file in os.listdir(folderPath):
        # print(file)
        # if it is a file
        if(os.path.isfile(os.path.join(folderPath, file))):
            # match with the regex
            mo = regex.search(file)
            if mo == None:
                continue

            # find the length of the number string to identify how many zeroes are needed
            # for 002 -> numLen = 3
            numLen = len(mo.group(2))
            # add 2 in numbers list
            numbers.append(int(mo.group(2)))
            # .txt
            extn = mo.group(3)
    # for files spam001.txt, spam002.txt, spam004.txt
    # numbers = [1,2,4]
    numbers = sorted(numbers)
    print(str(numbers))

    # iterate from 1 to number of files in order (1,2,3)
    for i in range(1, len(numbers) + 1):
        # for i = 3
        # newFilename = spam + 00 + 3 + .txt = spam003.txt
        newFilename = prefix + '0'*(numLen - len(str(i))) + str(i) + extn
        # if this file does not exist
        if not os.path.exists(os.path.join(folderPath, newFilename)):
            # find the next actual filename
            # oldNum = numbers[3-1] = numbers[2] = 4 (refer line:33)
            oldNum = numbers[i-1]
            # oldFilename = spam + 00 + 4 + .txt = spam004.txt
            oldFilename = prefix + '0'*(numLen - len(str(oldNum))) + str(oldNum) + extn
            print('Renaming %s to %s' % (oldFilename, newFilename))
            # rename spam004.txt to spam003.txt
            shutil.move(os.path.join(folderPath, oldFilename), os.path.join(folderPath, newFilename))

if __name__ == '__main__':
    fillGaps(r'J:\STUDIES\GITHUB\automate-python-projects\9-Organizing Files\5.Filling in the gaps\test', 'spam')
