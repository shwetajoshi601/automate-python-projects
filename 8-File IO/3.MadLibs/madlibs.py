#! python3
# usage - python madlibs.py

import re
# open the file for reading
fileObj = open('madlibs.txt','r')
content = fileObj.read()

regex = re.compile(r'NOUN|VERB|ADVERB|ADJECTIVE')
for token in regex.findall(content):
    val = input('Enter a/an '+ token.lower() + ': ')
    content = content.replace(token, val, 1)

print(content)
newFile = open('madlibs_result.txt', 'w')
newFile.write(content)
