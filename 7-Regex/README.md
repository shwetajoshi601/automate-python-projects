# Regular Expressions

These are expressions that let you find certain patterns in your text.

## Cheatsheet

* {n} - match a character/group n times; e.g.: \d{3} - valid patterns: 444, 456
* {n,m} - match a character/group n to m times; e.g.: '(Ha){2,4}' -> HaHa, HaHaHa, HaHaHaHa
* {n,m}? - match a character/group n to m times but group() returns the shortest match possible;
* {n,} - match from n to any number of times
* {,m} - match any number of times upto m. (Starting from 0)
* | - match any of the patterns; e.g.: 'batman|martha' -> matches either batman or martha
* ? - zero or one occurrence of the pattern; e.g.: 'Bat(wo)?man' -> Batman, Batwoman
* '*' - zero or more occurrences; e.g.: 'Bat(wo)*man' -> Batman, Batwoman, Batwowowoman
* '+' - one or more occurrences; e.g.: 'Bat(wo)+man' -> Batwoman, Batwowoman, Batman: returns None
* ^ - match beginning of the string; e.g.: '^Hello' -> Hello World, Hello xyz
* $ - match end of the string; e.g.: '\d$' -> 'You no is 42'
* .(dot) - wildcard, match any single character except newline; e.g.: '.at' -> cat, sat, hat, mat
* .* - match anything except newline; e.g.: 'Fname: .*' -> will match anything after Fname: 
    
    Note: Using the re.DOTALL as the second argument to re.compile, you can match newline

### Character Classes
* \d - numerical character 0 to 9
* \D - any character that is not a numeric digit
* \w - word characters - letter, numeric digit, underscore
* \W - non-word characters - not a letter, numeric digit, underscore
* \s - space characters - space, tab, newline
* \S - non-space characters - not a space, tab, newline
* [] - match the characters in the brackets; e.g.: [0-5] -> matches 0,1,2,3,4,5; e.g.: [a-zA-Z0-9] - matches all lowercase letters, all uppercase letters and numbers
* [^] - match negation of the character class; e.g.: [^aeiou] -> matches all consonants (not vowels)

    Note: You do not need to escape special characters like ., ?,* in a character class   