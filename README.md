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

### user_prompt() function
This function prompts the user to input a number, the number system to be translated from, and the number system to be translated to. Then it will store the information collected from the user in variables and call the base_to_base(number, from_base, to_base) function to convert the number. After, it ask the user if there is any other number to be converted. In case there is another number to be converted, the function will call itself

![](Screenshots/Screen%20Shot%202021-12-09%20at%2011.35.31%20PM.png)

### base_to_base(number, from_base, to_base) function
This function will translate the number indicated in the first parameter from the base indicated in the second parameter to decimal by calling the other_base_to_decimal() function, and store it in a temporal variable. After that it will translate the code from decimal to the base indicated in the third parameter by calling the decimal_to_other_base() function. 
If the user is intending to translate from decimal, it will only call the decimal_to_other_base() function. And if the user is intending to translate to decimal, it will only call the other_base_to_decimal() function

![](Screenshots/Screen%20Shot%202021-12-09%20at%2011.36.29%20PM.png)
