#! python3

import pyperclip,re

# phone regex
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

# email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})      # dot-something
    )''', re.VERBOSE)

# copy text from the clipboard
text = str(pyperclip.paste())
matches = []
# extract all phone numbers
for groups in phoneRegex.findall(text):
    # join numbers e.g: 444-555-666
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    # check extension
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

# extract all emails
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Form a string and copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("Copied to clipboard:")
    print('\n'.join(matches))
else:
    print("No email addresses or phone numbers found!")