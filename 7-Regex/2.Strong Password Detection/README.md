# Strong Password Detection

Write a function that uses regular expressions to make sure the password string it is passed is strong. A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit. You may need to test the string against multiple regex patterns to validate its strength.

In this regex, we need to consider multiple possibilities.

A-Z followed by a-z followed by 0-9 or

a-z followed by A-Z followed 0-9

Any of these character classes can occur in the beginning end or middle.

We also need to match any character other than lowercase letters, uppercase letters and digits, such as special characters.

To restrict the string length, we use a positive lookahead. A positive lookahead is given by ?= and means, the following expression is matched but not returned in the results.