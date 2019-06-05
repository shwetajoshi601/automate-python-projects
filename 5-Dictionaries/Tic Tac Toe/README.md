# Tic Tac Toe using Dictionaries

A tic-tac-toe board looks like a large hash symbol (#) with nine slots that can each contain an X, an O, or a blank.

```
'top-L' | 'top-M' | 'top-R'
--------+---------+----------
'mid-L' | 'mid-M' | 'mid-R'
--------+---------+----------
'low-L' | 'low-M' | 'low-R'
```

We can use a dictionary to represent a tic-tac-toe board. 

```
Board =    {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
```
Here, each key represents the board positions and it's value represents 'X', 'O' or ' '.
