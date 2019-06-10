# The pyperclip Module

The pyperclip module is used for copying text to and from your system's clipboard. This module does not come bundled with python. You have to install it.

If you are using linux, you can install it using pip
```
pip install pyperclip
```

## Installing pip
If you do not have pip installed:

Download [this](https://bootstrap.pypa.io/get-pip.py) script, save it as 'get-pip.py'

Open the windows command prompt, run this script:
```
python get-pip.py
```
Check if it is successfully installed:
```
pip -V
or
pip3 -V
```

If you get and error "pip is not recognized as an internal or external command",
you need to add the path of pip.exe or pip3.exe to the PATH system environment variable.
Re-open the command prompt and try again.

For more details on installing modules refer [this](https://automatetheboringstuff.com/appendixa/) link

## Using pyperclip

```
import pyperclip

pyperclip.copy("Hello World!!")
print(pyperclip.paste())        # prints Hello World!!

```

## Running python programs

When you use IDLE to execute your python statements, you will not be able to pass commadline arguments to your programs.

To pass commandline arguments, you need to run python programs on your local system using the python command:
```
python <filename>.py> <cmdline_args>
```

## Creating batch programs
If you are using windows, you can also create batch files so that you don't have to run the script using the python command each time. Running the scripts would just mean using Windows + R and typing the filename