# Comma Code

Say you have a list value like this:
```
spam = ['apples', 'bananas', 'tofu', 'cats']
```

Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return :
```
'apples, bananas, tofu, and cats'
```

But your function should be able to work with any list value passed to it.

## Solution
There are two ways to solve this problem
1. Iterate over the list, check if the index is not the last index, add item and ', '
   For the last index, add 'and ' and then the item
2. Use the str.join method. This method takes the object to be converted to a string as a parameter.
   ```
   ','.join(['cat','hat'])

   This will give a string with value
   'cat,hat'
   ```
   Use the list slicing operator to pick the list upto the second last element. Join them using the join method with ', ' as the separator.
   Add the last element to the resulting string with ',and '
