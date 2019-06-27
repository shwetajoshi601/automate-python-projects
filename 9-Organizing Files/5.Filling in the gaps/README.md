# Filling in the Gaps

Write a program that finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on, in a single folder and locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt but no spam002.txt). Have the program rename all the later files to close this gap.

As an added challenge, write another program that can insert gaps into numbered files so that a new file can be added.

We need to use a regex to identify the prefix and the numbers:
For example,
```
^(spam)(\d)+(\.[a-z]+)
```
This regex will match all the file names of the pattern spam01.txt, spam001.txt, etc.