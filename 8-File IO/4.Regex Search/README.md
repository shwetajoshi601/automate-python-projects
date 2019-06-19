# Regex Search

Write a program that opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression. The results should be printed to the screen.

The "test" folder contains sample files used in the program. Make sure you change the path according to your system.

Following is the input and output you receive on running the program:
```
>python regexSearch.py

Enter a regular expression: (NAME|ADDRESS)|(\+91-\d{3}-\d{3}-\d{4})
Matches for file test.txt:
[('NAME', ''), ('ADDRESS', '')]
Matches for file test2.txt:
[('', '+91-779-882-3359')]

```