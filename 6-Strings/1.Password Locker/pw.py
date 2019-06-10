#! python3
"""This is the shebang line for windows.
For OS X replace with: #! /usr/bin/env python3.
On Linux, the shebang line is #! /usr/bin/python3.
"""

PASSWORDS = {
    'email': 'abcd123456',
    'github': 'qwerty09865432',
    'qatar-airways':'wfdwhqfje;fenq'
}

import sys, pyperclip

if len(sys.argv) < 2: # no commandline args given
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for account ' + account + 'copied to clipboard!')
else:
    print('There is no account named '+ account)