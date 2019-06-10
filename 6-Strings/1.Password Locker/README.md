# Password Locker

You probably have accounts on many different websites. It’s a bad habit to use the same password for each of them because if any of those sites has a security breach, the hackers will learn the password to all of your other accounts. It’s best to use password manager software on your computer that uses one master password to unlock the password manager. Then you can copy any account password to the clipboard and paste it into the website’s Password field.

The password manager program you’ll create in this example isn’t secure, but it offers a basic demonstration of how such programs work.

## Data structure
Since we need to organize the passwords for various accounts, we can use a dictionary data structure map the password to it's respective account
```
{
    'email': 'wegksalkasc',
    'blog': '24736rbwjdn;A[0IPOQWU]'
}
```
## Running the program
To add account details in this password locker, the user must enter a commandline argument.

```
python pw.py [account_name]
```
Commandline arguments are stored in sys.argv.

argv[0] is the name of the python file and argv[1] onwards contain the commandline arguments

We have used the pyperclip module to copy the account password to clipboard if it already exists in the password manager program.

Using this script you can easily copy complex passwords without remembering them! Each time you need to add a new password to the dictionary, update the PASSWORDS variable and run the script

### Running using a batch file
If you are using windows, create a pw.bat file (file given in this folder).
Replace the placeholder with the path of your pw.py file. Make sure there are no spaces in the path. For convenience, you may place it in C:\Windows

Place the .bat file in C:\Windows
```
Press Windows + R, type pw <account_name>
```