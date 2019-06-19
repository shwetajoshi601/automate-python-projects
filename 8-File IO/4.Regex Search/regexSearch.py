#! python3

import re, os

regex = re.compile(input('Enter a regular expression: '))
dirPath = r'J:\STUDIES\GITHUB\automate-python-projects\8-File IO\4.Regex Search\test'

for file in os.listdir(dirPath):
    if file.endswith('.txt'):
        fileObj = open(os.path.join(dirPath, file))
        content = fileObj.read()
        matches = regex.findall(content)
        print('Matches for file ' + file + ':')
        print(str(matches))