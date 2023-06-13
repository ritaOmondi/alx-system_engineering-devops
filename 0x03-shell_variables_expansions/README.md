                      0x03. Shell, init files, variables and expansions
0. alias ls="rm*": This ia an alias command
1. echo "hello $USER": Prints the word hello user.
2. PATH=$PATH:/action: Add /action to the PATH. /action should be the last directory the shell looks into when looking for a program
3. echo $PATH | tr ':' '\n' | wc -1 : counting the number of directories in PATH  
