import re

# function to strip the characters from the beginning and end of the string
# default value for sep is '\s'. If no characters are given, by default whitespaces will be removed

def strip(string, sep=r'\s'):
    # the string either begins with the pattern, or ends
    regStr = '(^[' + sep + ']+)|([' + sep + ']+$)'
    regex = re.compile(regStr)
    # if there is a match at the beg or end, replace it with an empty '' to remove it
    return regex.sub('', string)

# removes characters abcd from th beg/end
print(strip('aaaaabcdMy name is Shwetabcdddd','abcd'))
# does not remove any characters since abcd are not present at the beg/end
print(strip('   aaaaabcdMy name is Shwetabcdddd     ','abcd'))
# removes the spaces and tabs by default
print(strip('   aaaaabcdMy name is Shwetabcdddd     '))
# does not remove any characters since the sep is empty
print(strip('   aaaaabcdMy name is Shwetabcdddd     ', ''))