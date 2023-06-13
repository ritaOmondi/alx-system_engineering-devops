                      0x03. Shell, init files, variables and expansions
0. alias ls="rm*": This ia an alias command
1. echo "hello $USER": Prints the word hello user.
2. PATH=$PATH:/action: Add /action to the PATH. /action should be the last directory the shell looks into when looking for a program
3. echo $PATH | tr ':' '\n' | wc -1 : counting the number of directories in PATH
4. Printenv: lists all global variables.
5. set: command used to list all varibales and functions
6. BEST="School" : creating a new local variable
7. export BEST= "School": converting local variable to environment variable.
8. echo $((128 + $TRUKNOWLEDGE)): The sum of 128 and the value held id variable "TRUKNOWLEDGE"
9. echo $((POWER/DIVIDE)): Dividing two global variables
10. echo $((BREATH**LOVE)): Exponential values.
11. echo $((2#BINARY)): converting a number from base 2 to base 10.
12. echo {a..z}{a..z} | tr '' '\n' | grep -v "oo"
13. printf '%.2f\n' $NUM
14.  
