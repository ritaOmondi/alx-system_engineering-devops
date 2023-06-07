     1. pwd: It is used to show the current working directory.
     2. ls: Used to display the content of the current directory
     3. cd: This is used to navigate to the user's home directory
     4. ls -l : used to display files in long format. Files in the current working directory.
     5. ls -la: Displays the content of the current directories content in long format, even the ones with .
     6. ls -lan: Dispalys current directory's content in long format including user with ID and files with hidden characters
     7:/tmp$ mkdir my_first_directory : Creates the directory "my_first_directory" in the directory, "tmp" 
     8.mv -p /tmp/betty /tmp/my_first_directory/:Script used to move the filr betty from tmp to tmp/my_first_directory
     9. rm /tmp/my_first_directory/betty: Deleting the file betty from the directory in tmp directory.
     10. rm -r /tmp/my_first_directory: Deleting the directory my_first_directory.
     11. cd - : a script that changes the working directory to the previous one.
     12. ls -la "$(pwd)" "$(dirname "$(pwd)")" /boot: Displaying all content in the in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.
     13: file -b /tmp/iamafile:  a script that prints the type of the file named iamafile. The file iamafile will be in the /tmp directory when we will run your script.
     14.ln -s /bin/ls __ls__ : Used to create a symbolic link.
     15. find . -name "*.html" -exec cp -u {} .. \;: Editing parent directory with information that was poriginally not prrsent in the parent director.
     16: mv [A-Z]* /tmp/u/:  a script that moves all files beginning with an uppercase letter to the directory /tmp/u.

You can assume that the directory /tmp/u will exist when we will run your script. 
     17: rm -f *~ : a script that deletes all files in the current working directory that end with the character ~
      18: mkdir welcome; mkdir welcome/to; mkdir welcome/to/school: Creating the three directories oin the current working directory.
      
