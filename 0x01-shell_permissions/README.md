# Concede permissions


in this proyect, we learn how to concede permissions to file and directorys
# How we will do that

there its a list of command that will concede a series of permissions depending of what we need, open the terminal window in your Unix operating systems and type the comand of this category.


### How this will useful

with this that more than one user can be operating the computer at the same time used to get a optimal perform on large projects, we can grants superuser permissiones to modify files, installs apps, write then, change the owners, to other user that are connect in the same terminal by internet. this remote users can log in via ssh (secure shell).

#### Commands and Description ####


| Command | Description |
| ------ | ------ |
| chmod | modify file access rights |
| su | temporarily become the superuser |
| sudo | temporarily become the superuser |
| chown | change file ownership |
| chgrp| change a file's group ownership |



### Deployment

each command have rules, type "comand" + "OPTION you need depending the rights you gonna concede to the other user, or other option".
yo see more, read the manpages of this commands.

few examples

command chmod, "xxx" these are binary numbers that represents the permissions you are gonna concede to other users
```sh
$ chmod 777 file_name
```

command sudo,  concede a temporaly superuser permission + the command we gonna affect:
```sh
$ su apt-get install emacs
```

command chown, changing owner of a file to other user
```sh
$ chown holberton file_name
```
#### CREDITS

HOLBERTON SCHOOL