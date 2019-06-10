#! python3
"""
Adds Wikipedia bullet points to the start of each line of the text copied to the clipboard
"""
import pyperclip

# get the text from the clipboard
text = pyperclip.paste()

# modify the lines
# get a list of lines
lines = text.split('\n')
    # add a star before each line
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)
pyperclip.copy(text)