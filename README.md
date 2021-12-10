# Number System Translator

## Program Description
The Number System Translator is a program that allows its user to directly translate numbers between any number system from Base-1 up to Base-16. The program will prompt the user to input a number, the number system to be translated from, and the number system to be translated to. Then, it will return the translated number, and ask the user if there is any other number to be translated. In the case the answer is no, the program will end. Otherwise, the program will continue running.

![](Screenshots/Screen%20Shot%202021-12-09%20at%2011.10.02%20PM.png)

## Program Procedure
The program is made up of the following:

1. A list with the possible digits in a base-16 number system
2. A user_prompt() function
3. The decimal_to_other_base(number, n, list) function
4. The other_base_to_decimal(number, base) function
5. The base_to_base(number, from_base, to_base) function

### user_prompt()
