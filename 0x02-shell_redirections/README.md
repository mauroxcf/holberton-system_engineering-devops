# Shell Redirection Project

in this project we will explore the feature used by many command line programs called input/output redirection. By using some special notations we can redirect the output of many commands to files, devices, and even to the input of other commands.

# How we will do that

-to standard output. By default, always directs its contents to the display. To redirect standard output to a file, the ">" character.

-to standard input. By default, standard input gets its contents from the keyboard, it can be redirected to with the "<" character in the command line.

### How this will useful

with this we can print to a file the results generated of a output to a file... same goes with the input but in other way, its use to print the inputs of the commands and combine with other options o redirect to standard output.

#### Characters and Description ####

| Characters | Description |
| ------ | ------ |
| > | redirect standard output to a file, etc. |
| >> | new results are added to the end of the file |
| < | redirect standard input from a file instead of the keyboard |
| "|"| pipeline connect multiple commands together |


### Deployment

standard input/output have rules, type "comand" + "standard input/output option depending what you need" + file,directory,etc its gonna affect.
yo see more, read the manpages of the commands.

few examples

command ls, ">" standard output to print in the file_list.txt
```sh
$ ls > file_list.txt
```

command sort, "<" standard input, print the file_list.txt in to the command sort and displau y the terminal:
```sh
$ sort < file_list.txt
```

command ls-l, pipeline "|" to combine with the command less.
```sh
$ ls -l | less
```
#### CREDITS

HOLBERTON SCHOOL