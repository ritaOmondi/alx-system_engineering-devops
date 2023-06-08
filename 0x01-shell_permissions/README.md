      0. su betty : changes the user to better
      1. whoami : command used to print the usernam eof the current user
      2. groups: script used to print all the groups the current user is on.
      3. chown betty hello:  used to change owenership of file hello to the user betty.
      4. touch hello : creates an empty file called hello
      5. chmod u+x hello :  a script that adds execute permission to the owner of the file hello
      6. ug+x,o+r: gives executable rights to user and the group owner, as well as giving reading rights to other users.
      7. ugo+x or a+x hello: gives executable rightsto all references.
      8. chmod 007 hello: giving all rights to other users and deniying group and owners.
      9.chmod 753 hello: interpreting -rwxr-r-wx without commas.
      10. chmod --reference=olleh hello: sets the mode of the file hello the same as olleh’s mode.
      11.chmod -R ugo+x .: script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users.
      12.mkdir -m 751 my_dir:script that creates a directory called my_dir with permissions 751 in the working directory.
      13. chgrp: used to change group owner of a particular file.
     14. chown vincent:staff *:  a script that changes the owner to vincent and the group owner to staff for all the files and directories in the working directory. 
      15. chown -h vincent:staff _hello:
      16.chown --from=guillaume betty hello
      17. 
